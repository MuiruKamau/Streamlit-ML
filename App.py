import streamlit as st
import numpy as np
import pandas as pd

# Read a simple data frame using pandas
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 8, 6, 4, 2]})
st.write(df)

st.title('Hello World')
st.write('This is a simple hello world app')


