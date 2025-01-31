from flask import Flask, request, redirect, render_template_string
import pyshorteners

app = Flask(__name__)

# Initialize the URL shortener
s = pyshorteners.Shortener()

# Store the original URL and shortened URL mappings
url_mapping = {}

@app.route('/')
def index():
    return render_template_string("""
    <html>
        <body>
            <h1>URL Shortener</h1>
            <form action="/shorten" method="POST">
                <label for="url">Enter URL: </label>
                <input type="text" id="url" name="url" required>
                <button type="submit">Shorten</button>
            </form>
        </body>
    </html>
    """)

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_url = s.tinyurl.short(original_url)
    url_mapping[short_url] = original_url
    return render_template_string("""
    <html>
        <body>
            <h1>Your Shortened URL</h1>
            <p>Short URL: <a href="{{ short_url }}" target="_blank">{{ short_url }}</a></p>
            <a href="/">Go Back</a>
        </body>
    </html>
    """, short_url=short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    full_url = url_mapping.get(short_url)
    if full_url:
        return redirect(full_url)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
