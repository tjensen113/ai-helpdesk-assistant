
import openai
import streamlit as st
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Helpdesk Ticket Responder")

ticket = st.text_area("Paste the helpdesk ticket here:")

if st.button("Generate Response"):
    if ticket.strip():
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an IT support specialist."},
                {"role": "user", "content": f"Here is a ticket: {ticket}"}
            ]
        )
        reply = response['choices'][0]['message']['content']
        st.text_area("Suggested Reply", value=reply, height=200)
    else:
        st.warning("Please enter a ticket.")
