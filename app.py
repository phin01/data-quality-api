from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import random
from prometheus_client import Counter


app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='endpoint')

@app.route('/')
def main():
    return 'OK'

@app.route('/kpi')
@metrics.counter(
    'KPI_OXE', 'Number of invocations per collection', labels={
        'status': lambda resp: resp.status_code,
        'status2': lambda: random.random()
    })
def get_item_from_collection():
    output = 'KPI_ALEATORIO{endpoint="main",le="0.005",method="GET",status="200"} ' + str(random.random()) + "\n" + 'KPI_ALEATORIO2{endpoint="main",le="0.005",method="GET",status="200"} 5.0'
    return output

app.run(port=5000)