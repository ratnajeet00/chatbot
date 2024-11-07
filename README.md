# Chatbot Using Google Gemini API

This chatbot project enables interaction with a conversational AI powered by the Google Gemini API. The chatbot loads and maintains conversation history for specific users, responds to user input by generating prompts, and displays responses in real-time. It is designed as a command-line application that uses JSON files to store conversation history and integrates with the Google Gemini API to generate responses based on user prompts.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)


## Features

- Load conversation history from a JSON file.
- Generate responses to user prompts using Google Gemini API.
- Maintain history for each client ID.
- Simple CLI-based interface.
- Real-time response generation with error handling.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```
Navigate to the project directory:
```
cd your-repo-name
```
Install dependencies:
Make sure you have Python installed (Python 3.x).
Install required packages:
```
pip install requests
```

Usage
Prepare your API key:
Replace API_KEY_HERE in the code with your actual Google Gemini API key.

Prepare a conversation data file:
Create a JSON file named conversation_data.json in the project directory with conversation history, structured like so:
```
{
    "-4567175683": [
        {"human": "Hello!"},
        {"ai": "Hi there! How can I help you today?"}
    ]
}
Run the chatbot:

```
```
python chatbot.py
```

Interact with the chatbot:

Type your input and press Enter.
Type exit to end the session.

# Configuration:

API Key: Add your API key to the API_KEY variable in generate_response().
Client ID: Set the client_id variable in the main function to manage conversations for a specific user.
Conversation History: The chatbot stores each conversation per client ID. Ensure the JSON file has the correct structure to avoid errors.
Code Structure
load_conversation_data(file_path): Loads conversation data from a JSON file.
generate_response(prompt): Sends a request to Google Gemini API to generate a response based on the given prompt.
chat_with_user(client_id, conversation_data): Main function to handle user interaction and response generation.
__main__: Loads conversation data and starts the chat interface.
Error Handling
HTTP Errors: Captured and reported for easier debugging.
Unexpected API Response Structure: Catches and notifies when the API response structure is unexpected.
