from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
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
        <label>
            Rotate by:
            <input type="text" name="rot" value="0"/>            
        </label><br>
        <textarea name="text"></textarea>
        <input type="submit" value="Submit"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rotated=''
    rot = request.form['rot']  
    rot=int(rot)  
    text=request.form['text']
    rotated=rotate_string(text, rot)
    
    return "<h1>" + rotated + "</h1>"

app.run()