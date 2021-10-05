from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/sessions", methods=['POST'])
@cross_origin()
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

    total_count = len(full_payload)
    page = int(request.args.get('page'))
    print(f"\n\n\n\npage is {page}\n\n\n\n")
    size = int(request.args.get('size', 2))

    # 'results': full_payload[(page-1)*size:(page)*size]

    return {
        'results': full_payload[(page-1)*size:(page)*size],
        'total_count': total_count
    }
    