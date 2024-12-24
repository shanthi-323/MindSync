import streamlit as st
import openai

# Retrieve the OpenAI API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]

# Set the OpenAI API key
openai.api_key = api_key

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

class StreamlitOpenAIChatbot:
    def __init__(self):
        """
        Initialize the Streamlit OpenAI Chatbot
        """
        # Initialize session state for conversation history
        self._initialize_session_state()
    
    def _initialize_session_state(self):
        """
        Initialize or reset session state variables
        """
        # Initialize conversation history if not exists
        if 'conversation' not in st.session_state:
            st.session_state.conversation = [
                {"role": "system", "content": "You are a helpful AI assistant. Be concise and friendly."}
            ]
    
    def generate_response(self, user_input):
        """
        Generate AI response using OpenAI API
        
        :param user_input: User's message
        :return: AI's response
        """
        try:
            # Add user message to conversation
            st.session_state.conversation.append(
                {"role": "user", "content": user_input}
            )
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.conversation
            )
            
            # Extract AI response
            ai_response = response.choices[0].message["content"]
            
            # Add AI response to conversation
            st.session_state.conversation.append(
                {"role": "assistant", "content": ai_response}
            )
            
            return ai_response
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return "Sorry, I'm having trouble processing your request."
    
    def render_chat_interface(self):
        """
        Render the Streamlit chat interface
        """
        # Title and description
        st.title("🤖 AI Chatbot")
        st.write("Chat with an intelligent AI assistant powered by OpenAI")
        
        # Display chat messages from history
        for message in st.session_state.conversation[1:]:  # Skip system message
            if message['role'] != 'system':
                with st.chat_message(message['role']):
                    st.write(message['content'])
        
        # Chat input
        if prompt := st.chat_input("What would you like to chat about?"):
            # Display user message
            with st.chat_message("user"):
                st.write(prompt)
            
            # Generate and display AI response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = self.generate_response(prompt)
                    st.write(response)
        
        # Additional sidebar controls
        with st.sidebar:
            # Reset conversation button
            if st.button("🔄 Reset Conversation"):
                st.session_state.conversation = [
                    {"role": "system", "content": "You are a helpful AI assistant. Be concise and friendly."}
                ]
                st.rerun()
            
            # Model selection
            st.selectbox(
                "Select AI Model", 
                ["gpt-3.5-turbo", "gpt-4"]
            )

def main():
    chatbot = StreamlitOpenAIChatbot()
    chatbot.render_chat_interface()

if __name__ == "__main__":
    main()
