import streamlit as st

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.title("🏋️ AI Real-Time Workout Coach")
    st.markdown("### Welcome!, Please Enter a username to start...")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique): ", placeholder="unique name e.g.: (Suryam@700)")
        response = st.form_submit_button("Start Session", icon=":material/home:", width="stretch")

    if response:
        if not username:
            st.error("EmptyError: username shouldn't be empty")
            return False

        st.session_state["username"] = username
        st.session_state["user_id"] = "1"
        st.rerun()

    return False