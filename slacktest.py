from slackclient import SlackClient
from flask import Flask, jsonify
import os

####### probably need to store as env variable

sc= SlackClient('ksu97t9Xghkr4cPEhVIf3qe9') 

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
	
	return jsonify({
    "response_type": "in_channel",
    "text": "Get Monay.",
    "attachments": [
        {
            "text":":dollar:"
        }
    ]
	})
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4040))
    app.run(host='0.0.0.0', port=port, debug=True)