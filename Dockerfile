FROM python:3

ADD eight_queens_puzzle.py /
ADD databaseQueensPuzzle.py /
ADD test_eight_queens_puzzle.py /
ADD README.md /

RUN pip install ortools
RUN pip install SQLAlchemy

CMD [ "python", "./eight_queens_puzzle.py" ]