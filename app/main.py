import streamlit as st  # loaded by streamlit cloud

st.markdown(f"# BIMO BI 2")
st.metric(label=st.markdown("Overall Census<br>Metric description here"), value="92%", delta="1.2")
st.metric(label=st.markdown("# Metric 2"), value="92%", delta="1.2")