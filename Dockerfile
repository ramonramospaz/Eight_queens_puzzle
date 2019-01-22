FROM python:3.7

ADD eight_queens_puzzle.py /
ADD databaseQueensPuzzle.py /
ADD test_eight_queens_puzzle.py /
ADD README.md /

RUN python3 -m pip install -U SQLAlchemy
RUN python3 -m pip install -U psycopg2-binary 
RUN python3 -m pip install -U pytest

CMD [ "python", "./eight_queens_puzzle.py" ]