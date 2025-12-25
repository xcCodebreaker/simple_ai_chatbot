import os
from openai import OpenAI
import local_chatbot


def run_local_chatbot():
    """Run the local pattern-matching chatbot"""
    print("\n[*] Local Chatbot Active! (Type 'quit' to exit)")
    print("-----------------------------------------------------")
    
    intents = local_chatbot.load_intents()
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        response = local_chatbot.get_response(user_input, intents)
        print(f"Bot: {response}")


def run_ai_chatbot():
    """Run the advanced AI chatbot using OpenRouter"""
    MY_OPENROUTER_KEY = "API Key"

    api_key = MY_OPENROUTER_KEY
    if api_key == "PASTE_YOUR_KEY_HERE":
        api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key or api_key == "PASTE_YOUR_KEY_HERE":
        print(" ERROR: Missing API Key!")
        print("Please open 'chatbot.py' and paste your OpenRouter API Key in the 'MY_OPENROUTER_KEY' variable.")
        return

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    print("\n[*] Advanced AI Chatbot Active! (Type 'quit' to exit)")
    print("-----------------------------------------------------")

    messages = []

    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            completion = client.chat.completions.create(
                model="openai/gpt-3.5-turbo", 
                messages=messages
            )

            ai_response = completion.choices[0].message.content
            print(f"AI: {ai_response}")
            messages.append({"role": "assistant", "content": ai_response})

        except Exception as e:
            print(f" An error occurred: {e}")


def main():
    """Main function to select chatbot mode"""
    print("\n" + "="*50)
    print("  CHATBOT SELECTION MENU")
    print("="*50)
    print("\nChoose your chatbot mode:")
    print("  1. Local Chatbot - PC Building Assistant")
    print("  2. Advanced AI Chatbot")
    print("\n" + "="*50)
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            run_local_chatbot()
            break
        elif choice == "2":
            run_ai_chatbot()
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()
