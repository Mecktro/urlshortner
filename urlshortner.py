import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store shortened URLs
url_mapping = {}

def generate_short_code(length=6):
    """Generate a random short code for the URL."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """API endpoint to shorten a given URL."""
    data = request.get_json()
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({"error": "No URL provided"}), 400
    
    short_code = generate_short_code()
    url_mapping[short_code] = original_url
    
    return jsonify({"short_url": f"http://127.0.0.1:5000/{short_code}"})

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    """Redirect short URL to the original URL."""
    original_url = url_mapping.get(short_code)
    if original_url:
        return jsonify({"original_url": original_url})
    return jsonify({"error": "Short URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
