import streamlit as st
from faq import ingest_faq_data, faq_chain
from pathlib import Path
from router import router
from sql import sql_chain
from smalltalk import talk

# Page Configuration
st.set_page_config(
    page_title="EcomBot",
    page_icon="🛍️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1E3A8A, #3B82F6);
        padding: 0.9rem 2rem;           /* Reduced height */
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        width: 100%;
    }
    .main-header h1 {
        font-size: 2.6rem;
        margin: 0;
        font-weight: 700;
    }
    .main-header p {
        font-size: 1.2rem;
        margin: 4px 0 0 0;
        opacity: 0.95;
    }
    
    /* Outer Container Border */
    .main .block-container {
        border: 2px solid #e2e8f0;
        border-radius: 20px;
        padding: 2rem 2.5rem;
        background-color: white;
        max-width: 1200px;
        margin: 1rem auto;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    
    /* Larger Message Boxes */
    .stChatMessage {
        padding: 18px 22px !important;
        border-radius: 18px !important;
        font-size: 1.05rem !important;
        line-height: 1.55 !important;
    }
    
    .stChatInput textarea {
        font-size: 1.1rem !important;
        height: 68px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ===================== HEADER (Reduced Height) =====================
st.markdown("""
    <div class="main-header">
        <h1>🛍️ EcomBot</h1>
        <p>Your Smart E-commerce Shopping Assistant</p>
    </div>
""", unsafe_allow_html=True)

# Ingest FAQ Data
faqs_path = Path(__file__).parent / "resources/faq_data.csv"
ingest_faq_data(faqs_path)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hi! 👋 Welcome to EcomBot. How can I help you today? Ask me about products, orders, refunds, or policies."
        }
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Routing Function
def ask(query):
    route = router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    elif route == 'small_talk':
        return talk(query)
    else:
        return "Sorry, I didn't understand that. Feel free to ask about products, return policy, or track orders."

# Chat Input
query = st.chat_input("Type your message here... (e.g., Puma shoes under 3000, refund policy, track my order)")

# Process Query
if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask(query)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})