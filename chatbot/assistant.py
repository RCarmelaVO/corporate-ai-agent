from langchain_ollama import OllamaLLM
from chatbot.retriever import load_retriever


def create_assistant():

    retriever = load_retriever()

    llm = OllamaLLM(
        model="qwen2.5:1.5b",
        temperature=0
    )


    def ask(question):

        documents = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content 
            for doc in documents
        )


        prompt = f"""
You are a corporate AI assistant.

Answer the user's question using ONLY the information
provided in the context.

If the answer is not found in the context,
say that the information is not available.

Context:
{context}


Question:
{question}


Answer:
"""


        response = llm.invoke(prompt)

        return response


    return ask