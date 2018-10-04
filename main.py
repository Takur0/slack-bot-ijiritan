# encode: UTF-8
from flask import Flask, request, abort
import pprint
import requests
import os
import json

app = Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return '', 200
    else:
        abort(400)


def post_to_slack():
    response = requests.post(
        os.environ['SLACK_WEBHOOK_URL'],
        json.dumps({"text":"Hello, World! From Python!"}),
        headers={'Content-Type': 'application/json'}
    )

    # pprint.pprint(response.json())

if __name__ == '__main__':
    app.run()
    post_to_slack()