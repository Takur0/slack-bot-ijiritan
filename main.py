# encode: UTF-8
from flask import Flask, request, Response, abort
import requests
import os
import json
from argparse import ArgumentParser

app = Flask(__name__)

configs = ["debug", "release"]
config = os.environ['BUILD_CONFIG']

ijiritan_user_id = os.environ['IJIRITAN_USER_ID']

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        body = request.get_json()
        print(body)
        # when url verifing
        if body["type"] == "url_verification":
            return Response(headers={'Content-Type': 'plain/text'}, response=body["challenge"])

        # when message.channel event occuring and message is not ijiritan's
        elif body["type"] == "event_callback" and not body["event"]["bot_id"] == 'BD8R0MWE9':
            message = body["event"]["text"]
            # echo
            webhook_urls = ['SLACK_WEBHOOK_URL','SLACK_WEBHOOK_URL_CALENDAR']
            for webhook_url in webhook_urls:
                # when debug config, ijiritan never chat in public channel
                if config == "debug":
                    if webhook_url == 'SLACK_WEBHOOK_URL':
                        continue

                requests.post(
                    os.environ[webhook_url],
                    json.dumps({"text":message}),
                    headers={'Content-Type': 'application/json'}
                )
            # return json.dumps(body)
    else:
        body = request.get_data(as_text=True)
        webhook_urls = ['SLACK_WEBHOOK_URL','SLACK_WEBHOOK_URL_CALENDAR']
        for webhook_url in webhook_urls:
            # when debug config, ijiritan never chat in public channel
            if config == "debug":
                if webhook_url == 'SLACK_WEBHOOK_URL':
                    continue

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
