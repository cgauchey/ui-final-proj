from flask import Flask, render_template, request, jsonify
from questions_data import questions
import random

app = Flask(__name__)

# current_id = 1
answers = []


#ROUTES

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/posture/<int:item_id>')
def posture(item_id):
    if item_id == 2:
        return render_template('learn/posture/lower_crossed.html', id=item_id)
    else:
        return render_template('learn/posture/forward_head.html', id=item_id)


@app.route('/anatomy/<int:item_id>')
def anatomy(item_id):
    return render_template('learn/anatomy/anatomy_carousel.html')


@app.route('/stretches/<int:item_id>')
def stretches(item_id):
    return render_template('learn/stretches/stretch.html', id=item_id)


@app.route('/quiz/<int:item_id>')
def quiz(item_id):
    quiz_data = questions.get(item_id) 
    
    if not quiz_data: 
        return "<h1>Quiz not found</h1>"
    elif quiz_data["type"] == "dragdrop": 
        drags = list(quiz_data['answers'].values())
        random.shuffle(drags)
        drops = list(quiz_data['answers'].keys())
        random.shuffle(drops)
        return render_template('quiz/drag_drop.html', quiz=quiz_data, drags = drags, drops=drops)
    elif quiz_data["type"] == "mcq": 
        return render_template('quiz/mc.html', quiz=quiz_data)
    


@app.route('/quiz/results/<int:item_id>')
def results(item_id):
    return render_template('quiz/results.html', id=item_id)



#AJAX FUNCTIONS
@app.route('/save_answer', methods=['POST'])
def save_answer():
    global answers 
    answer = request.get_json()
    answers.append(answer)
    return answer


if __name__ == '__main__':
    app.run(debug=True)
