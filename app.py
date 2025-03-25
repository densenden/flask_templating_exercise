from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True, port=5001)
