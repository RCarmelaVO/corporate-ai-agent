from chatbot.retriever import load_retriever


retriever = load_retriever()


question = "How many vacation days do employees receive?"


results = retriever.invoke(question)


for doc in results:
    print("----------------")
    print(doc.page_content)