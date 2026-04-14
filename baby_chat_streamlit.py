

# ============================================================
# STEP 1: Install dependencies
# Uncomment the line below if running in Colab:
#!pip install anthropic streamlit -q
# ============================================================
 
import os
 
# ============================================================
# STEP 2: Set your API key
# Replace with your actual key, or set it as an environment variable
# ============================================================
API_KEY = "sk-XXX"
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
 
# ============================================================
# DETECT ENVIRONMENT
# ============================================================
def is_streamlit():
    try:
        import streamlit as st
        return True
    except ImportError:
        return False
 
 
# ============================================================
# COLAB / TERMINAL VERSION old sonnet-4-20250514 new sonnet-4-6-20260217
# ============================================================
def run_colab_chat():
    from anthropic import Anthropic
 
    client = Anthropic(api_key=API_KEY)
    messages = []
 
    print("=" * 40)
    print("  Simple Chatbot (type 'quit' to exit)")
    print("=" * 40)
 
    while True:
        user_input = input("\nYou: ")
 
        if user_input.strip().lower() in ("quit", "exit", "q"):
            print("\nGoodbye!")
            break
 
        messages.append({"role": "user", "content": user_input})
 
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=messages,
        )
 
        reply = response.content[0].text
        messages.append({"role": "assistant", "content": reply})
 
        print(f"\nBot: {reply}")
 
 
# ============================================================
# STREAMLIT VERSION
# ============================================================
def run_streamlit_chat():
    import streamlit as st
    from anthropic import Anthropic
 
    st.set_page_config(page_title="Simple Chatbot", page_icon="💬")
    st.title("💬 Simple Chatbot")
 
    client = Anthropic(api_key=API_KEY)
 
    # Initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = []
 
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
 
    # Chat input
    if user_input := st.chat_input("Type a message..."):    
    
        if user_input.strip().lower() in ("quit", "exit", "q"):
            print("\nGoodbye!")
            break
     
     # Show user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
 
        # Get bot response
        with st.chat_message("assistant"):
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                messages=st.session_state.messages,
            )
            reply = response.content[0].text
            st.write(reply)
 
        st.session_state.messages.append({"role": "assistant", "content": reply})
 
 
# ============================================================
# RUN
# ============================================================
#try:
#    import streamlit as st
#   # If we can access runtime, we're in Streamlit
#   if hasattr(st, "runtime"):
run_streamlit_chat()
#    else:
#        run_colab_chat()
#except Exception:
#run_colab_chat()
 
