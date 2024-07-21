import datetime
from flask import Flask, request, jsonify, render_template
import spacy
app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')


def get_bot_response(user_input):
    doc = nlp(user_input.lower())

    responses = {
        "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
        "farewell": ["bye", "goodbye", "see you", "later"],
        "name": ["what is your name", "who are you", "your name"],
        "help": ["help", "assist", "support"],
        "how_are_you": ["how are you", "what's up", "how do you do"],
        "capabilities": ["what can you do", "features", "capabilities"],
        "weather": ["what's the weather", "weather", "forecast"],
        "time": ["what time is it", "current time", "time"],
        "joke": ["tell me a joke", "joke", "make me laugh"],
        "thank_you": ["thank you", "thanks", "appreciate it"],
        "feedback": ["feedback", "suggestion", "improve"],
        "faq": ["faq", "frequently asked questions", "common questions"],
        "contact": ["contact", "how to reach you", "contact information"],
        "task": ["help with tasks", "assist with tasks", "task assistance"],
        "ai_concepts": ["ai concepts", "what is AI", "artificial intelligence"],
        "machine_learning": ["machine learning", "what is machine learning", "ML"],
        "deep_learning": ["deep learning", "what is deep learning", "DL"],
        "nlp": ["natural language processing", "NLP", "what is NLP"],
        "data_science": ["data science", "what is data science", "DS"],
        "creator": ["who created you", "who made you", "who is your creator"]
    }

    for key, phrases in responses.items():
        if any(phrase in user_input for phrase in phrases):
            if key == "greeting":
                return "Hello! How can I assist you today?"
            elif key == "farewell":
                return "Goodbye! Have a great day!"
            elif key == "name":
                return "I'm a friendly chatbot here to help you with your queries."
            elif key == "help":
                return "I'm here to help! You can ask me about my features or how I can assist you."
            elif key == "how_are_you":
                return "I'm just a bunch of code, but I'm doing well! How can I help you today?"
            elif key == "capabilities":
                return "I can assist with general queries, provide information, and make your day better!"
            elif key == "weather":
                return "I can't check the weather right now, but you can use a weather app for that!"
            elif key == "time":
                now = datetime.now().strftime("%H:%M:%S")
                return f"The current time is {now}."
            elif key == "joke":
                return "Why don’t scientists trust atoms? Because they make up everything!"
            elif key == "thank_you":
                return "You're welcome! If you have any more questions, feel free to ask."
            elif key == "feedback":
                return "I appreciate your feedback! Let me know how I can improve."
            elif key == "faq":
                return "You can ask me about general topics, tasks, or how to contact support. Let me know what you need help with!"
            elif key == "contact":
                return "You can reach us at support@example.com or call us at (123) 456-7890."
            elif key == "task":
                return "I can assist with various tasks such as scheduling, reminders, and more. Let me know what you need help with!"
            elif key == "ai_concepts":
                return "Artificial Intelligence (AI) involves creating machines that can perform tasks that typically require human intelligence. It includes learning, reasoning, problem-solving, and understanding natural language."
            elif key == "machine_learning":
                return "Machine Learning (ML) is a subset of AI where algorithms learn from data to make predictions or decisions. It's used in applications like recommendation systems and autonomous vehicles."
            elif key == "deep_learning":
                return "Deep Learning (DL) is a type of ML that uses neural networks with many layers to analyze various factors of data. It's particularly effective in tasks like image and speech recognition."
            elif key == "nlp":
                return "Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. It is used in applications like chatbots, language translation, and sentiment analysis."
            elif key == "data_science":
                return "Data Science involves analyzing and interpreting complex data to help organizations make decisions. It combines statistical analysis, machine learning, and data visualization."
            elif key == "creator":
                return "I was created by Patan Yaseen for a Codesoft internship."
    
    return "I'm sorry, I didn't understand that. Can you please rephrase your question?"



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_bot_response(user_input)
    return jsonify({'response': response})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
