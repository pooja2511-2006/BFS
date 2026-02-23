import streamlit as st
from collections import deque

# Define the tree structure
trees = {
    1: [5, 6],
    5: ['a', 'b'],
    6: ['c', 'd'],
    'a': [2, 3],
    'b': ['e'],
    'c': [],
    'd': [],
    2: [],
    3: [],
    'e': []
}

def bfs(start):
    traversal = []
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
            queue.extend(trees[node])
    return traversal

# Streamlit UI
st.title("🌳 BFS Traversal Visualizer")

# Dropdown for start node
start_node = st.selectbox("Select Start Node:", list(trees.keys()))

# Run BFS when button clicked
if st.button("Run BFS"):
    traversal_result = bfs(start_node)
    st.success(f"BFS Traversal starting from {start_node}:")
    st.write(" → ".join(map(str, traversal_result)))
