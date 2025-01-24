import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import seaborn as sns

#Load the Titanic dataset
titanic = sns.load_dataset("Titanic")

st.title("Titanic Dataset Dashboard")
st.sidebar.header("Filter options")


st.dataframe(titanic)
