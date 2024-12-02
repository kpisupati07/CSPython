import json
import keys
import requests

# EXAMPLE
# Uses the openai chat-completions api to make a chatbot that speaks like
# a pirate. This makes the post request directly.
#
# https://platform.openai.com/docs/guides/gpt/chat-completions-api

API_KEY = 'add your key here'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}',
}
URL = 'https://api.openai.com/v1/chat/completions'

    
def chat_with_bot(prompt, conversation_history):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Get a response from the model
    request = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history,
    }

    response = requests.post(URL, headers=HEADERS, data=json.dumps(request)).json()

    # Extract the assistant's message and add it to the conversation history
    ai_answer = response['choices'][0]['message']['content']
    conversation_history.append({"role": "assistant", "content": ai_answer})

    return ai_answer

def main():
    # Start the conversation with a system message
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant. You speak like a pirate."},
    ]

    prompt = None
    while prompt != "done":
        # Get input from the user
        prompt = input("You: ")

        # Get the AI's response and print it
        ai_text = chat_with_bot(prompt, conversation_history)
        print("\nAI: ", ai_text, "\n")

if __name__ == "__main__":
    main()
