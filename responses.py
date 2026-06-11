RESPONSES = {

    "hello": "Hello! I'm WEbot. How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! Great to see you.",
    "good morning": "Good morning! Have a productive day.",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! Hope you're doing well.",

    "who are you": "I'm WEbot, a rule-based AI chatbot.",
    "what are you": "I'm a chatbot designed to answer common questions.",
    "what is your name": "My name is WEbot.",
    "who made you": "I was created by a developer using Python and rule-based logic.",
    "are you human": "No, I'm an AI chatbot.",

    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that learns from data.",
    "what is deep learning": "Deep Learning uses neural networks with multiple layers.",
    "what is generative ai": "Generative AI creates new content such as text, images, and code.",
    "what is a chatbot": "A chatbot is software that can communicate with users.",

    "what is python": "Python is a popular programming language known for its simplicity.",
    "what is java": "Java is an object-oriented programming language.",
    "what is html": "HTML is used to structure web pages.",
    "what is css": "CSS is used to style web pages.",
    "what is javascript": "JavaScript adds interactivity to websites.",
    "what is github": "GitHub is a platform for hosting and managing code repositories.",

    "what is internship": "An internship provides practical work experience for students.",
    "how to prepare for interview": "Practice technical skills, communication, and problem-solving.",
    "how to improve coding": "Practice regularly and work on projects.",
    "how to learn ai": "Start with Python, mathematics, machine learning, and projects.",

    "what is india": "India is a country in South Asia.",
    "what is the capital of india": "New Delhi is the capital of India.",
    "largest planet": "Jupiter is the largest planet in our solar system.",
    "fastest animal": "The cheetah is the fastest land animal.",

    "what is fever": "Fever is a temporary rise in body temperature, often due to infection.",
    "what is headache": "A headache is pain or discomfort in the head region.",
    "what is cold": "The common cold is a viral infection affecting the nose and throat.",
    "how much water should i drink": "Many adults aim for around 2 to 3 liters of water daily, but needs vary.",
    "what is bmi": "BMI stands for Body Mass Index and estimates body weight relative to height.",
    "how to stay healthy": "Eat balanced meals, exercise regularly, sleep well, and stay hydrated.",
    "what is cough": "A cough is a reflex action that helps clear the airways.",

    "motivate me": "Success comes from consistent effort. Keep learning and improving!",
    "i am tired": "Take a short break and return with a fresh mind.",
    "give me motivation": "Every expert was once a beginner. Keep going.",

    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "tell me something interesting": "The human brain contains around 86 billion neurons.",
    "do you like pizza": "I can't eat pizza, but many people love it!",

    "what is 2+2": "2 + 2 = 4",
    "what is 5x5": "5 × 5 = 25",
    "what is 10 divided by 2": "10 ÷ 2 = 5",

    "what day is today": "I cannot access the current date in this rule-based version.",
    "what time is it": "I cannot access real-time information in this version.",

    "help": "You can ask me about AI, programming, health basics, students, and general knowledge.",
    "what can you do": "I can answer common questions and hold simple conversations.",

    "bye": "Goodbye! Keep building amazing projects.",
    "goodbye": "See you later!",
    "exit": "Exiting chatbot... Goodbye!",
    "quit": "Exiting chatbot... Goodbye!",

    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
}
import random

DEFAULT_RESPONSES = [
    "I'm not sure I understand. Try asking in a different way.",
    "Sorry, I don't have information about that yet.",
    "That's an interesting question! I haven't learned that yet.",
    "I couldn't find a matching response. Try 'help' to see what I can do.",
    "I'm still learning. Could you rephrase your question?",
    "I don't know the answer to that right now.",
    "Hmm... that's outside my current knowledge base.",
    "Can you ask that differently? I may understand better.",
    "I can currently answer questions about AI, programming, health basics, and general knowledge.",
    "Sorry, I don't recognize that question yet."
]

def get_default_response():
    return random.choice(DEFAULT_RESPONSES)