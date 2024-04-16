questions = {
    1: {
        "id": 1,
        "type": "mcq",
        "question": "Which posture problem is the person in the image suffering from?",
        "choices": [
            "Forward Head Posture",
            "Rounded Shoulders",
            "Lower Crossed Syndrome",
        ],
        "image": "https://b907749.smushcdn.com/907749/wp-content/uploads/2022/05/body-posture-1024x539-1.jpg?lossy=2&strip=1&webp=1",
        "answer": "Forward Head Posture",  # do it this way so it's possible to scramble up the mcq order
        "next": 2,
    },
    2: {
        "id": 2,
        "type": "dragdrop",
        "question": "Drag each description to its corresponding term.",
        "answer": {
            "Muscles": "Supports and stabilizes the skeletal system",
            "Spine": "Comprised of vertebrae and discs",
            "Joints": "Allow movement and contribute to posture",
            "Connective Tissue": "Ligaments and tendons connect bones and muscles",
        },
        "next": 3,
    },
    3: {
        "id": 3,
        "type": "mcq",
        "question": "Which posture problem does this stretch target?",
        "choices": ["Lower Crossed Syndrome", "Forward Head Syndrome"],
        "image": "https://images.squarespace-cdn.com/content/v1/5a620a85d55b41e7233c5243/ae25b65f-ef76-40f5-8091-76cb07bdad9b/PleasantTerrificBettong-size_restricted.gif",
        "answer": "Forward Head Syndrome",
        "next": 4,
    },
    4: {
        "id": 4,
        "type": "mcq",
        "question": "Which of the following is not a component of posture?",
        "choices": ["Muscle", "Connective Tissues", "Cardiovascular System", "Spine"],
        "image": "",
        "answer": "Cardiovascular System",
        "next": 5,
    },
    5: {
        "id": 5,
        "type": "dragdrop",
        "question": "Drag each muscle to its corresponding stretch.",
        "answer": {
            "Thoracic Extension Stretch": "Upper Back",
            "Locust Pose": "Lower Back",
            "Thoracic rotation": "Both Upper and Lower Back",
        },
        "next": 6,
    },
    6: {
        "id": 6,
        "type": "mcq",
        "question": "Which stretch is demonstrated in the image on the right?",
        "choices": ["Cat Cow", "Hip Flexor Lunge", "Floor Cobra", "Wall Angel"],
        "image": "https://pic1.zhimg.com/80/v2-e439c01a3cc3aeb7833ebc523a26af1c_720w.webp",
        "answer": "Floor Cobra",
        "next": 7,
    },
    7: {
        "id": 7,
        "type": "dragdrop",
        "question": "Drag each stretch to its corresponding muscle",
        "answer": {
            "Upper Back": "Shoulder Stretch",
            "Lower Back": "Cat Cow",
            "Both Upper and Lower Back": "Dynamic Camel",
        },
        "next": 8,
    },
    8: {
        "id": 8,
        "type": "mcq",
        "question": "Which stretch is demonstrated in the image on the right?",
        "choices": ["Cat Cow", "Angel Wings", "Cat Cow", "Wall Angel"],
        "image": "https://media.post.rvohealth.io/wp-content/uploads/sites/2/2021/04/GRT-1.7.Wall-Angels.gif",
        "answer": "Wall Angel",
        "next": 9,
    },
    9: {
        "id": 9,
        "type": "mcq",
        "question": "If you are experiencing upper back pain, which stretch will be the most effective?",
        "choices": ["Hamstring Stretch", "Thoracic Extension Stretch", "Hip Flexor Stretch", "Pectoral Stretch"],
        "image": "https://www.microspinemd.com/wp-content/uploads/2019/10/upper-back-pain.png",
        "answer": "Wall Angel",
        "next": "end",
    },


}
