import streamlit as st
from services.auth.login import render_login_wall

st.set_page_config(page_title="🏋️ AI Real-Time Workout Coach")

def main():
    st.set_page_config(
        page_icon="🏋️",
        page_title="AI Real-Time Workout Trainer",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    if not render_login_wall():
        return

    st.write("Hello!!")

if __name__ == "__main__":
    main()
