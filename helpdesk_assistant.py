import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load your .env file
load_dotenv()
client = OpenAI()

# Streamlit UI
st.title("Liam and Lucas's  IT Support Assistant")

ticket = st.text_area("Paste the helpdesk ticket here:")

if st.button("Generate Response"):
    if ticket.strip():
        with st.spinner("Generating response..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an IT support specialist."},
                    {"role": "user", "content": ticket}
                ]
            )
            reply = response.choices[0].message.content
        st.text_area("Suggested Reply", value=reply, height=200)
    else:
        st.warning("Please enter a ticket.")
