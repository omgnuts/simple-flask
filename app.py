import model as ml
from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/classifier', methods=['GET'])
def run_classifier():
	value = request.args.get('value', default = '*', type = str)
	return ml.classify(value)

# start python 
if __name__ == "__main__":
	app.run()

