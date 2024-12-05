
import streamlit as st
from groq import Groq


if 'x' not in st.session_state:
    st.session_state.x=""

def genrate():
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Tell me a joke",
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

st.session_state.x=genrate()

st.write(st.session_state.x)

if st.button("Next"):
    st.session_state.x=genrate()