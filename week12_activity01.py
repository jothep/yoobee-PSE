from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    html_content = '''
    <p style="
        font-size: 72px;">
        Hello,<br>Flask!
    </p>
    '''
    return html_content

@app.route("/username/<name>")
def learn(name):
    html_content = f'''
    <p style="
        font-size: 72px;">
        {name} is learning Flask!
    </p>
    '''
    return html_content