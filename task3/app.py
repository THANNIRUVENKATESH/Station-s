from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch data from fakestoreapi
    api_url = 'https://fakestoreapi.com/products'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        products = response.json()  # Parse JSON response
    else:
        products = []  # In case of error, send an empty list

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
