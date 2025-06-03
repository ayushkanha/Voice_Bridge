import streamlit as st

def about_page():
    st.title("📌 About VoiceBridge")
    
    st.markdown("""
    **VoiceBridge** is a smart and user-friendly app designed to help you **translate speech or text across multiple languages** and analyze the **emotional tone** of the message.

    ---
    ### 🚀 What Can VoiceBridge Do?
    - 🗣️ Convert **voice to text** using speech recognition
    - 🌐 Translate text or speech into other languages using Deep Translator (Google Translate)
    - 💬 Detect the **sentiment or tone** of the message using local and cloud-based models

    ---
    ### 🔧 Technologies Used
    - **Speech Recognition**: `speech_recognition` library for converting audio to text
    - **Translation**: `deep_translator` with Google Translate for accurate text translation
    - **Sentiment Analysis**:
        - For text: Hugging Face Transformer models (e.g., BERT-based sentiment classification)
        - For voice: A local emotion detection model to analyze audio tone

    ---
    ### 🎯 Why VoiceBridge?
    VoiceBridge is created to:
    - Break language barriers in real-time
    - Help understand the emotional intent of communication
    - Enable better interaction in global, multicultural environments
    - Support accessibility and learning

    ---
    ### 👨‍💻 Developer Info
    **Developed by**: Ayush & Manav
    🔗 [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

    ---
    🌐 VoiceBridge is open for collaboration and feedback. Let's bridge the gap between voices and languages! 💬🌍
    """)

