from flask import Flask, request

app = Flask(__name__)

@app.route("/sessions")
def hello_world():
    full_payload = [
        {
            'mouse_id': 1,
            'session_date': '2021-09-29',
        },
        {
            'mouse_id': 1,
            'session_date': '2021-09-28',
        },
        {
            'mouse_id': 1,
            'session_date': '2021-09-27',
        },
        {
            'mouse_id': 2,
            'session_date': '2021-09-26',
        },
        {
            'mouse_id': 2,
            'session_date': '2021-09-25',
        },
    ]
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 5))

    return {
        'results': full_payload[(page-1)*size:(page)*size],
    }
    