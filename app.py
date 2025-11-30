from flask import Flask, send_from_directory, redirect
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def root():
	return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
	safe_path = os.path.normpath(path)
	if safe_path.startswith('..'):
		return redirect('/')
	return send_from_directory('.', safe_path)

def create_app():
	return app

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
