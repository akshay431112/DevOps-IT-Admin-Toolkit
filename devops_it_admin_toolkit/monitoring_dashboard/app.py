from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Monitoring Dashboard Coming Soon!'

if __name__ == '__main__':
    app.run(debug=True)