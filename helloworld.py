from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body { font-family: Arial; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .container { text-align: center; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); }
            h1 { color: #333; margin: 0; }
            button { background-color: #667eea; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
            button:hover { background-color: #764ba2; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, World!</h1>
            <button onclick="alert('Button clicked!')">Click Me</button>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
