# Campus Navigator - Floyd-Warshall Visualizer

## Project Overview

This project is an interactive web application that implements and visualizes the Floyd-Warshall algorithm, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

### Problem Definition

The Floyd-Warshall algorithm is used to find the shortest paths between all pairs of nodes in a weighted graph. In this project, the graph represents points of interest within the university campus.

### Mathematical Background

The Floyd-Warshall algorithm uses dynamic programming to progressively improve the estimate of the shortest path between two vertices. The algorithm works by considering all pairs of nodes and checking if a path through an intermediate node results in a shorter path.

### Algorithm Steps

1. Initialize a distance matrix with direct distances between nodes.
2. Set the distance from each node to itself as zero.
3. For each intermediate node `k`, update the shortest path from node `i` to node `j` by comparing the current distance with the sum of the distances from `i` to `k` and from `k` to `j`.
4. Repeat for all pairs (i, j) and all intermediate nodes k.

### Pseudocode

```
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
```

## Complexity Analysis

### Time Complexity

- **Best Case:** O(n**3) - The algorithm always runs in cubic time regardless of graph structure.
- **Average Case:** O(n**3) - Applies to all graphs.
- **Worst Case:** O(n**3) - Even in dense graphs, the time complexity remains cubic.

### Space Complexity

- O(n**2) - A matrix of size n x n is used to store distances.

## Features

- Step-by-step visualization of the Floyd-Warshall algorithm
- Matrix updates displayed in real-time
- Selection of campus locations as nodes
- Visual indication of shortest paths and intermediate steps

## Screenshots

![Main Interface] (Ekran Görüntüsü (82).png)
*User interface showing building selection and algorithm start*

![Algorithm in Action] (Ekran Görüntüsü (85).png)
*Visualization of the distance matrix being updated*

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/uguryalin/campus_navigator/tree/main/floyd_warshall_app
   cd campus-navigator
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Select start and end campus locations.
2. Click the “Run Algorithm” button to visualize shortest paths.
3. Use the matrix viewer to understand step-by-step matrix updates.

### Example Inputs

- From "Library" to "30th Year Cafe" → Output: Shortest route and distance.
- From "Refectory" to "Murad Mosque" → Output: Shortest route and matrix path.
- From "Faculty of Technology" to "Sok Market" → Output: Shortest route highlighted.

## Implementation Details

### Key Components

- `algorithm.py`: Contains the Floyd-Warshall implementation
- `app.py`: Main Streamlit application logic and UI
- `utils.py`: Helper functions for data formatting and matrix display
- `visualizer.py`: Dynamic matrix and path visualization tools

### Code Highlights

```python
def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

## Testing

This project includes a test suite to verify the correctness of the Floyd-Warshall implementation:

```bash
pytest test_algorithm.py
```

### Test Cases

- 4-node sample matrix with known paths
- Edge case with disconnected nodes
- Fully connected matrix with random weights

## Live Demo

A live demo of this application is available at: [https://campusnavigator-floydwarshall.streamlit.app/]

## Limitations and Future Improvements

### Current Limitations

- Visualization performance may degrade with very large graphs
- No error handling for invalid inputs yet
- Static campus layout limits dynamic use

### Planned Improvements

- Add interactive map interface for node selection
- Improve real-time visualization animations
- Add multilingual support (Turkish/English)

## References and Resources

### Academic References

1. Introduction to Algorithms - Cormen et al.
2. Algorithm Design Manual - Steven Skiena
3. Lecture slides from Algorithms and Programming II

### Online Resources

- https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
- https://streamlit.io/
- https://visualgo.net/en/floydwarshall

## Author

- **Name:** [UGUR YALIN]
- **Student ID:** [230543014]
- **GitHub:** [https://github.com/uguryalin]

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project and for the opportunity to explore algorithm visualization techniques.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*
