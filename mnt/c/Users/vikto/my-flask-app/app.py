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

    if not text or not transform_type:
        return jsonify({'error': 'Please enter both a text and transformation type'}), 400

    transformed_text = transform_utils.transform(text, transform_type)
    return jsonify({'transformed_text': transformed_text})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 if not set
    app.run(host='0.0.0.0', port=port)