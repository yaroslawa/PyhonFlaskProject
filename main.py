from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__, static_url_path="/static", static_folder='static')

client = MongoClient('mongodb', 27017,
                     username='root',
                     password='pass')
db = client['html_events']
collection = db['btn_events']


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.post('/api/events')
def load_events():
    element_id = request.json.get('element_id')
    event_type = request.json.get('event_type')
    timestamp = request.json.get('timestamp')
    print(element_id, event_type, timestamp)
    data = {'element_id': element_id,
            'event_type': event_type,
            'timestamp': timestamp}
    return jsonify({"uuid": str(collection.insert_one(data).inserted_id)})


@app.route('/event-logs/<event_type>')
def event_logs(event_type):
    results = collection.find({'event_type': event_type})
    return '\n'.join(map(lambda result: f'<p>{result}</p>', results))


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)