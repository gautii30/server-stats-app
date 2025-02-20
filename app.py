import os
import getpass
import subprocess
from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "gautam saraf"
    system_username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"], text=True)
    except Exception as e:
        top_output = f"Error running top: {e}"
    html_response = f"""
    <html>
      <head>
        <title>HTop Stats</title>
      </head>
      <body>
        <h1>HTop Endpoint</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {system_username}</p>
        <p><strong>Server Time (IST):</strong> {now_ist}</p>
        <hr />
        <pre>{top_output}</pre>
      </body>
    </html>
    """
    return html_response

@app.route('/')
def index():
    return "Server Stats App is running. Go to /htop for details."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
