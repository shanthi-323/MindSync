import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from supabase import create_client
from datetime import datetime

# Supabase configuration
SUPABASE_URL = "https://ywqhxcbcyeytashknble.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl3cWh4Y2JjeWV5dGFzaGtuYmxlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM3NTY0MjYsImV4cCI6MjA0OTMzMjQyNn0.O2N4AVNlIyCYaugtRI0LPnO5YkA2EMNyHOimbdyoRlk"  # Replace with your Supabase API key
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Label Mapping
LABEL_MAPPING = {
    0: "Mind Reading",
    1: "Overgeneralization",
    2: "Magnification",
    3: "Labelling",
    4: "Personalization",
    5: "Fortune Telling",
    6: "Emotional Reasoning",
    7: "Mental Filter",
    8: "Should Statements",
    9: "All-or-Nothing Thinking",
    10: "Catastrophizing",
    11: "Disqualifying the Positive",
    12: "Jumping to Conclusions",
    13: "Blaming",
    14: "Comparisons"
}

# Cognitive Distortion Explanations and Coping Strategies
DISTORTION_DETAILS = {
    "Mind Reading": {
        "explanation": "Assuming you know what others are thinking without evidence.",
        "coping": [
            "Ask for clarification instead of assuming.",
            "Challenge your assumption with evidence."
        ]
    },
    "Overgeneralization": {
        "explanation": "Drawing broad negative conclusions based on a single event.",
        "coping": [
            "Look for exceptions to the rule.",
            "Focus on specific instances rather than broad conclusions."
        ]
    },
    "Magnification": {
        "explanation": "Exaggerating the importance of problems or shortcomings.",
        "coping": [
            "Ask yourself if you are overestimating the problem.",
            "Focus on the positives and balance your perspective."
        ]
    },
    "Labelling": {
        "explanation": "Attaching negative labels to yourself or others.",
        "coping": [
            "Replace labels with specific descriptions of behavior.",
            "Recognize that one action does not define a person."
        ]
    },
    "Personalization": {
        "explanation": "Blaming yourself for things outside your control.",
        "coping": [
            "Consider other factors that might have influenced the situation.",
            "Remind yourself that not everything is about you."
        ]
    },
    "Fortune Telling": {
        "explanation": "Predicting negative outcomes without proof.",
        "coping": [
            "Focus on the present instead of predicting the future.",
            "Challenge the belief that you can accurately predict outcomes."
        ]
    },
    "Emotional Reasoning": {
        "explanation": "Believing something is true because you feel it strongly.",
        "coping": [
            "Separate feelings from facts.",
            "Look for evidence that supports or disproves your feelings."
        ]
    },
    "Mental Filter": {
        "explanation": "Focusing exclusively on negative details while ignoring positive aspects.",
        "coping": [
            "List both positive and negative aspects of the situation.",
            "Actively seek out the positives to create a balanced view."
        ]
    },
    "Should Statements": {
        "explanation": "Criticizing yourself or others with rigid 'should' or 'must' statements.",
        "coping": [
            "Replace 'should' with 'could' to allow for flexibility.",
            "Focus on realistic and compassionate self-talk."
        ]
    },
    "All-or-Nothing Thinking": {
        "explanation": "Seeing things in absolute, black-and-white categories.",
        "coping": [
            "Identify gray areas and consider alternatives.",
            "Acknowledge progress instead of perfection."
        ]
    },
    "Catastrophizing": {
        "explanation": "Expecting the worst possible outcome in any situation.",
        "coping": [
            "Ask yourself if the worst-case scenario is truly likely.",
            "Focus on what you can control in the situation."
        ]
    },
    "Disqualifying the Positive": {
        "explanation": "Rejecting positive experiences by insisting they 'don't count'.",
        "coping": [
            "Accept compliments and achievements without discounting them.",
            "Remind yourself that positive experiences are valid and real."
        ]
    },
    "Jumping to Conclusions": {
        "explanation": "Making negative interpretations without actual evidence.",
        "coping": [
            "Ask for clarification before making assumptions.",
            "Seek evidence to support your conclusions."
        ]
    },
    "Blaming": {
        "explanation": "Holding yourself or others responsible for things not entirely in their control.",
        "coping": [
            "Consider shared responsibility in the situation.",
            "Focus on solutions rather than assigning blame."
        ]
    },
    "Comparisons": {
        "explanation": "Constantly measuring yourself against others in a negative way.",
        "coping": [
            "Focus on your own progress and achievements.",
            "Remind yourself that everyone's journey is unique."
        ]
    }
}


@st.cache_resource
def load_model():
    """
    Load the pre-trained model and tokenizer with caching to improve performance.
    """
    model_name = "shanthi-323/fine-tuned-bert-CBT"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name).to("cpu")
    return model, tokenizer

def classify_text(input_text, model, tokenizer):
    """
    Classify the input text using the pre-trained model.
    """
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to("cpu")
    
    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the predicted label
    predicted_label = outputs.logits.argmax(dim=1).item()
    predicted_label_description = LABEL_MAPPING.get(predicted_label, "Unknown Label")
    
    return predicted_label, predicted_label_description

def save_to_supabase(input_text, label, reframe):
    """
    Save the analysis results to the Supabase database.
    """
    record = {
        "input": input_text,
        "label": label,
        "reframe": reframe if reframe.strip() else None,
        "created_at": datetime.now().isoformat()
    }
    response = supabase.table("thoughts").insert(record).execute()
    return response.status_code == 201

def main():
    # Set page configuration
    st.set_page_config(
        page_title="CBT Cognitive Distortions Classifier",
        page_icon="🧠",
        layout="centered"
    )

    # Title and description
    st.title("🧠 Cognitive Distortions Analyzer")
    st.markdown("""
    Enter a statement, and the app will help you recognize potential cognitive distortions in your thinking patterns.
    """)

    # Load the model
    model, tokenizer = load_model()

    # Text input
    st.markdown("### 📝 Enter Your Thought")
    user_input = st.text_area(
        "Enter a thought you'd like to analyze:",
        placeholder="Type here...",
        height=150
    )

    # Analyze button
    if st.button("Analyze Thought", type="primary"):
        if user_input.strip():
            # Perform classification
            predicted_label, label_description = classify_text(user_input, model, tokenizer)
            details = DISTORTION_DETAILS.get(label_description, {"explanation": "No detailed explanation available.", "coping": []})

            # Display results in a styled format
            st.success(f"### 💡 Identified Cognitive Distortion: **{label_description}**")
            st.markdown(f"""
            **What This Means:**  
            {details['explanation']}
            """)

            # Coping strategies
            if details["coping"]:
                st.markdown("### 🛠️ Coping Strategies")
                for idx, strategy in enumerate(details["coping"], 1):
                    st.markdown(f"{idx}. {strategy}")

            # Encouraging tips section
            st.info("""
            Recognizing these patterns is the first step to healthier thinking. 
            Take a moment to challenge and reframe your thoughts compassionately.
            """)

            # Save to Supabase
            reframed_thought = st.text_area(
                "Reframe your thought to a more balanced perspective:",
                placeholder="Type a revised version of your thought here..."
            )
            if st.button("Save Thought"):
                if save_to_supabase(user_input, label_description, reframed_thought):
                    st.success("Your thought has been saved successfully!")
                else:
                    st.error("An error occurred while saving your thought.")
        else:
            st.warning("Please enter a thought to analyze.")

    # Footer
    st.markdown("---")
    st.markdown("""
    *This tool is for educational purposes and is not a substitute for professional mental health advice.*
    """)

if __name__ == "__main__":
    main()