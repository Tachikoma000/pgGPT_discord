from experiments.ai_chat_system import AIChatSystem

def main():
    # Initialize the AI chat system
    chat_system = AIChatSystem()
    
    while True:
        # Take input from the user
        user_input = input("Enter your query (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            break

        # Get response from the AI chat system
        response = chat_system.chat(user_input)
        print("AI Response:", response)

if __name__ == "__main__":
    main()
