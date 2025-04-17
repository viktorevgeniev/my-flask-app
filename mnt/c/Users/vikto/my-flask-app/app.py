```
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/transform', methods=['POST'])
def handle_text():
    data = request.get_json()
    text = data.get('text', '')
    transform_type = data.get('transform', '')

    if transform_type == 'reverse':
        transformed_text = text[::-1]
        return jsonify({'transformed_text': transformed_text})
    elif transform_type == 'uppercase':
        return jsonify({'transformed_text': text.upper()})
    elif transform_type == 'lowercase':
        return jsonify({'transformed_text': text.lower()})
    elif transform_type == 'wordcount':
        wordcount = len(text.split())
        return jsonify({'wordcount': wordcount})
    elif transform_type == 'capitalize':
        transformed_text = text.title()
        return jsonify({'transformed_text': transformed_text})
    else:
        return jsonify({'error': 'Unknown transform type'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 if not set
    app.run(host='0.0.0.0', port=port)
```