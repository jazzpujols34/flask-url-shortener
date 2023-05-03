# Import required modules
import random 
import string
import json 
from flask import Flask, render_template, redirect, request

# Initialize Flask application
app = Flask(__name__)

# Dictionary to store shortened URLs
shortened_urls = {}

# Function to generate a short URL
def generate_short_url(length=6):
    # Define the characters to use in short URLs
    chars = string.ascii_letters + string.digits
    # Generate a random string of the defined length using the characters
    short_url = "".join(random.choice(chars) for _ in range (length))
    return short_url

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    # If the request method is POST, a long URL has been submitted
    if request.method == "POST":
        # Get the long URL from the form data
        long_url = request.form['long_url']
        # Generate a short URL
        short_url = generate_short_url()
        # If the short URL is already in use, generate a new one
        while short_url in shortened_urls:
            short_url = generate_short_url()

        # Store the short and long URL mapping in the dictionary
        shortened_urls[short_url] = long_url
        # Write the dictionary to a JSON file
        with open("urls.json", "w") as f:
            json.dump(shortened_urls, f)
        # Return the short URL
        return f"Shortened URL: {request.url_root}{short_url}"
    # If the request method is GET, render the home page
    return render_template("index.html")

# Route for short URLs
@app.route("/<short_url>")
def redirect_url(short_url):
    # Get the long URL corresponding to the short URL
    long_url = shortened_urls.get(short_url)
    # If the long URL exists, redirect to it
    if long_url:
        return redirect(long_url)
    # If the long URL does not exist, return a 404 error
    else:
        return "URL not found", 404
    
# If this script is run directly, start the Flask application
if __name__ == "__main__":
    # Load the dictionary from the JSON file
    with open("urls.json", "r") as f:
        shortened_urls = json.load(f)
    # Start the Flask application
    app.run(debug=True)
