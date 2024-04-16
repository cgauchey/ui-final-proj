from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# current_id = 1


postures = {
    "1":{
        "item_id": "1",
        "title": "Forward Head Posture",
        "image": "https://static1.squarespace.com/static/5b4e58369d5abb9d6adac232/5b50dfab575d1ff383c06981/5c73effee79c704c50cf605d/1619981137718/Figure_18.4.png?format=300w",
        "text": [["Headaches","Fatigue","Balance issues"],["Pain and stiffness","Impaired movement"],["Pain and stiffness","Impaired movement","Respiratory issues"]]
    },
    "2":{
        "item_id": "2",
        "title": "Lower Crossed",
        "image": "https://www.yoganatomy.com/wp-content/uploads/2020/10/lcs-diagram.jpg",
        "text": [["Protruding stomach"],["Lower back pain"],["Pain and stiffness"]]
    }
}

anatomies = {
    "1":{
        "item_id": "1",
        "title": "Muscles",
        "text": "Support and stabilize the skeletal system, aiding in proper alignment and resisting postural imbalances."
    },
    "2":{
        "item_id": "2",
        "title": "Joints",
        "text": "Allow movement and contribute to posture; proper alignment of joints ensures balance and stability."
    },
    "3":{
        "item_id": "3",
        "title": "Spine",
        "text": "Comprised of vertebrae and discs, maintaining its natural curves—cervical, thoracic, lumbar, and sacral—is key for good posture."
    },
    "4":{
        "item_id": "3",
        "title": "Connective Tissues",
        "text": "Ligaments and tendons connect bones and muscles, providing support and stability crucial for posture."
    }
}

stretcheslist = {
    "1":{
        "item_id": "1",
        "action": "strengthen",
        "target": "weak",
        "title":"Standing Chin Tucks",
        "media": "https://i0.wp.com/post.healthline.com/wp-content/uploads/2020/07/Chin-tucks.gif?w=200",
        "text": ["Strengthen deep neck flexors","Stand with the upper back against the wall, with the feet shoulder-width apart.", "Tuck the chin in and hold for a few seconds.", "Return to the starting position and repeat a number of times."]
    },
    "2":{
        "item_id": "2",
        "action": "strengthen",
        "target": "weak",
        "title":"Floor Cobras",
        "media": "https://www.ocregister.com/wp-content/uploads/migration/kpi/kpinsg-07exercicelg.jpg?w=100",
        "text": ["Strengthen lower trapz and serratus anterior ","Lie on the floor, arms at side of body (or with arms in front of body in a “Superman” position), palms facing toward ground.", "Pinch shoulder blades together and lift chest off the floor. Hold for 2 seconds. Slowly return body to the ground, keeping chin tucked."]
    },
    "3":{
        "item_id": "3",
        "action": "strengthen",
        "target": "weak",
        "title":"Wall Angels",
        "media": "https://media.post.rvohealth.io/wp-content/uploads/sites/2/2021/04/GRT-1.7.Wall-Angels.gif",
        "text": ["Strengthen back muscles","Stand against the wall: Align back and head; engage core.", "Raise arms in “V,” adjust feet for alignment.", "Bend elbows, lower hands above shoulders; hold, then return. Repeat 5-10x."]
    },
    "4":{
        "item_id": "4",
        "action": "stretch",
        "target": "tight",
        "title":"Upper Trapz Stretch",
        "media": "https://www.athletico.com/wp-content/uploads/2017/12/Stretch-of-the-Week-Self-Trapezius-Traction-Stretch-608x608.jpg",
        "text": ["Stretch upper trapezius and levator scapulae", "Tuck chin and slowly draw left ear to left shoulder.", "Continue by rotating chin downward until a slight stretch is felt on the right side.", "Perform the sequence on both sides, holding each stretch position for 20-30 seconds."]
    },
    "5":{
        "item_id": "5",
        "action": "stretch",
        "target": "tight",
        "title":"Chest Stretch",
        "media": "https://images.squarespace-cdn.com/content/v1/5a620a85d55b41e7233c5243/ae25b65f-ef76-40f5-8091-76cb07bdad9b/PleasantTerrificBettong-size_restricted.gif",
        "text": ["Stretch pecs", "Stand upright with the feet shoulder-width apart.", "Bring the shoulders back and down.", "Interlace the fingers behind the back with the palms up.", "Draw the shoulders back and down, ensuring that the elbows are straight and that there is no arch in the low back."]
    }
}

back_stretchlist = {
    "1": {
        "item_id": "1",
        "part": "Upper Back",
        "image" : "https://img.freepik.com/premium-vector/back-muscles-educational-anatomical-diagram-posterior-model-human-structure-arrangement_193165-244.jpg",
        "stretch_names": ["Mindful shoulder circles", "Thoracic extension stretch", "Angel wings", "Shoulder stretch", "Neck stretch"]
    },
    "2":
    {
        "item_id": "2",
        "part": "Lower Back",
        "image" : "https://img.freepik.com/premium-vector/back-muscles-educational-anatomical-diagram-posterior-model-human-structure-arrangement_193165-244.jpg",
        "stretch_names": ["Cat cow", "Extended puppy pose", "Locust Pose"]
    },
    "3":
    {
        "item_id": "3",
        "part": "Both",
        "image" : "https://img.freepik.com/premium-vector/back-muscles-educational-anatomical-diagram-posterior-model-human-structure-arrangement_193165-244.jpg",
        "stretch_names": ["Thoracic rotation", "Sphinx", "Dynamic camel"]
    },

}

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/posture/<int:item_id>')
def posture(item_id):
    pos = postures[str(item_id)]
    if item_id == 2:
        return render_template('learn/posture/lower_crossed.html', id=item_id, pos=pos)
    else:
        return render_template('learn/posture/forward_head.html', id=item_id, pos=pos)


@app.route('/anatomy/<int:item_id>')
def anatomy(item_id):
    anatomy = anatomies[str(item_id)]
    if item_id == len(anatomies):
        next_url = '/stretches/1'
    else:
        next_url = str(item_id+1)
    return render_template('learn/anatomy/anatomy_carousel.html', anatomy=anatomy, next_url=next_url)


@app.route('/stretches/<int:item_id>')
def stretches(item_id):
    stretch = stretcheslist[str(item_id)]
    if item_id == len(stretcheslist):
        next_url = '/stretches/back_stretches'
    else:
        next_url = str(item_id+1)
    return render_template('learn/stretches/stretch.html', id=item_id, stretch=stretch, next_url=next_url)

@app.route('/stretches/back_stretches')
def back_stretches():
    return render_template('learn/stretches/back_stretches.html', back_stretchlist=back_stretchlist)

@app.route('/quiz/<int:item_id>')
def quiz(item_id):
    if item_id == 2:
        return render_template('quiz/drag_drop.html', id=item_id)
    else:
        return render_template('quiz/mc.html', id=item_id)


@app.route('/quiz/results/<int:item_id>')
def results(item_id):
    return render_template('quiz/results.html', id=item_id)


if __name__ == '__main__':
    app.run(debug=True)
