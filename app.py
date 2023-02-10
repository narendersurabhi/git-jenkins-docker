from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return """<h1>Hello world!</h1>"""

@app.route('/stanford')
def stanford_page():
    return """<h1>Hello stanford!</h1>""" 

@app.route('/newyork')
def newyork_page():
    return """<h1>Hello newyork!</h1>""" 

@app.route('/tokyo')
def tokyo_page():
    return """<h1>Hello tokyo!</h1>"""

if __name__ == "__main__":
#     app.run(host='0.0.0.0',port=5050)
	app.run()