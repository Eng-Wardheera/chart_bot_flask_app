from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Su'aalo bot-ka
questions = [
    "Magacaa?",
    "Imisa jir baad tahay?",
    "Wadankee baad joogtaa?",
    "Maxaad baranaysaa?",
    "Maxaad rabtaa inaad noqoto mustaqbalka?"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_question", methods=["GET"])
def get_question():
    step = int(request.args.get("step", 0))
    
    if step < len(questions):
        return jsonify({"question": questions[step]})
    else:
        return jsonify({"question": "Waad ku mahadsantahay! Su'aalaha waa dhamaadeen."})

@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()
    user_answer = data.get("answer")
    step = data.get("step")

    print(f"User Answer {step}: {user_answer}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
