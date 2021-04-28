from flask import Flask
app = Flask(__name__)

indexData= 'index page data'
aboutData= 'about page data'
contactData= 'contact page data'

@app.route('/')
def index():
    return indexData


@app.route('/about')
def about():
    return aboutData

@app.route('/contact')
def contact():
    return contactData


if __name__ == '__main__':
    app.run(debug=True)
