import streamlit as st  # loaded by streamlit cloud


def local_css(file_name: str) -> None:
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url: str) -> None:
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name: str) -> None:
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
icon("search")

selected = st.text_input("", "Search...")
button_clicked = st.button("OK")
st.markdown(f"# BIMO BI 2")
st.metric(label="Overall Census", value="92%", delta="1.2")
st.metric(label="Metric 2", value="92%", delta="1.2")
