from flask import Flask, render_template, request
from http.server import BaseHTTPRequestHandler
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/services/brand-development')
def brand_development():
    return render_template('services/brand-development.html')

@app.route('/services/webdesign')
def webdesign():
    return render_template('services/webdesign.html')

@app.route('/mediation')
def mediation():
    return render_template('mediation.html')

@app.route('/software-development')
def software_development():
    return render_template('software-development.html')

@app.route('/art-department')
def art_department():
    return render_template('art-department.html')

# Für Vercel Serverless
def handler(request):
    """Handle incoming requests."""
    if request.method == "GET":
        path = request.path
        if path == "/":
            return app.view_functions["index"]()
        elif path == "/about":
            return app.view_functions["about"]()
        elif path == "/services":
            return app.view_functions["services"]()
        elif path == "/services/brand-development":
            return app.view_functions["brand_development"]()
        elif path == "/services/webdesign":
            return app.view_functions["webdesign"]()
        elif path == "/mediation":
            return app.view_functions["mediation"]()
        elif path == "/software-development":
            return app.view_functions["software_development"]()
        elif path == "/art-department":
            return app.view_functions["art_department"]()
        else:
            return "Not Found", 404
    else:
        return "Method not allowed", 405

# Für lokale Entwicklung
if __name__ == '__main__':
    app.run(debug=True, port=5001)
