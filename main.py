# encode: UTF-8
from flask import Flask, request, abort
import requests
import os
import json
from argparse import ArgumentParser

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.get_data(as_text=True)
    response = requests.post(
        os.environ['SLACK_WEBHOOK_URL'],
        json.dumps({"text":body}),
        headers={'Content-Type': 'application/json'}
    )


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
