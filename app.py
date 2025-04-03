from flask import Flask, request, jsonify, render_template
from morse_code import MorseCode

app = Flask(__name__)
morse = MorseCode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': '请提供要编码的文本'}), 400
    
    text = data['text']
    morse_code = morse.encode(text)
    return jsonify({'morse_code': morse_code})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    if not data or 'morse_code' not in data:
        return jsonify({'error': '请提供要解码的摩尔斯电码'}), 400
    
    morse_code = data['morse_code']
    text = morse.decode(morse_code)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)