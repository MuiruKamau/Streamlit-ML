import streamlit as st
import numpy as np
import pandas as pd

# Read a simple data frame using pandas
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 8, 6, 4, 2]})
st.write(df)

st.title('Hello World')
st.write('This is a simple hello world app')

import matplotlib.pyplot as plt

# Your data
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Graph')

# Show the plot
st.pyplot(fig)
