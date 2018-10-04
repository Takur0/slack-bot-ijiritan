# encode: UTF-8

import pprint
import requests
import os
import json

def main():
    response = requests.post(
        os.environ['SLACK_WEBHOOK_URL'],
        json.dumps({"text":"Hello, World! From Python!"}),
        headers={'Content-Type': 'application/json'}
    )

    # pprint.pprint(response.json())

if __name__ == '__main__':
    main()