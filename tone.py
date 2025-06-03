import streamlit as st 
from deep_translator import GoogleTranslator
from gtts import gTTS
from pydub import AudioSegment
import tempfile
import os
import speech_recognition as sr
import css
from voice import transcribe
from transformers import pipeline as pl
# from speechbrain.pretrained import EncoderClassifier

# @st.cache_resource
# def load_emotion_model():
#     return EncoderClassifier.from_hparams(
#         source="emotion_model_local",
#         savedir="tmp_emotion_model"
#     )

# emotion_model = load_emotion_model()

# def detect_emotion(uploaded_file):
#     # Save the uploaded file temporarily
#     # Use a more robust way to handle the temporary file lifecycle
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
#         tmp_file.write(uploaded_file.getvalue())
#         raw_path = tmp_file.name

#     try:
#         audio = AudioSegment.from_file(raw_path)
#         audio = audio.set_frame_rate(16000).set_channels(1)
#         audio.export(raw_path, format="wav")

#         # Predict emotion using the cleaned file
#         # Ensure the path is passed as a standard string
#         result = emotion_model.classify_file(str(raw_path))
#         predicted_emotion = result[3][0]
#         return predicted_emotion
#     finally:
#         # Clean up the temporary file
#         if os.path.exists(raw_path):
#             os.remove(raw_path)
def tone():           

    st.session_state.analyse=False
    st.markdown('<div class="middle">', unsafe_allow_html=True)
    with st.session_state.mid_col:
        
        css.cicle_button()
        
        if st.button("Translate"):
           st.session_state.analyse=True

    st.markdown('</div>', unsafe_allow_html=True)
    with st.session_state.right_col:
        if st.session_state.analyse:
            if st.session_state.inp != "Text":
                st.session_state.text = transcribe(st.session_state.uploaded_file)
            st.write(" ")
            st.write(" ")
            st.write(" ")
            with st.form("Tone_form"):
                if st.session_state.text !="" and st.session_state.text != " ":
                    pipe = pl("text-classification", model="tabularisai/multilingual-sentiment-analysis")
                    sentence = st.session_state.text
                    result = pipe(sentence)[0] 

                    sentiment = result['label']  
                    
                    if sentiment == "Very Negative":
                        st.error('This is Very Negative', icon="🚨")
                    elif sentiment == "Negative":
                        st.error('This is Negative', icon="😭")
                    elif sentiment == "Neutral":
                        st.warning('This is Neutral', icon="😐")
                    elif sentiment == "Positive":
                        st.success('This is Positive', icon="😊")
                    else: 
                        st.success('This is Very Positive', icon="😃")
                else:
                    st.warning("write something first")
                reset = st.form_submit_button("Reset ↻ ")
                if reset:
                    st.session_state.analyse= False






        # if st.session_state.inp != "Text":
        #     text = transcribe(st.session_state.uploaded_file)
        #     if text !="" and text != " ":
        #         emotion = detect_emotion(st.session_state.uploaded_file)
        #         st.write(f"🎭 Detected Emotion: `{emotion}`")