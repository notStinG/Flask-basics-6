from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/display", methods=["POST"])
def display():
    rgb_values = request.form["rgb_values"]
    rgb_list = rgb_values.splitlines()
    colors = []
    for rgb in rgb_list:
        try:
            r, g, b = map(int, rgb.split(","))
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                colors.append(f"rgb({r},{g},{b})")
            else:
                colors.append("rgb(255,255,255)")  
        except ValueError:
            colors.append("rgb(255,255,255)")  
    return render_template("display.html", colors=colors)

@app.route("/generate_random", methods=["GET"])
def generate_random():
    rgb_list = []
    for __ in range(100):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_list.append(f"rgb({r}, {g}, {b})")
    return render_template("display.html", colors=rgb_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
