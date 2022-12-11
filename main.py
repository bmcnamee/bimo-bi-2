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

st.markdown("# Executive Summary Dashboard")

tabs_list = [
    "KPI Summary",
    "Domain Scores",
    "Patient Satisfaction",
    "Patient Rounding",
    "Service Recovery",
]
t1, t2, t3, t4, t5 = st.tabs(tabs_list)

with t1:
    r1c1, r1c2, r1c3, r1c4 = st.columns(4)
    r1c1.metric(label="Overall Census", value="92.0%", help="Percent of beds currently filled.")
    r1c2.metric(label="ER Waiting", value="8 patients", help="Number of patients currently waiting in the ER.")
    r1c3.metric(label="Admitted Today", value="3 patients", help="Number of patients admitted so far today.")
    r1c4.metric(label="Discharged Today", value="3 patients", help="Number of patients discharged so far today.")

    r2c1, r2c2, r2c3, r2c4 = st.columns(4)
    r2c1.metric(label="Overall Patient Satisfaction", value="77.6%", delta="1.2 MoM"
                , help="Current month to date overall patient satisfaction percent \
                        and absolute difference from prior month.")
    r2c2.metric(label="Likelihood to Recommend", value="77.6%", delta="-0.6 MoM"
                , help="Current month to date likelihood to recommend percent \
                        and absolute difference from prior month.")
    r2c3.metric(label="Length of Stay", value="4.2 days", delta="1.2 MoM"
                , help="Current month to date average length of patient stay in days \
                        and absolute difference from prior month.")
    r2c4.metric(label="30 Day Re-admit Rate", value="2.2%", delta="1.0 MoM"
                , help="Current month to date 30 day patient re-admittance rate \
                        and absolute difference from prior month.")

with t2:
    st.markdown(f"{tabs_list[1]}")

with t3:
    st.markdown(f"{tabs_list[2]}")

with t4:
    st.markdown(f"{tabs_list[3]}")

with t5:
    st.markdown(f"{tabs_list[4]}")
