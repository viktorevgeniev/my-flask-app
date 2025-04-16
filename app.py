from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_text():
    text = request.json['text']
    transform_type = request.json['transform']

    if transform_type == 'reverse':
        transformed_text = reversed(text)
    elif transform_type == 'uppercase':
        transformed_text = text.upper()
    elif transform_type == 'lowercase':
        transformed_text = text.lower()
    elif transform_type == 'wordcount':
        wordcount = len(text.split())
        transformed_text = jsonify({'wordcount': wordcount})
    else:
        return jsonify({'error': 'Unknown transform type'}), 400

    return jsonify({'transformed_text': transformed_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

