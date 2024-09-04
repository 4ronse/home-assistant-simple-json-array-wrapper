import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is missing"}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Wrap the JSON array in an object with a "data" key
        wrapped_data = {"data": data}

        return jsonify(wrapped_data)
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to fetch URL: {str(e)}"}), 500
    except ValueError:
        return jsonify({"error": "Invalid JSON response from the URL"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
