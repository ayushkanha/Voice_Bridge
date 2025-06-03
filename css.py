import streamlit as st

def nev():
    st.markdown("""
        <style>
        /* Responsive icon and text size for option menu */
        @media only screen and (max-width: 768px) {
            .nav-link > span {
                font-size: 14px !important; /* reduce label size */
            }
            .nav-link > i {
                font-size: 16px !important; /* reduce icon size */
            }
        }

        @media only screen and (max-width: 480px) {
            .nav-link > span {
                font-size: 12px !important;
            }
            .nav-link > i {
                font-size: 14px !important;
            }
        }

        @media only screen and (min-width: 769px) {
            .nav-link > span {
                font-size: 18px !important;
            }
            .nav-link > i {
                font-size: 20px !important;
            }
        }

        .custom-navbar {
            margin-top: 0px;
        }

        @media only screen and (max-width: 768px) {
            .custom-navbar {
                margin-top: 50px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

def cicle_button():
    st.markdown("""
        <style>
        /* Target the button using Streamlit's internal structure */
        div[class^="stButton"] > button {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background-color: #008080;
            color: white;
            font-weight: bold;
            font-size: 16px;
            padding: 0;
            border: none;
            margin-left: 37%;
            margin-top: 70px;
        }
        
        @media (max-width: 640px) {
        div[class^="stButton"] > button {
            margin-top: 0px;
            margin-left:43%;
            
        }
        div[class^="stButton"] > button:hover {
            background-color: #009999;
            margin-left: 90px;
        }
        @media (max-width: 767px) {
        div[class^="stButton"] > button:hover{
            margin-top: 0px;
            margin-left:60px;   
        }
        @media (max-width: 640px) {
        div[class^="stButton"] > button:hover{
            margin-top: 0px;
            margin-left:43%;   
        }
        </style>
        """, unsafe_allow_html=True)