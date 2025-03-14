from dotenv import load_dotenv

load_dotenv()
from typing import Set

import streamlit as st
from streamlit_chat import message

from backend.core import run_llm

st.set_page_config(
    page_title="Your App Title",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Add these imports
from PIL import Image
import requests
from io import BytesIO

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"]= []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "Sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i + 1}. {source}\n"
    return sources_string


# Add this function to get a profile picture
def get_profile_picture(email):
    # This uses Gravatar to get a profile picture based on email
    # You can replace this with a different service or use a default image
    gravatar_url = f"https://www.gravatar.com/avatar/{hash(email)}?d=identicon&s=200"
    response = requests.get(gravatar_url)
    img = Image.open(BytesIO(response.content))
    return img

# Custom CSS for dark theme and modern look
st.markdown(
    """
<style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stTextInput > div > div > input {
        background-color: #2D2D2D;
        color: #FFFFFF;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: #FFFFFF;
    }
    .stSidebar {
        background-color: #252526;
    }
    .stMessage {
        background-color: #2D2D2D;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Set page config at the very beginning


# Sidebar user information
with st.sidebar:
    st.title("User Profile")

    # You can replace these with actual user data
    user_name = "Le Trung Tuyen"
    user_email = "letrungtuyen2002@gmail.com"

    profile_pic = get_profile_picture(user_email)
    st.image(profile_pic, width=150)
    st.write(f"**Name:** {user_name}")
    st.write(f"**Email:** {user_email}")

st.header("LangChain🦜🔗 Udemy Course- Helper Bot")

# Initialize session state
if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []

# Create two columns for a more modern layout
col1, col2 = st.columns([2, 1])

with col1:
    prompt = st.text_input("Prompt", placeholder="Enter your message here...")

with col2:
    st.write("")  # Thêm khoảng trống để căn giữa nút
    if st.button("Submit", key="submit"):
        prompt = prompt or "Hello"  # Default message if input is empty

if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_llm(query=prompt)
        sources = set(
            [doc.metadata["source"].replace("\\", "/") for doc in generated_response["source_documents"]]
        )

        formatted_response = (
            f"{generated_response['result']} \n\n {create_sources_string(sources)}"
        )

        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(formatted_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(st.session_state["chat_answers_history"], st.session_state["user_prompt_history"]):
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(generated_response)

# Add a footer
st.markdown("---")
st.markdown("Powered by LangChain and Streamlit")