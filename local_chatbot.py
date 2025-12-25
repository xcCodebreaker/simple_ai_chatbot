import json
import random
import re


def load_intents():
    """Load intents from intents.json file"""
    with open('intents.json', 'r') as file:
        data = json.load(file)
    return data['intents']


def get_response(user_input, intents):
    # Match user input against patterns and return a response.
    user_input_lower = user_input.lower()
    
    # Extract budget from user input
    budget_match = re.search(r'\$?(\d{3,4})', user_input)
    extracted_budget = int(budget_match.group(1)) if budget_match else None
    
    # If budget is found
    if extracted_budget:
        # Determine if it's gaming, workstation, or streaming based on keywords
        is_gaming = any(word in user_input_lower for word in ['gaming', 'game', 'play', 'fps'])
        is_workstation = any(word in user_input_lower for word in ['workstation', 'work', 'editing', 'rendering', '3d', 'programming', 'coding'])
        is_streaming = any(word in user_input_lower for word in ['streaming', 'stream', 'twitch', 'youtube'])
        
        # Match budget to appropriate tier
        if is_streaming and 1400 <= extracted_budget <= 2200:
            tag = "streaming_build"
        elif is_workstation:
            if extracted_budget < 800:
                tag = "workstation_entry"
            elif extracted_budget < 1700:
                tag = "workstation_mid"
            else:
                tag = "workstation_high"
        elif is_gaming or not (is_workstation or is_streaming):  # Default to gaming
            if extracted_budget < 800:
                tag = "budget_entry_gaming"
            elif extracted_budget < 1400:
                tag = "budget_mid_gaming"
            elif extracted_budget < 2000:
                tag = "budget_high_gaming"
            else:
                tag = "budget_enthusiast_gaming"
        
        # Find and return response for matched tag
        for intent in intents:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    
    # Standard pattern matching
    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input_lower or user_input_lower in pattern.lower():
                return random.choice(intent['responses'])
    
    # Default response if no match found
    return "I'm not sure I understand. Can you rephrase that? Try asking about a specific budget (e.g., 'gaming pc for $1000') or component advice!"


def chat():
    """Main function to run the local chatbot"""
    print("\n*** Local PC Building Chatbot Active! (Type 'quit' to exit) ***")
    print("-----------------------------------------------------")
    
    intents = load_intents()
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! Happy building!")
            break
        
        response = get_response(user_input, intents)
        print(f"Bot: {response}")


if __name__ == "__main__":
    chat()
