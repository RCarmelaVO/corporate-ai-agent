from chatbot.assistant import create_assistant


assistant = create_assistant()


question = "How many vacation days do employees receive?"


answer = assistant(question)


print("\nANSWER:")
print(answer)