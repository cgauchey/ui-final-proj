from flask import Flask, render_template, request, redirect, url_for
from questions_data import questions
import random

app = Flask(__name__)

# current_id = 1
answers = {}
user_results = [True for _ in range(len(questions))]


postures = {
    "1": {
        "item_id": "1",
        "title": "Forward Head Posture",
        "image": "/static/forward-head.png",
        "description": "A common condition where your head is positioned with your ears in front of your body's vertical midline.",
        "text": [
            ["Headaches", "Fatigue", "Balance issues"],
            ["Pain and stiffness", "Impaired movement"],
            ["Pain and stiffness", "Impaired movement", "Respiratory issues"],
        ],
    },
    "2": {
        "item_id": "2",
        "title": "Lower Crossed Syndrome",
        "image": "/static/lower-cross.png",
        "description": "A common musculoskeletal condition characterized by specific patterns of muscle weakness and tightness that may affect the lower segment of the body.",
        "text": [["Protruding stomach"], ["Lower back pain"], ["Pain and stiffness"]],
    },
}

anatomies = {
    "1": {
        "item_id": "1",
        "title": "Muscles",
        "text": "Support and stabilize the skeletal system, aiding in proper alignment and resisting postural imbalances.",
    },
    "2": {
        "item_id": "2",
        "title": "Joints",
        "text": "Allow movement and contribute to posture; proper alignment of joints ensures balance and stability.",
    },
    "3": {
        "item_id": "3",
        "title": "Spine",
        "text": "Comprised of vertebrae and discs, maintaining its natural curves—cervical, thoracic, lumbar, and sacral—is key for good posture.",
    },
    "4": {
        "item_id": "3",
        "title": "Connective Tissues",
        "text": "Ligaments and tendons connect bones and muscles, providing support and stability crucial for posture.",
    },
}

stretcheslist = {
    "1": {
        "item_id": "1",
        "action": "strengthen",
        "target": "weak",
        "title": "Standing Chin Tucks",
        "media": "https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/07/Chin-tucks.gif?w=400",
        "text": [
            "Strengthen deep neck flexors",
            "Stand with the upper back against the wall, with the feet shoulder-width apart.",
            "Tuck the chin in and hold for a few seconds.",
            "Return to the starting position and repeat a number of times.",
        ],
    },
    "2": {
        "item_id": "2",
        "action": "strengthen",
        "target": "weak",
        "title": "Floor Cobras",
        "media": "https://www.ocregister.com/wp-content/uploads/migration/kpi/kpinsg-07exercicelg.jpg?w=400",
        "text": [
            "Strengthen lower trapz and serratus anterior ",
            "Lie on the floor, arms at side of body (or with arms in front of body in a “Superman” position), palms facing toward ground.",
            "Pinch shoulder blades together and lift chest off the floor. Hold for 2 seconds. Slowly return body to the ground, keeping chin tucked.",
        ],
    },
    "3": {
        "item_id": "3",
        "action": "strengthen",
        "target": "weak",
        "title": "Wall Angels",
        "media": "https://media.post.rvohealth.io/wp-content/uploads/sites/2/2021/04/GRT-1.7.Wall-Angels.gif",
        "text": [
            "Strengthen back muscles",
            "Stand against the wall: Align back and head; engage core.",
            "Raise arms in “V,” adjust feet for alignment.",
            "Bend elbows, lower hands above shoulders; hold, then return. Repeat 5-10x.",
        ],
    },
    "4": {
        "item_id": "4",
        "action": "stretch",
        "target": "tight",
        "title": "Upper Trapz Stretch",
        "media": "https://www.athletico.com/wp-content/uploads/2017/12/Stretch-of-the-Week-Self-Trapezius-Traction-Stretch-608x608.jpg",
        "text": [
            "Stretch upper trapezius and levator scapulae",
            "Tuck chin and slowly draw left ear to left shoulder.",
            "Continue by rotating chin downward until a slight stretch is felt on the right side.",
            "Perform the sequence on both sides, holding each stretch position for 20-30 seconds.",
        ],
    },
    "5": {
        "item_id": "5",
        "action": "stretch",
        "target": "tight",
        "title": "Chest Stretch",
        "media": "https://images.squarespace-cdn.com/content/v1/5a620a85d55b41e7233c5243/ae25b65f-ef76-40f5-8091-76cb07bdad9b/PleasantTerrificBettong-size_restricted.gif",
        "text": [
            "Stretch pecs and address forward head posture",
            "Stand upright with the feet shoulder-width apart.",
            "Bring the shoulders back and down.",
            "Interlace the fingers behind the back with the palms up.",
            "Draw the shoulders back and down, ensuring that the elbows are straight and that there is no arch in the low back.",
        ],
    },
}

back_stretchlist = {
    "1": {
        "item_id": "1",
        "part": "Upper Back",
        "image": "../../../static/upper.png",
        "stretch_names": [
            "Mindful shoulder circles",
            "Thoracic extension stretch",
            "Angel wings",
            "Shoulder stretch",
            "Neck stretch",
        ],
    },
    "2": {
        "item_id": "2",
        "part": "Lower Back",
        "image": "../../../static/lower.png",
        "stretch_names": ["Cat cow", "Extended puppy pose", "Locust Pose"],
    },
    "3": {
        "item_id": "3",
        "part": "Both",
        "image": "../../../static/both.png",
        "stretch_names": ["Thoracic rotation", "Sphinx", "Dynamic camel"],
    },
}


# ROUTES
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/favicon.ico")
def favicon():
    return "", 204


@app.route("/posture/<int:item_id>")
def posture(item_id):
    pos = postures[str(item_id)]
    if item_id == 2:
        return render_template("learn/posture/lower_crossed.html", id=item_id, pos=pos)
    else:
        return render_template("learn/posture/forward_head.html", id=item_id, pos=pos)


@app.route("/anatomy")
def anatomy():
    # anatomy = anatomies[str(item_id)]
    # print(anatomies)
    prev_url = "/posture/2"
    next_url = "/stretches/1"
    return render_template(
        "learn/anatomy/anatomy.html",
        anatomies=anatomies,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route("/stretches/<int:item_id>")
def stretches(item_id):
    stretch = stretcheslist[str(item_id)]
    if item_id == 1:
        prev_url = "/anatomy"
    else:
        prev_url = str(item_id - 1)
    if item_id == len(stretcheslist):
        next_url = "/stretches/back_stretches"
    else:
        next_url = str(item_id + 1)
    return render_template(
        "learn/stretches/stretch.html",
        id=item_id,
        stretch=stretch,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route("/stretches/back_stretches")
def back_stretches():
    return render_template(
        "learn/stretches/back_stretches.html", back_stretchlist=back_stretchlist
    )


@app.route("/quiz/<int:item_id>")
def quiz(item_id):
    if not item_id or item_id not in questions:
        return "<h1>quiz not found </h1>"

    # Assuming `answers` is accessible here, e.g., from session or database
    if item_id in answers:
        return redirect(url_for('results', item_id=item_id))

    quiz_data = questions.get(item_id)

    # drag and drop
    if quiz_data["type"] == "dragdrop":

        # shuffle the drag options
        drags = list(quiz_data["answer"].values())
        random.shuffle(drags)

        drops = list(quiz_data["answer"].keys())

        return render_template(
            "quiz/drag_drop.html",
            quiz=quiz_data,
            drags=drags,
            drops=drops,
        )

    # mcq
    elif quiz_data["type"] == "mcq":
        return render_template(
            "quiz/mc.html",
            quiz=quiz_data,
        )


# display results and update user score at the same time
@app.route("/quiz/results/<int:item_id>")
def results(item_id):
    global user_results

    if item_id not in answers:
        return "<h1>Please complete the question first!</h1>"

    quiz_data = questions.get(item_id)

    user_answer = answers[item_id]
    correct_answer = quiz_data["answer"]

    # update user score
    if user_answer != correct_answer:
        user_results[item_id-1] = False

    # mcq
    if quiz_data["type"] == "mcq":
        return render_template("quiz/mc_results.html",
                               id=item_id,
                               quiz=quiz_data,
                               user_answer=user_answer,
                               correct_answer=correct_answer)
    # dragdrop
    else:
        drops = list(quiz_data["answer"].keys())
        correct_drags = [quiz_data["answer"][drop] for drop in drops]
        correct_answer = zip(correct_drags, drops)
        user_answer = zip(list(answers[item_id].values()), drops)

        return render_template("quiz/drag_drop_results.html",
                               id=item_id,
                               quiz=quiz_data,
                               user_answer=user_answer,
                               correct_answer=correct_answer,
                               is_correct=user_results[item_id-1])


@app.route("/quiz/finalresults")
def final_results():
    if len(answers) != len(questions):
        return "<h1>Please complete the quiz first!</h1>"

    num_correct, num_wrong, percentage, results = get_quiz_final_results()
    return render_template(
        "quiz/results.html",
        final_score=[num_correct, num_wrong],
        percentage=percentage,
        results=results,
    )


# FUNCTIONS
def get_quiz_final_results():

    num_correct = sum(user_results)
    num_wrong = len(questions) - num_correct
    percentage = f"{num_correct}0%"

    return num_correct, num_wrong, percentage, user_results


# AJAX FUNCTIONS
@app.route("/save_answer", methods=["POST"])
def save_answer():
    global answers
    answer = request.get_json()

    quiz_id = int(answer["quizId"])
    user_answer = answer["answer"]

    answers[quiz_id] = user_answer
    return answer


@app.route("/clear_quiz_answers", methods=["POST"])
def clear_quiz_answers():
    global answers
    answers = {}

    return "400"


if __name__ == "__main__":
    app.run(debug=True)
