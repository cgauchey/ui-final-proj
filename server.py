from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# current_id = 1


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/learn/<int:item_id>')
def learn(item_id):
    return render_template('learn.html')


@app.route('/quiz/<int:item_id>')
def quiz(item_id):
    return render_template('quiz.html')


if __name__ == '__main__':
    app.run(debug=True)
