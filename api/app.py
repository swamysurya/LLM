from flask import Flask

app = Flask(__name__)

@app.route('/name')
def name():
    return 'My name is Flask!'


app.run(debug=True)