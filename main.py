from flask import Flask, request, render_template, jsonify
from gpt_helper import Responder
from database import Memory

app = Flask(__name__)
client = Responder()
db = Memory()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    memory = db.read_from_memory()
    memory = '---'.join(mem[0] for mem in memory)
    response = client.get_completion(user_input, memory)
    db.write_to_memory(user_input, response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)