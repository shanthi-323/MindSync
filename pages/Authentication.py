import streamlit as st
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = "https://ywqhxcbcyeytashknble.supabase.co"  # Replace with your Supabase project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl3cWh4Y2JjeWV5dGFzaGtuYmxlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM3NTY0MjYsImV4cCI6MjA0OTMzMjQyNn0.O2N4AVNlIyCYaugtRI0LPnO5YkA2EMNyHOimbdyoRlk"  # Replace with your Supabase API key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Functions for authentication
def sign_up(email, password):
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})
        if response.user:
            return {"success": True, "user": response.user}
        elif response.error:
            return {"success": False, "error": response.error.message}
    except Exception as e:
        return {"success": False, "error": str(e)}

def sign_in(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if response.user:
            return {"success": True, "user": response.user}
        elif response.error:
            return {"success": False, "error": response.error.message}
    except Exception as e:
        return {"success": False, "error": str(e)}

def reset_password(email):
    """
    Trigger a password reset email.
    """
    try:
        response = supabase.auth.reset_password_for_email(email)
        if response.error:
            return {"success": False, "error": response.error.message}
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

# Main UI
def main():
    st.set_page_config(page_title="MindSync : Mental Health Support Platform with AI-Chatbot", page_icon="💖", layout="centered")

    st.sidebar.title("🔐 Authentication Menu")
    auth_option = st.sidebar.radio("Choose an option:", ["Sign In", "Sign Up", "Forgot Password"])

    st.title("💖 MindSync : Mental Health Support Platform with AI-Chatbot")
    st.markdown("Welcome to the app! Please sign in, sign up, or reset your password.")

    if auth_option in ["Sign In", "Sign Up"]:
        email = st.text_input("📧 Email", placeholder="Enter your email")
        password = st.text_input("🔑 Password", placeholder="Enter your password", type="password")

        if auth_option == "Sign Up" and st.button("Sign Up", key="signup"):
            if email and password:
                response = sign_up(email, password)
                if response["success"]:
                    st.success("🎉 Sign-Up Successful! Please check your email to confirm your account.")
                else:
                    st.error(f"❌ Sign-Up Failed: {response['error']}")
            else:
                st.warning("⚠️ Please fill in both email and password fields.")

        if auth_option == "Sign In" and st.button("Sign In", key="signin"):
            if email and password:
                response = sign_in(email, password)
                if response["success"]:
                    st.success(f"🎉 Welcome back, {response['user'].email}!")
                    st.session_state["user"] = response["user"]
                else:
                    st.error(f"❌ Sign-In Failed: {response['error']}")
            else:
                st.warning("⚠️ Please fill in both email and password fields.")

    elif auth_option == "Forgot Password":
        email = st.text_input("📧 Enter your email to reset password", placeholder="Enter your email")
        if st.button("Send Reset Email", key="reset"):
            if email:
                response = reset_password(email)
                if response["success"]:
                    st.success("✅ A password reset email has been sent! Please check your inbox.")
                else:
                    st.error(f"❌ Failed to send reset email: {response.get('error', 'Unknown error.')}") #
            else:
                st.warning("⚠️ Please provide your email address.")

    if "user" in st.session_state:
        st.markdown(f"### 👋 Welcome, **{st.session_state['user'].email}**!")
        st.info("You are successfully logged in. Explore the app features below!")

        if st.button("Log Out", key="logout"):
            del st.session_state["user"]
            st.success("👋 You have been logged out. See you next time!")

    # Footer
    st.markdown("---")
    st.markdown("""
    *This tool is for educational purposes and is not a substitute for professional mental health advice.*
    """)

if __name__ == "__main__":
    main()     