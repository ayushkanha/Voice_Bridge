import streamlit as st 
from deep_translator import GoogleTranslator
from gtts import gTTS
from pydub import AudioSegment
import tempfile
import os
import speech_recognition as sr
from transformers import pipeline as pl
from streamlit_option_menu import option_menu
import css
from st_audiorec import st_audiorec
import streamlit.components.v1 as components
from voice import transcribe,text_to_speech
from tone import tone
import about

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
st.session_state.translate=False

st.set_page_config(page_title="VoiceBridge",layout="wide",page_icon="fevicon.png")
Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az',
             'basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca',
             'cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw',
             'corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo',
             'estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka',
             'german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw',
             'hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id',
             'irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km',
             'korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt',
             'luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi',
             'marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','odia':'or','pashto':'ps',
             'persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm',
             'scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk',
             'slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg',
             'tamil':'ta','telugu':'te','thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur','uyghur':'ug',
             'uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}



st.markdown(
    """
    <style>

    [alt="Logo"] {
        height: 90px;
        width: auto;  
        
    }
    .block-container {
            padding-top: 0rem;
        }
    header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns([1, 6])
with col1:
    st.markdown("""
    <style>
    @media only screen and (max-width: 959px) {
        img {
            max-width: 100px;
            height: auto;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    st.logo("logo.png")
with col2:

    css.nev()
    st.markdown('<div class="custom-navbar">', unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Translate", "Tone", "About"],
        icons=["bi-people-fill", "bi-soundwave", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#0E1117"},
            "icon": {"color": "white"},
            "nav-link": {
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#204044",
            },
            "nav-link-selected": {"background-color": "#1f6f78"},
        }
    )
    st.markdown('</div>', unsafe_allow_html=True)
with st.container():
    st.markdown("""
    <style>
    .custom-container {
        margin-top: 70px;
    }

    @media (max-width: 767px) {
        .custom-container {
            margin-top: 0px;
        }
    }
    </style>
    <style>
    .middle {
        margin-top: 120px;
    }

    @media (max-width: 767px) {
        .middle {
            margin-top: 0px;
        }
    }
    </style>
""", unsafe_allow_html=True)
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)

    left_col, st.session_state.mid_col, st.session_state.right_col = st.columns([3, 2, 3])
    # left user input
    # ------------------------------------------------------------------------------------------------------------------------------------------------
    if (selected == "Translate" or selected == "Tone"):
        with left_col:
            with st.popover("", icon=":material/tune:"):
                inp = st.selectbox('Choose Input Format', ("Text", "Audio_file", "MIC"))
                st.session_state.inp = inp
            with st.form("my_form"):
                st.markdown("### 🎙️ Input")
                if st.session_state.inp == "Text":
                    st.session_state.text = st.text_area("Enter Text:", help="Type your text here...")
                elif st.session_state.inp == "MIC":
                    st.session_state.uploaded_file = st.audio_input("Record a Voice Message")
                else:
                    st.session_state.uploaded_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "m4a"])
                    
                submitted = st.form_submit_button("Submit")
    
        # ------------------------------------------------------------------------------------------------------------------------------------------------
    if selected == "Translate":            
        
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        # center button
        st.markdown('<div class="middle">', unsafe_allow_html=True)
        with st.session_state.mid_col:
            
            css.cicle_button()
            
            if st.button("Translate"):
                st.session_state.translate=False
                st.session_state.translate=True
        st.markdown('</div>', unsafe_allow_html=True)


        # ------------------------------------------------------------------------------------------------------------------------------------------------
        # Right Output
        with st.session_state.right_col:
            
            with st.popover("", icon=":material/tune:"):
                out_type = st.selectbox('Choose Input Format', ("Text", "Voice", "Both"))
                st.session_state.out_type = out_type
            with st.form("output"):
                st.markdown("### 🔉 Voice Output")
                option2 = st.selectbox('Select Output Language', list(Languages.keys()))
                value2 = Languages[option2]
                
                if st.session_state.translate:
                    c1,c2=st.columns(2)
                    if st.session_state.inp != "Text":
                        st.session_state.text = transcribe(st.session_state.uploaded_file)
                        
                    translated_text = GoogleTranslator(target=value2).translate(st.session_state.text)
                    
                    if st.session_state.out_type == "Text":
                        st.text_area("Translated Text:", translated_text, height=100)

                    elif st.session_state.out_type == "Voice":
                        if translated_text.strip():
                            audio_file = text_to_speech(translated_text, value2)
                        else:
                            c2.warning("Please enter text before converting.")
                        st.audio(audio_file, format='audio/mp3', autoplay=True)

                    else:
                        if translated_text.strip():
                            audio_file = text_to_speech(translated_text, value2)
                        else:
                            c2.warning("Please enter text before converting.")
                        with c1.popover("", icon=":material/library_books:"):
                            st.text_area("Translated Text:", translated_text, height=100)
                        c2.audio(audio_file, format='audio/mp3', autoplay=True)

                reset = st.form_submit_button("Reset ↻ ")
                if reset:
                    st.session_state.translate= False
        # Optional: Add some styling
        st.markdown("""
                    
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stButton>button {
            background-color: teal;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


    if selected == "Tone":
        tone()
    if selected == "About":
        about.about_page()
