import model as ml
from flask import Flask, render_template, json, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Provide cross-origin-resource-sharing support

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/ajax')
def ajax_example():
	return render_template('ajax.html')

@app.route('/classifier', methods=['GET'])
def run_classifier():
	value = request.args.get('value', default = '*', type = str)
	return ml.classify(value)

@app.route('/postjson', methods=['POST'])
def run_postjson():
    jsond = request.json
    return json.dumps(jsond)

# start flask server 
if __name__ == "__main__":
	app.run(debug=True) 

