from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
    "Magacaa?",
    "Imisa jir baad tahay?",
    "Wadankee baad joogtaa?",
    "Maxaad baranaysaa?",
    "Maxaad rabtaa inaad noqoto mustaqbalka?"
]

@app.route("/")
def index():
    return "Flask app is running!"

@app.route("/get_question")
def get_question():
    step = int(request.args.get("step", 0))

    if step < len(questions):
        return jsonify({"question": questions[step]})
    else:
        return jsonify({"question": "Waad ku mahadsantahay! Su'aalaha waa dhamaadeen."})

@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()
    print(data)
    return jsonify({"status": "ok"})

# IMPORTANT for Vercel
def handler(environ, start_response):
    return app(environ, start_response)
