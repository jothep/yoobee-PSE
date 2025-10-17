from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    html_content = '''
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Input the pic URL here.</title>
        <style>
        h1 {
            color: blue;
        }
        p {
            color: blue; font-size: 25px;
        }
    </style>
    </head>
    <body>
        <div class="container">
            <h1>Pic checking</h1>
            <p style="color: red; font-size: 20px;">This line is using Inline CSS.</p>
            <p> This line is effected by Internal CSS.</p>
            <form action="/show_image" method="GET">
                <input type="url" name="image_url" placeholder="Pls paste the URL here" required>
                <button type="submit">Show the picture</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return html_content

@app.route("/show_image")
def show_image():
    image_url = request.args.get('image_url', '')

    if image_url.startswith('http://') or image_url.startswith('https://'):
        image_display_html = '<img src="{}" alt="The picture which user gived" width="600">'.format(image_url)
    else:
        image_display_html = '<p>No useful image URL provided. Please make sure it starts with http:// or https://</p>'

    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>The picture</title>
        <link rel="stylesheet" href="{ url_for('static', filename='styles.css') }">
        <p> This page is using External CSS.</p>
    </head>
    <body>
        {image_display_html}
        <hr>
        <a href="/">Return to index</a>
    </body>
    </html>
    '''
    return html_content

if __name__ == "__main__":
    app.run(debug=True)