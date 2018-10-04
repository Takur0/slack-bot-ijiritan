# encode: UTF-8
from flask import Flask, request, abort
# import pprint
import requests
import os
import json
from argparse import ArgumentParser

app = Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
    # if request.method == 'POST':
    #     print(request.json)
    #     return '', 200
    # else:
    #     abort(400)

# @app.route('/hello', method=['POST'])
# def post_to_slack():
    response = requests.post(
        os.environ['SLACK_WEBHOOK_URL'],
        json.dumps({"text":"Hello, World! From Python!"}),
        headers={'Content-Type': 'application/json'}
    )

    # pprint.pprint(response.json())

if __name__ == '__main__':
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
