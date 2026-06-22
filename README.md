# Rule-Based CLI Chatbot 🤖

A conversational command-line interface (CLI) application built in Python. This project demonstrates foundational Natural Language Processing (NLP) concepts using rule-based keyword matching, dynamic system interactions, and continuous state management. 

### Application Output
![Chatbot Output](Rule%20Based%20ChatBot.png)

## 🚀 Features

* **Dynamic Time-Aware Greeting:** Utilizes Python's `datetime` module to fetch the current system hour and deliver context-aware greetings.
* **Rule-Based NLP Engine:** Implements a dictionary-based routing system to scan user input for specific keywords and return mapped responses.
* **Input Normalization:** Sanitizes user input by converting strings to lowercase, preventing case-sensitivity errors.
* **Continuous Conversation Loop:** Uses an infinite `while` loop to maintain application state until the explicit `break` condition ("bye") is triggered.

## 🛠️ Technologies & Concepts Used

* **Language:** Python 3.x
* **Modules:** `datetime`, `time`
* **Core Concepts:** * Dictionary Mapping (Key-Value pairs)
  * String Manipulation & Sanitization
  * Conditional Logic (If/Elif/Else)

## 💻 How to Run the Application

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/rule-based-cli-chatbot.git](https://github.com/yourusername/rule-based-cli-chatbot.git)
