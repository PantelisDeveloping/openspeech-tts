from flask import Flask, request, send_file, jsonify
from gevent.pywsgi import WSGIServer
from functools import wraps
from art import tprint
import edge_tts
import asyncio
import tempfile
import getpass

app = Flask(__name__)

API_KEY = getpass.getpass("Enter your desired API key: ")
PORT = int(input("Enter the port number: "))

tprint("OPEN VOICE")
print(f"OpenSource TTS API Compatible with OpenAI API")
print(f" ")
print(f"   ---------------------------------------------------------------- ")
print(f" * Serving OpenVoice API")
print(f" * Server running on http://localhost:{PORT}")
print(f" * VOice Endpoint Generated: http://localhost:{PORT}/v1/audio/speech")
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
    if not data or 'input' not in data:
        return jsonify({"error": "Missing 'input' in request body"}), 400

    text = data['input']
    model = data.get('model', 'tts-1') # We will ignore this input
    voice = data.get('voice', 'en-US-AriaNeural')

    # Map OpenAI voices to edge-tts voices (this is a simple mapping, you might want to expand it)
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

    return send_file(output_file.name, mimetype="audio/mpeg", as_attachment=True, download_name="speech.mp3")

@app.route('/v1/models', methods=['GET'])
@require_api_key
def list_models():
    # For simplicity, we're returning a fixed list of "models"
    models = [
        {"id": "tts-1", "name": "Text-to-speech v1"},
        {"id": "tts-1-hd", "name": "Text-to-speech v1 HD"}
    ]
    return jsonify({"data": models})

@app.route('/v1/voices', methods=['GET'])
@require_api_key
def list_voices():
    voices = edge_tts.list_voices()
    # Transform the voice data to match OpenAI's format
    formatted_voices = [{"name": v['ShortName'], "language": v['Locale']} for v in voices]
    return jsonify({"voices": formatted_voices})

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', PORT), app)
    http_server.serve_forever()