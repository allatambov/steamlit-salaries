import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

# prepare data

dat = pd.read_csv("Salaries.csv")
dat.rename(columns = {"yrs.since.phd" : "phd", 
            "yrs.service" : "service"}, inplace = True)

# prepare the list of variables,
# without Untitled, the 1st one

options = list(dat.columns[1:]) 

# add title and a dropdown menu to select a column

st.title("Salaries in US universities")
selected = st.sidebar.selectbox("Choose a variable", options)

# add a field for the color of the graph (e.g. #346eeb)

fill_color = st.sidebar.text_input("Enter a color:", 
                           value = "#346eeb")

# create a table with descriptive statistics

selected_table = dat[selected].describe()

# if column is not numeric (type object)
# create a table with frequencies
# and plot a bar chart -> plot in ax, save as fig
# otherwise, plot a histogram -> plot in ax, save as fig

if dat[selected].dtype == "object":
    freqs = dat[selected].value_counts()
    fig, ax = plt.subplots()
    ax.bar(freqs.index, freqs.values, color = fill_color)
    
else:
    fig, ax = plt.subplots()
    ax.hist(dat[selected], color = fill_color, edgecolor = "white")

    
# add two tabs, 1st with table of descriptives,     
# 2nd with the graph

col1, col2 = st.tabs(["Statistics", "Visualization"])

with tab1:
    st.table(selected_table)

with tab2:    
    st.pyplot(fig)