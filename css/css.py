import streamlit as st


def define_css():
    st.markdown(
        """
        <style>
        .centered-img {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )