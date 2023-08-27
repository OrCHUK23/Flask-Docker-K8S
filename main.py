from flask import Flask, render_template
import os
import socket

app = Flask(__name__)
# s = socket()

@app.route('/')
def home():
    pod_name = socket.gethostname()
    return render_template('index.html', pod_name=pod_name)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)