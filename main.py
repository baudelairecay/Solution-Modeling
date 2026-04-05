import numpy as np
import streamlit as st
import pandas as pd
# Plotting for my solution to homework 5 part c

def func(a, t):
    y = a*np.exp((-2/3)*t) + ((2*a + 3)/3) * t * np.exp((-2/3)*t) # Solution to the DE(found by hand)
    return y
t = np.linspace(0,10)

# Streamlit stuff
st.latex(r"y(t) = ae^{-2t/3} + \frac{2a-3}{3}te^{-2t/3}, 0\le t \le8, a>0") # Labels the top of the site with the function I am modeling 
st.sidebar.markdown("# Variables") # Creates and Labels a sidebar with 'Variables' at the top in bold
a = st.sidebar.slider( 
    "Select values of a", 
     1, 100
    )
# the above code implements a value slider from 0,100 (integers) for a
df_1 = pd.DataFrame(
    {
        'input': t ,
        'output': func(a,t)
    }
)
# Plot to for 0<=t<=8
st.line_chart(df_1,x='input' ,y='output', x_label='t', y_label='y(t)') # creates a line chart from columns in the DataFrame above

t_2 = np.linspace(0,15)
df_2 = pd.DataFrame(
    {
        'input': t_2,
        'output': func(a, t_2) 
    }
)
st.latex(r"y(t) = ae^{-2t/3} + \frac{2a-3}{3}te^{-2t/3}, 0\le t \le15, a>0") 
# Plot to for 0<=t<=15
st.line_chart(df_2,x='input' ,y='output', x_label='t', y_label='y(t)') # creates a line chart from columns in the 'DataFrame above
