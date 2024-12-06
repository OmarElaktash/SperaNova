from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot_response():
    user_message = request.json.get("message")
    if user_message.lower() == "hello":
        return jsonify({"response": "Hi! How can I support you today?"})
    return jsonify({"response": "I'm here to listen. Tell me more."})

if __name__ == '__main__':
    app.run(debug=True)
