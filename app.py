from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    api_url = 'https://dog-api.kinduff.com/api/facts?number=1'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            responseFacts={
                "Response":data['facts'][0]
            }
            return jsonify(responseFacts)
        else:
            errorMessage={
            "Success":False,
            "Message":f'Request failed with status code {response.status_code}'
            }

            return jsonify(errorMessage), response.status_code

    except requests.exceptions.RequestException as e:
        errorMessage={
            "Success":False,
            "Message":f'Request failed: {str(e)}'
        }
        return jsonify(errorMessage), 500
    
    