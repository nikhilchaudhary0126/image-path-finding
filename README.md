# Image Path Finding
This project can be used to compute the path between two pixels of a map image.
Various path finding algorithms like BFS, DFS, A* and Dijkstra can be used to find a path between pixels of images representing geographical features.
It also shows real-time traversing of pixels using the OpenCV module.

## Sample Outputs
The below diagrams show how provided ```terrain.png``` is traversed using Breadth First Search, Depth First Search, A* and Dijkstra algorithms respectively.

<img src="https://github.com/nikhilchaudhary0126/image-path-finding/blob/main/img/bfs.gif" alt="BFS" width="220" height="220"> <img src="https://github.com/nikhilchaudhary0126/image-path-finding/blob/main/img/dfs.gif" alt="DFS" width="220" height="220"/> <img src="https://github.com/nikhilchaudhary0126/image-path-finding/blob/main/img/astar.gif" alt="AStar" width="220" height="220"/> <img src="https://github.com/nikhilchaudhary0126/image-path-finding/blob/main/img/dijkstra.gif" alt="Dijkstra" width="220" height="220"/>

## Requirements
The repository contains the ```requirements.txt``` file with all the required modules.

Use this command to install all dependencies:
```python3 -m pip install -r requirements.txt```

## Instructions
* Provide a sample file as an input to the program.

* Specify path using ```path.txt```

* Edit the ```scripts/load.py``` file to configure terrain and pixel colors to identify the terrain details.

* Run using the below command:
```
python3 run.py <terrain file> <algorithm(bfs,dfs,ucs,astar)>
python3 run.py terrain.png astar
```

Although all algorithms can be used to find the path, it is recommended to use A* to find the shortest path using heuristic search.
