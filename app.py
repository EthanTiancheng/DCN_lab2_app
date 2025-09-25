from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/time")
def get_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current server time: {now}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
