import numpy as np
import streamlit as st
import pandas as pd
# Plotting for my solution to homework 5 part c

def func(a, t):
    y = a*np.exp((-2/3)*t) + ((2*a + 3)/3) * t * np.exp((-2/3)*t)
    return y
t = np.linspace(0,8)
a = st.sidebar.slider(
    'Select values of a', 
     0, 100
    )
df = pd.DataFrame(
    {
        'input': t ,
        'output': func(a,t)
    }
)
print(df.head())
st.line_chart(df,x='input' ,y='output', x_label='t', y_label='y(t)')

