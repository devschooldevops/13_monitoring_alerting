from flask import Flask
from prometheus_client import Counter, generate_latest

view_metric = Counter('view', 'Product view', ['product'])
buy_metric = Counter('buy', 'Product buy', ['product'])

app = Flask(__name__)

@app.route('/view/<id>')
def view_product(id):
    view_metric.labels(product=id).inc()
    return "View %s" % id

@app.route('/buy/<id>')
def buy_product(id):
    buy_metric.labels(product=id).inc()
    return "Buy %s" % id

@app.route('/metrics')
def metrics():
    return generate_latest()