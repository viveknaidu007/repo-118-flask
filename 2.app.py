from flask import Flask

app = Flask(__name__)

@app.route('/')
def vivek():
    print("Route '/' was accessed")
    return "pls subscribe"

if __name__ == '__main__':
    print("Starting Flask app...")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
