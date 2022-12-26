from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

        
if __name__ == "__main__":
    app.run(host='127.0.0.1:5000', port=5000, debug=True)
