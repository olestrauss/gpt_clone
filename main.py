# main.py
from flask import Flask, request, render_template, jsonify
from gpt_helper import Responder

app = Flask(__name__)
client = Responder()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = client.get_completion(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
