from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    if height == 0:
        return 0
    height_m = height / 100
    return round(weight / (height_m ** 2), 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "normal"
    elif 25 <= bmi < 29.9:
        return "Overweight", "overweight"
    else:
        return "Obese", "obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi_result = None
    bmi_category = None
    category_class = None

    submitted_weight = ""
    submitted_height = ""

    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight', 0))
            height = float(request.form.get('height', 0))
            
            submitted_weight = request.form.get('weight', '')
            submitted_height = request.form.get('height', '')

            if weight > 0 and height > 0:
                bmi_result = calculate_bmi(weight, height)
                bmi_category, category_class = get_bmi_category(bmi_result)
            else:
                bmi_category = "Please enter valid positive numbers for weight and height."
                category_class = "error"


        except (ValueError, TypeError):
            bmi_category = "Invalid input. Please enter numbers only."
            category_class = "error"


    return render_template('index.html',
                           bmi=bmi_result,
                           category=bmi_category,
                           category_class=category_class,
                           weight=submitted_weight,
                           height=submitted_height)

if __name__ == '__main__':
    app.run(debug=True)

