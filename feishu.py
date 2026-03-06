from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_verify():
    return jsonify({
        "challenge": request.args.get('challenge', '')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)