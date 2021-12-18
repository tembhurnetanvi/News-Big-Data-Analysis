import streamlit as st
import pandas as pd

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">CNN</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_us.py" target="_blank">US</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_wor.py" target="_blank">World</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_pol.py" target="_blank">Politics</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_opi.py" target="_blank">Opinion</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_hea.py" target="_blank">Health</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_eco.py" target="_blank">Economy</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/tanvi/streamlit/page_tec.py" target="_blank">Tech</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/tembhurnetanvi/news-big-data-analysis/main/streamlit/page_dev_login.py" target="_blank">Dev_LogIn</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.subheader("Welcome!")
st.markdown("____")
st.header("News Analysis Application 👀")
st.markdown("____")
st.subheader("This application helps to empower mind with day-to-day news.")
st.write("This project for DAMG-7245 NEU guided by Prof. Srikanth KrishnaMurthy, made by Kartik Kumar and Tanvi Tembhurne")
st.markdown("____")