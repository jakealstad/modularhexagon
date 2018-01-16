from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
	return render_template('index.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
