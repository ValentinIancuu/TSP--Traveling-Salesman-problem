
# TSP Problem

# Traveling Salesman Problem Solver

This Python script provides solutions to the Traveling Salesman Problem (TSP) using various search techniques.

## Overview

The Traveling Salesman Problem (TSP) is a classic problem in computer science and optimization. Given a list of cities and the distances between each pair of cities, the task is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## Usage

To use this script, follow these steps:

1. **Install Dependencies**: Make sure you have Python 3.x installed on your system along with the `networkx` library.

    ```bash
    pip install networkx
    ```

2. **Run the Script**: Execute the script `tsp_solver.py` in your Python environment.

    ```bash
    python tsp_solver.py
    ```

3. **Input Data**: Provide the filename containing the TSP data when prompted. The data file should contain the distances between each pair of cities.

4. **Choose Technique**: Select one of the following techniques to solve the TSP:

    - Depth-First Search (DFS)
    - Uniform Cost Search (UCS)
    - A* Search

5. **View Results**: The script will display the best path found and its corresponding minimum cost.

## Code Structure

- `tsp_solver.py`: Contains the main script for solving the TSP.
- `README.md`: This file providing information about the script and its usage.

## Modules and Functions

### `TSP` Class

- **`__init__(self, file_name)`**: Initializes the TSP instance with the given data file.
- **`load_data(self, file_name)`**: Loads TSP data from the given file.
- **`find_index(self, city)`**: Finds the index of a city in the list of cities.
- **`dfs(self)`**: Solves the TSP using Depth-First Search.
- **`ucs(self)`**: Solves the TSP using Uniform Cost Search.
- **`mst_cost(self, unvisited)`**: Calculates the minimum spanning tree (MST) cost for the given set of unvisited cities.
- **`a_star(self)`**: Solves the TSP using A* Search.

### `main()` Function

- **`main()`**: Main function to execute the TSP solver script. Prompts the user for input and displays the results. 
## Interact with menu based interface;
1. DFS
2. LCS
3. A*
enter the file name you want to test on and choose the desired algorithm.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Questions
### how to run the python file?

You can use pycharm/ Visualstudio or any other python supporting environment.

### how to edit latex pdf?
You can edit latex pdf using link: [https://www.overleaf.com]

