import streamlit as st

# Page Configuration
st.set_page_config(page_title="Simple AI Chatbot", page_icon="🤖")

# Title and Description
st.title("🤖 AI Chatbot")
st.write("Welcome! I'm your friendly chatbot. Ask me anything, and I'll do my best to help!")

# Predefined Responses (expandable)
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! What brings you here today?",
    "help": "Of course! I'm here to help. Please ask your question.",
    "services": "We offer a variety of services including cloud solutions, AI development, and more!",
    "pricing": "Our pricing is competitive and depends on your needs. Contact us for a custom quote!",
    "contact": "You can reach us at services@codealpha.tech or visit our website at www.codealpha.tech.",
    "bye": "Goodbye! Have a great day!",
}

# Chatbot Response Function
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I didn't quite catch that. Could you please rephrase?"

# Input Box
user_input = st.text_input("Type your message:")

# Display Response
if user_input:
    response = chatbot_response(user_input)
    st.text_area("Chatbot:", value=response, height=100)

# Footer
st.markdown("---")
st.caption("Developed for CodeAlpha Internship by Aryan Sharma")
