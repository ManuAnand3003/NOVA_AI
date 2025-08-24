from flask import Flask, render_template, request, jsonify
from calculator import evaluate_expression
from sentiment import analyze_sentiment
from vision_module import analyze_image
from ai_generation_module import generate_text
from image_generation import generate_image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    expr = data.get('expression', '')
    try:
        result = evaluate_expression(expr)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/sentiment', methods=['POST'])
def api_sentiment():
    data = request.json
    text = data.get('text', '')
    result = analyze_sentiment(text)
    return jsonify({'result': result})

@app.route('/api/vision', methods=['POST'])
def api_vision():
    data = request.json
    image_url = data.get('image_url', '')
    result = analyze_image(image_url)
    return jsonify({'result': result})

@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    prompt = data.get('prompt', '')
    result = generate_text(prompt)
    return jsonify({'result': result})

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    message = data.get('message', '')
    reply, _ = gpt_response(message)
    return jsonify({'result': reply})

@app.route('/api/image-generate', methods=['POST'])
def api_image_generate():
    data = request.json
    prompt = data.get('prompt', '')
    output_path = generate_image(prompt)
    image_url = '/static/' + os.path.basename(output_path)
    static_path = os.path.join(app.root_path, 'static', os.path.basename(output_path))
    if not os.path.exists(static_path):
        try:
            os.replace(output_path, static_path)
        except Exception:
            pass
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.json
    expr = data.get('expression', '')
    try:
        result = evaluate_expression(expr)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/sentiment', methods=['POST'])
def api_sentiment():
    data = request.json
    text = data.get('text', '')
    result = analyze_sentiment(text)
    return jsonify({'result': result})

@app.route('/api/vision', methods=['POST'])
def api_vision():
    data = request.json
    image_url = data.get('image_url', '')
    result = analyze_image(image_url)
    return jsonify({'result': result})

@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    prompt = data.get('prompt', '')
    result = generate_text(prompt)
    return jsonify({'result': result})

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    message = data.get('message', '')
    response = gpt_response(message)
    return jsonify({'result': response})

    @app.route('/api/image-generate', methods=['POST'])
    def api_image_generate():
        data = request.json
        prompt = data.get('prompt', '')
        output_path = generate_image(prompt)
        image_url = '/static/' + os.path.basename(output_path)
        static_path = os.path.join(app.root_path, 'static', os.path.basename(output_path))
        if not os.path.exists(static_path):
            try:
                os.replace(output_path, static_path)
            except Exception:
                pass
        return jsonify({'image_url': image_url})
if __name__ == '__main__':
    app.run(debug=True)
