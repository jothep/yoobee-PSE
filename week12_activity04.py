from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    result_html = ''

    if request.method == 'POST':
        weight_str = request.form.get('weight')
        height_str = request.form.get('height')

        if weight_str and height_str:
            try:
                weight_kg = float(weight_str)
                height_cm = float(height_str)
                height_m = height_cm / 100

                if height_m == 0:
                    raise ZeroDivisionError

                bmi = weight_kg / (height_m ** 2)
                
                if bmi < 18.5:
                    classification = "Underweight"
                elif 18.5 <= bmi < 25:
                    classification = "Normal weight"
                elif 25 <= bmi < 30:
                    classification = "Overweight"
                else:
                    classification = "Obesity"
                
                result_html = f'''
                <hr>
                <h2>BMI Calculator Result</h2>
                <p>Your BMI is: {bmi:.2f}</p>
                <p>You are classified as: {classification}</p>
                '''
            except (ValueError, ZeroDivisionError):
                result_html = '''
                <hr>
                <p style="color: red;">Invalid input. Please enter valid numbers.</p>
                '''

    return f'''
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="UTF-8">
        <title>BMI Calculator</title>
    </head>
    <body>
        <h1>BMI Calculator</h1>
        <form action="/" method="POST">
            Weight in kilograms(kg): <input type="text" name="weight" required><br><br>
            Height in centimeters(cm): &nbsp;&nbsp;&nbsp;<input type="text" name="height" required><br><br>
            <button type="submit">Calculate BMI</button>
        </form>

        {result_html}

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)