# app.py - Interface of Streamlit

import streamlit as st
from algorithm import NODES, create_initial_graph, floyd_warshall, reconstruct_path
from utils import format_matrix, get_updated_cells, highlight_updates, path_to_text

st.set_page_config(page_title="Campus Navigator", layout="wide")
st.title("🎓 Campus Navigator -Algorithm of Floyd-Warshall")

# Prepare data
original_graph = create_initial_graph()
dist_matrix, next_node, steps = floyd_warshall(original_graph)

# Sidebar: Get start and destination points from user
st.sidebar.header("🔍 Route Selection")
start_name = st.sidebar.selectbox("Initial Point", NODES)
end_name = st.sidebar.selectbox("Target Point", NODES, index=1)

start = NODES.index(start_name)
end = NODES.index(end_name)

# Main section: Show matrix steps
st.header("🔢 Step by Step Distance Matrix")

for k, matrix in enumerate(steps):
    st.subheader(f"Step {k + 1} - Waypoint: {NODES[k]}")
    df = format_matrix(matrix)
    if k == 0:
        updated = get_updated_cells(create_initial_graph(), matrix)
    else:
        updated = get_updated_cells(steps[k - 1], matrix)
    styled_df = highlight_updates(df, updated)
    st.dataframe(styled_df, use_container_width=True)

st.divider()

# Result: Shortest path and distance between two selected buildings
st.header("📍 Information of the shortest way")

if start == end:
    st.info("Please choose two different point.")
else:
    path = reconstruct_path(start, end, next_node)
    distance = dist_matrix[start][end]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛣️ Road Route")
        st.success(path_to_text(path))

    with col2:
        st.subheader("📏 Total Distance")
        st.metric(label="In meters", value=f"{int(distance)} m")

st.caption("@2025 - Fırat University Software Eng.", unsafe_allow_html=True)