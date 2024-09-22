from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'document' not in request.files:
        return jsonify({'error': 'No document uploaded.'})

    file = request.files['document']

    if file.filename == '':
        return jsonify({'error': 'No selected document.'})

    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)



    return jsonify({'message': 'Document uploaded successfully.'})


if __name__ == '__main__':
    app.run(debug=True)
