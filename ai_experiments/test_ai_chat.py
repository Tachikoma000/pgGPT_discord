from pgai_v3 import AIChatSystemV2  

if __name__ == "__main__":
    chat_system = AIChatSystemV2()
    print(chat_system.chroma_collection.count())

    
    # Test querying the system
    user_input = input("Enter your query: ")
    response = chat_system.chat(user_input)
    print("AI Response:", response)
