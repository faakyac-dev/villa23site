from flask import Flask, render_template
from events import get_events

app = Flask(__name__)

@app.route("/")
def home():
    # Get events from events.py
    events = get_events()
    return render_template("index.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)