# encode: UTF-8
from flask import Flask, request, Response, abort
import requests
import os
import json
from argparse import ArgumentParser

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    
    #when url verifing
    if request.is_json:
        body = request.get_json()
        if body["type"] == "url_verification":
           return Response(headers={'Content-Type': 'application/json'},response=body["challenge"])

    else:
        body = request.get_data(as_text=True)
        webhook_urls = ['SLACK_WEBHOOK_URL','SLACK_WEBHOOK_URL_CALENDAR']
        for webhook_url in webhook_urls:    
            requests.post(
                os.environ[webhook_url],
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
