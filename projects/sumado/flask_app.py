import mainfunction
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<adj>')
def get_adj(adj="3x3_v1"):
    return mainfunction.main(adj)
