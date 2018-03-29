from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
    <!DOCTYPE html>

<html>
    <head>
        <style>         

            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
        <label>
            Rotate by:
            <input type="text" name="rot" value="0"/>            
        </label><br>
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Submit"/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():    
    return form.format("") 

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']  
    rot=int(rot)  
    text=request.form['text']
    rotated=rotate_string(text, rot)
    
    # content="<h1>" + cgi.escape(rotated) + "</h1>"
    # return form.format(content)

    return form.format(rotated)

app.run()