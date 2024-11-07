import json
import requests

# Load conversation data from JSON file
def load_conversation_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Generate a response using Google Gemini API
def generate_response(prompt):
    GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    API_KEY = 'API_KEY_HERE'  # Replace with your actual API key

    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    
    try:
        response = requests.post(f"{GEMINI_API_URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        json_response = response.json()
    
        
        # Access the nested response contents safely
        if 'candidates' in json_response and 'content' in json_response['candidates'][0]:
            return json_response['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Unexpected response structure from API."
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return "Sorry, I couldn't generate a response."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't generate a response."

# Function to handle user interaction
def chat_with_user(client_id, conversation_data):
    if client_id not in conversation_data:
        print("No conversation history found for this client.")
        return
    
    history = conversation_data[client_id]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Append user's message to history
        history.append({"human": f"(client_id: {client_id}): {user_input}"})
        
        # Create a prompt from the conversation history
        prompt = "\n".join([f"{msg.get('human', '')} {msg.get('ai', '')}" for msg in history])
        
        # Generate AI response
        ai_response = generate_response(prompt)
        
        # Append AI's response to history
        history.append({"ai": ai_response})
        
        print(f"AI: {ai_response}")

# Main function to run the chatbot
if __name__ == "__main__":
    conversation_data = load_conversation_data('conversation_data.json')  # Path to your JSON file
    client_id = "-4567175683"  # Example client ID from your data
    chat_with_user(client_id, conversation_data)
