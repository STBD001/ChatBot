import spacy
import en_core_web_sm
import tkinter as tk
from tkinter import scrolledtext

nlp = en_core_web_sm.load()

def generate_response(user_input):
    doc = nlp(user_input)
    if any(token.lemma_ == "hello" for token in doc):
        return "Hello! How can I help you today?"
    elif any(token.lemma_ == "bye" for token in doc):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

def send_message():
    user_input = user_entry.get()
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    response = generate_response(user_input)
    chat_history.insert(tk.END, "Bot: " + response + "\n")
    user_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chatbot")

chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD)
chat_history.pack(padx=10, pady=10)

user_entry = tk.Entry(window, width=50)
user_entry.pack(padx=10, pady=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

window.mainloop()
