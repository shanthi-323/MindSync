import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
        # Initialize API key from environment
        self._initialize_api_key()
        
        # Initialize OpenAI client
        self._initialize_openai_client()
        
        # Initialize session state for conversation history
        self._initialize_session_state()
    
    def _initialize_api_key(self):
        """
        Retrieve API key from environment variables
        """
        # Attempt to get API key from environment
        api_key = os.getenv("OPENAI_API_KEY")
        
        # Check if API key exists
        if not api_key:
            st.error("OpenAI API Key not found in .env file")
            st.info("Please add OPENAI_API_KEY to your .env file")
            st.stop()
        
        # Store API key in session state
        st.session_state.openai_api_key = api_key
    
    def _initialize_openai_client(self):
        """
        Initialize OpenAI client with API key
        """
        try:
            self.client = OpenAI(api_key=st.session_state.openai_api_key)
        except Exception as e:
            st.error(f"Failed to initialize OpenAI client: {e}")
            st.stop()
    
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
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.conversation
            )
            
            # Extract AI response
            ai_response = response.choices[0].message.content
            
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
