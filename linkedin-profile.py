import streamlit as st
from linkedin_api import Linkedin

st.session_state["profile_data"] = ""
username = st.secrets.get("LINKEDIN_USERNAME")
password = st.secrets.get("LINKEDIN_PASSWORD")


def get_profile_date(message: str):
    api = Linkedin(username, password)
    profile_data = api.get_profile(message)
    st.session_state["profile_data"] = profile_data


st.title("LinkedIn profile data")
st.divider()

with st.container():
    st.session_state["text"] = st.text_area(label="Username",
                                            placeholder="Enter linkedin username, e.g 'hridyansh-sahu'")
    st.markdown("")
    st.markdown("")
    if st.button(on_click=get_profile_date(st.session_state["text"]), label="Get profile data"):
        st.markdown("")
        st.markdown("")
        st.success(st.session_state["profile_data"])
    else:
        st.markdown("Click the button to get profile data")
