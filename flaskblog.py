from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')
    
@app.route('/contact')
def contact():
    return '<h1>Contact Us!</h1> <p>Please contact us for any questions you may have.</p>'
    
    
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug=True)