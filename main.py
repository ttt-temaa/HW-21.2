from flask import Flask, Response, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_contact(path):
    try:
        with open('src/contact.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        return Response(html_content, content_type='text/html', status=200)
    except FileNotFoundError:
        return Response('<h1>404 - Not Found</h1>', content_type='text/html', status=404)


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
