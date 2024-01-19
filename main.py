# GPT Clone

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    # Here you would process the input through your GPT model
    # For this example, we'll just echo the input
    return f"Your input was: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)