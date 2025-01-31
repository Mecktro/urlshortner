# URL Shortener

This is a simple URL shortener application built using Python and Flask. It allows users to input a URL, which is then shortened using the TinyURL API. The shortened URL can then be used to redirect to the original URL.

## Features

- Accepts a URL from the user and generates a shortened version.
- Redirects users to the original URL when the shortened URL is accessed.
- Uses the `pyshorteners` library to generate short URLs.
- Built with Flask for easy deployment and web interface.

## Requirements

Before running the application, make sure you have Python installed. You also need to install the required dependencies.

### Dependencies

- Flask: A web framework for Python.
- pyshorteners: A library to create short URLs using various services like TinyURL.

You can install the required libraries using `pip`:

```bash
pip install flask pyshorteners

Running the Application

    Clone this repository or download the code files.

    Navigate to the folder where the code is located, and create a Python virtual environment (optional but recommended):
Running the Application

    Clone this repository or download the code files.

    Navigate to the folder where the code is located, and create a Python virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install the dependencies:

pip install flask pyshorteners

Run the application:

python url_shortener.py

Open your browser and go to:

    http://127.0.0.1:5000/

    Enter a URL you want to shorten and click on "Shorten". You will receive a shortened URL that redirects to the original URL.

How It Works

    The app uses Flask to handle HTTP requests.
    When you submit a URL, the app generates a shortened URL using the pyshorteners library (specifically the TinyURL service).
    The shortened URL is mapped to the original URL and stored in the app’s memory.
    When you visit a shortened URL, the app redirects you to the corresponding original URL.
