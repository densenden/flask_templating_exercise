from flask import Flask, render_template, request
from http.server import BaseHTTPRequestHandler
import json

app = Flask(__name__)

app.config.update(
    SERVER_NAME='localhost:5002',
    APPLICATION_ROOT='/',
    PREFERRED_URL_SCHEME='http'
)

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
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with app.app_context():
                path = self.path
                if path == "/":
                    response = app.view_functions["index"]()
                elif path == "/about":
                    response = app.view_functions["about"]()
                elif path == "/services":
                    response = app.view_functions["services"]()
                elif path == "/services/brand-development":
                    response = app.view_functions["brand_development"]()
                elif path == "/services/webdesign":
                    response = app.view_functions["webdesign"]()
                elif path == "/mediation":
                    response = app.view_functions["mediation"]()
                elif path == "/software-development":
                    response = app.view_functions["software_development"]()
                elif path == "/art-department":
                    response = app.view_functions["art_department"]()
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b"Not Found")
                    return

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(str(response).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(e).encode())

# Für lokale Entwicklung
if __name__ == '__main__':
    app.run(debug=True, port=5002)
