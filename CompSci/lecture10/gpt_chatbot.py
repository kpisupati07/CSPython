import openai   # need to run the command "pip install openai" in the terminal first
import keys

# EXAMPLE
# Uses the openai chat-completions api to make a chatbot that speaks like
# a pirate. This version uses the openai module to make the post() request.
# See:
# https://platform.openai.com/docs/guides/gpt/chat-completions-api

openai.api_key = 'add your key here'

def chat_with_bot(prompt, conversation_history):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Get a response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
    )

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
        print("AI: ", ai_text)

if __name__ == "__main__":
    main()
