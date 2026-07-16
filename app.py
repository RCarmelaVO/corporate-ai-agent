import streamlit as st
from chatbot.assistant import create_assistant


st.set_page_config(
    page_title="Corporate AI Assistant",
    page_icon="🤖"
)


st.title("🤖 Corporate AI Assistant")

st.write(
    "Ask questions about company documents."
)


assistant = create_assistant()


question = st.text_input(
    "Your question:"
)


if st.button("Ask"):

    if question:

        with st.spinner("Searching documents..."):

            answer = assistant(question)


        st.subheader("Answer:")

        st.write(answer.content)

    else:

        st.warning("Please enter a question.")