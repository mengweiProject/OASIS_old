import sys
from datetime import datetime
sys.path.append("../..")
sys.path.append("..")

from celeryTasks import app

@app.task
def print111():
    print(111)

@app.task
def add(x, y):
    print(datetime.now())
    return x + y