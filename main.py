import streamlit as st  # loaded by streamlit cloud


def local_css(file_name: str) -> None:
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# def remote_css(url: str) -> None:
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)
#
#
# def icon(icon_name: str) -> None:
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


local_css("style.css")

# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
# icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")

st.markdown(f"# Executive Summary Dashboard")


r1c1, r1c2, r1c3, r1c4 = st.columns(4)
r1c1.metric(label="Overall Census (% of Beds Filled)", value="92.0")
r1c2.metric(label="ER Waiting (Number of Patients)", value="8")
r1c3.metric(label="Admitted Today (Number of Patients)", value="3")
r1c4.metric(label="Discharged Today (Number of Patients)", value="3")


r2c1, r2c2, r2c3, r2c4 = st.columns(4)
r2c1.metric(label="Overall Patient Satisfaction (%)", value="77.6", delta="1.2")
r2c2.metric(label="Likelihood to Recommend (%)", value="77.6", delta="-0.6")
r2c3.metric(label="Average Length of Stay (Days)", value="4.2", delta="1.2")
r2c4.metric(label="30 Day Readmit Rate (%)", value="2.2", delta="1.0")
