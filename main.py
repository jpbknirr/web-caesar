from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
            Rotate by:
            <input type="text" name="rot" value=0>
            <textarea input type="text" name="text">
            </textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation_number = request.form['rot']
    rot = int(rotation_number)
    form_text = request.form['text']
    text = str(form_text)
    encrypted_text = rotate_string(text, rot)  
    return "<h1>" + encrypted_text + "</h1>"


@app.route("/")
def index():
    return form

app.run()