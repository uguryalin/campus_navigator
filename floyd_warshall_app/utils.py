# utils.py - Auxiliary Functions

import streamlit as st
import pandas as pd
import numpy as np
import math
from algorithm import NODES

# Function to convert distance matrix to table
def format_matrix(matrix):
    formatted = []
    for row in matrix:
        formatted.append([
            ("∞" if (val == math.inf) else int(val)) for val in row
        ])
    return pd.DataFrame(formatted, columns=NODES, index=NODES)

# Find cells that are updated between steps
def get_updated_cells(prev_matrix, curr_matrix):
    updated = []
    for i in range(len(prev_matrix)):
        for j in range(len(prev_matrix)):
            if curr_matrix[i][j] != prev_matrix[i][j]:
                updated.append((i, j))
    return updated

# Style function for Streamlit table to apply color style
def highlight_updates(df, updated_cells):
    styles = pd.DataFrame("", index=df.index, columns=df.columns)
    for i, j in updated_cells:
        styles.iloc[i, j] = "background-color: #90ee90; font-weight: bold"  # green

    return df.style.apply(lambda _: styles, axis=None)

# Convert route to text format
def path_to_text(path):
    if not path:
        return "The way could not find."
    return " ➜ ".join(NODES[i] for i in path)
