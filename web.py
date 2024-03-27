from flask import Flask

web = Flask(__name__)

@web.route('/')
def home():
    return """
    <html>
    <head><title>Luna</title></head>
    <body>
        <h1>Luna is beautiful</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    web.run(debug=True)
