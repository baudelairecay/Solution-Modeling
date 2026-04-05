import numpy as np
import streamlit as st
import pandas as pd
# Plotting for my solution to homework 5 part c

def func(a, t):
    y = a*np.exp((-2/3)*t) + ((2*a + 3)/3) * t * np.exp((-2/3)*t) # Solution to the DE(found by hand)
    return y
t = np.linspace(0,10)

# Streamlit stuff
st.markdown("# Solution") # Labels the top of the site with 'Solution' in bold
st.sidebar.markdown("# Variables") # Creates and Labels a sidebar with 'Variables' at the top in bold
a = st.sidebar.slider( 
    "Select values of a", 
     1, 100
    )
# the above code implements a value slider from 0,100 (integers) for a
df = pd.DataFrame(
    {
        'input': t ,
        'output': func(a,t)
    }
)

st.line_chart(df,x='input' ,y='output', x_label='t', y_label='y(t)') # creates a line chart from columns in the dataframe above
