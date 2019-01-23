# Eight Queens Puzzle
Solutions of the Eight queens puzzle with constraint programming with python 3

## External libraries used:
This libraries need to be installed before running the script.
1) **ortools:**  is an open source software suite for optimization, tuned for tackling the world's toughest problems in vehicle routing, flows, integer and linear programming, and constraint programming. https://developers.google.com
2) **sqlalchemy:**  is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. https://www.sqlalchemy.org/

## running test
Use the command pytest, in the container need to use the command this way: pytest test_eight_queens_puzzle.py 

## Run Script
1) **python eight_queens_puzzle.py**: solve the queen puzzle with a board of 8x8
2) **python eight_queens_puzzle.py N**: solve the queen puzzle with a board of NxN
2) **python eight_queens_puzzle.py -1**: Show all the results of the previous running of the Script.

## Run Script using Docker-Compose
1) **make docker-build**: create the images, containers and networks.
2) **make docker-exec**: run the eight queens puzzle with the default parameters.
3) **make docker-shell**: run the container and put you into the shell, so you can run manualy.
4) **make clean-docker**: clean the images and containers.
5) **make docker-test**: run the pytest in the container.

