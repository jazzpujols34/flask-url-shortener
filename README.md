# URL Shortener in Flask with Python

This is a simple URL shortening application built with Flask, a lightweight web application framework in Python. The application provides functionality similar to services like bit.ly or TinyURL, allowing users to input a long URL and receive a shortened version that redirects to the original URL.

## File Descriptions

- `main.py` is the primary script which runs the Flask application, contains the routes and logic.
- `urls.json` stores the mapping between shortened URLs and original URLs.
- `index.html` is the HTML template for the homepage which contains a form for users to enter the URLs they wish to shorten.

## Application Logic

1. When a POST request is made with a long URL, the application generates a short URL using a combination of random letters and digits.
2. The short URL and original URL are stored as a key-value pair in the `shortened_urls` dictionary and also saved to `urls.json`.
3. When a GET request is made with the short URL, the application redirects to the original long URL. If the short URL does not exist in the dictionary, a 404 error is returned.

## Running the Application

To run the application, execute the following command in the terminal:

```bash
python main.py
Open your web browser and navigate to http://localhost:5000 to use the application.
```


## Future Work
Possible future enhancements could include:

- Implementing a user registration system to let users manage their URLs.
- Adding a feature to customize the short URL.
- Implementing analytics to track the number of times each shortened URL is used.


Please note that you might need to adjust the command to run the application and the localhost URL according to your actual configuration. The 'Future Work' section is just a suggestion - feel free to modify it based on your plans for the application.
