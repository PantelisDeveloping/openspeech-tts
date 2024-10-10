from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
from functools import wraps
from art import tprint
import edge_tts
import asyncio
import tempfile
import os
import base64

app = Flask(__name__)

# Use environment variables for API_KEY and PORT
API_KEY = os.environ.get('API_KEY')
PORT = int(os.environ.get('PORT', 5000))

tprint("OPEN SPEECH")
print(f"OpenSource TTS API Compatible with OpenAI API")
print(f" ")
print(f"   ---------------------------------------------------------------- ")
print(f" * Serving OpenVoice API")
print(f" * Server running on http://localhost:{PORT}")
print(f" * Voice Endpoint Generated: http://localhost:{PORT}/v1/audio/speech")
print(f" ")
print("Press CTRL+C to quit")

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Missing or invalid API key"}), 401
        token = auth_header.split('Bearer ')[1]
        if token != API_KEY:
            return jsonify({"error": "Invalid API key"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/v1/audio/speech', methods=['POST'])
@require_api_key
def text_to_speech():
    data = request.json
    print(request.json)
    
    # for debug
    point = data.get('point', '')
    print(f"point: {point}")
    
    if point == "ping":
        return jsonify({
            "result": "pong"
        })
    
    if point != "app.openspeech.query" or 'params' not in data or 'input' not in data['params']:
        return jsonify({"error": "Invalid request format"}), 400

    text = data['params']['input']
    options = data['params'].get('options', {})
    model = options.get('model', 'tts-1')  # We will ignore this input
    voice = options.get('voice', 'en-US-AriaNeural')

    # Map OpenAI voices to edge-tts voices
    voice_mapping = {
        'alloy': 'en-US-AriaNeural',
        'echo': 'en-US-GuyNeural',
        'fable': 'en-GB-SoniaNeural',
        'onyx': 'en-US-ChristopherNeural',
        'nova': 'en-AU-NatashaNeural',
        'shimmer': 'en-US-JennyNeural'
    }

    edge_tts_voice = voice_mapping.get(voice, voice)

    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

    async def generate_speech():
        communicate = edge_tts.Communicate(text, edge_tts_voice)
        await communicate.save(output_file.name)

    asyncio.run(generate_speech())

    # Read the generated audio file and encode it to base64
    with open(output_file.name, "rb") as audio_file:
        encoded_audio = base64.b64encode(audio_file.read()).decode('utf-8')

    # Clean up the temporary file
    os.unlink(output_file.name)

    return jsonify({"result": encoded_audio})

@app.route('/v1/models', methods=['GET'])
@require_api_key
def list_models():
    models = [
        {"id": "tts-1", "name": "Text-to-speech v1"},
        {"id": "tts-1-hd", "name": "Text-to-speech v1 HD"}
    ]
    return jsonify({"data": models})

@app.route('/v1/voices', methods=['GET'])
@require_api_key
def list_voices():
    voices = edge_tts.list_voices()
    formatted_voices = [{"name": v['ShortName'], "language": v['Locale']} for v in voices]
    return jsonify({"voices": formatted_voices})

if __name__ == '__main__':
    if not API_KEY:
        print("Warning: API_KEY environment variable is not set.")
    http_server = WSGIServer(('0.0.0.0', PORT), app)
    http_server.serve_forever()