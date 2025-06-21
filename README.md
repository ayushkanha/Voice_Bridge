 # 🎙️ VoiceBridge - Multilingual Voice & Text Translator with Sentiment Analysis

VoiceBridge is a Streamlit-based web application that allows users to **translate speech or text** between multiple languages and **analyze the emotional tone** of the message using sentiment analysis. The app features a clean and intuitive interface, making multilingual communication and tone detection easier than ever.

---

## 🚀 Features

- 🗣️ **Speech to Text**: Converts audio input into text using the `speech_recognition` library.
- 🌐 **Multilingual Translation**: Translates both text and audio using `deep_translator`'s Google Translate support.
- 💬 **Sentiment Analysis**:
  - For text: Uses Hugging Face Transformers to analyze sentiment.
  - For voice: Utilizes a local audio emotion detection model.
- 🧑‍💻 **User-Friendly Interface**: Built with Streamlit for seamless and interactive user experience.

---

## 🧠 Tech Stack

| Functionality        | Technology |
|----------------------|------------|
| Frontend UI          | Streamlit  |
| Speech Recognition   | `speech_recognition` |
| Translation          | `deep_translator` (Google Translate) |
| Text Sentiment       | Hugging Face Transformers |
| Voice Sentiment      | Local Emotion Detection Model |

---

## 🔧 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/ayushkanha/Voice_Bridge.git
   cd voicebridge
   ```

2. **Install dependencies**  
   It's recommended to use a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**  
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
voicebridge/
│
├── app.py                # Main Streamlit app
├── about.py              # About page
├── voice.py         # Translation logic
├── tone.py     # Text sentiment analysis
├── css.py    # Custome style for streamlit compomponets by css injection
├── requirements.txt      # List of dependencies
└── README.md             # This file
```

---

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/a9586a9c-4f80-4333-8467-102297e00cf8)

![image](https://github.com/user-attachments/assets/9661487d-b139-455e-87ff-f5ac4c2eeae2)


---

## 👨‍💻 Author

**Ayush Sahu**  
🔗 [LinkedIn](linkedin.com/in/ayush-kumar-sahu-299b8b23b)  


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐️ Support

If you like this project, please consider giving it a ⭐️ on GitHub!
