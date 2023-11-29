from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/encode', methods=['POST'])
def encode_string():
    data = request.json
    if 'text' in data:
        text = data['text']
        text_bytes = text.encode('utf-8')
        base64_bytes = base64.b64encode(text_bytes)
        base64_string = base64_bytes.decode('utf-8')
        return jsonify({'encoded': base64_string})
    else:
        return jsonify({'error': 'No text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
