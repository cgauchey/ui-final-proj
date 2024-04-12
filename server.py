from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# current_id = 1


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/posture/<int:item_id>')
def posture(item_id):
    if item_id == 2:
        return render_template('learn/posture/lower_crossed.html', id=item_id)
    else:
        return render_template('learn/posture/forward_head.html', id=item_id)


@app.route('/anatomy/')
def anatomy():
    return render_template('learn/anatomy/anatomy_carousel.html')


@app.route('/stretches/<int:item_id>')
def stretches(item_id):
    return render_template('learn/stretches/stretch.html', id=item_id)


@app.route('/quiz/<int:item_id>')
def quiz(item_id):
    return render_template('quiz/mc.html', id=item_id)


if __name__ == '__main__':
    app.run(debug=True)
