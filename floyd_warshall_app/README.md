 Campus Navigator - Floyd-Warshall Visualizer
Developed as part of the "Algorithm and Programming II" semester project at Fırat University Software Engineering Department, this application provides step-by-step visualization of the Floyd-Warshall algorithm using campus building data.

 Project Purpose
This project aims to:

Correctly and efficiently implement the Floyd-Warshall algorithm in Python,

Display it step by step in a user-friendly interface using Streamlit,

Make understanding easier with enriched matrix visuals.

Technologies Used
Python 3.8+

Streamlit: For UI and visualization

Pandas: For matrix operations

 Campus Points (Nodes)
Refectory

Library

Faculty of Technology

Faculty of Education

Murad Mosque

Sok Market

30th Year Cafe

 Application Screenshots
Step-by-step distance matrices, shortest path, and route screen images will be added here.

 Complexity Analysis
Floyd-Warshall algorithm complexity:

Time: O(n³)

Space: O(n²)

Because for each pair of nodes, passing through a third node is attempted.

 How to Use?
Installation
bash
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
Running
bash
streamlit run app.py
🌐 Deployment URL
When deployed via Streamlit Cloud, the app URL will be added here:
https://your-streamlit-app-url

🧪 Tests
bash
pytest test_algorithm.py
📁 Folder Structure
bash
CampusNavigator/
│
├── app.py               # Main Streamlit application
├── algorithm.py         # Floyd-Warshall algorithm
├── utils.py             # Helper functions
├── requirements.txt     # Required libraries
├── test_algorithm.py    # Algorithm tests
└── README.md            # Project documentation
🔗 References
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

https://streamlit.io/

https://realpython.com/python-data-visualization/

📌 Note: This project was prepared by a student of Fırat University for academic purposes.

© 2025 All rights reserved.