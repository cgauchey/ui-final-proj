var correctSVG =
'<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="green" style="float:right; margin-top: 2px;" viewBox="0 0 24 24"><path d="M20.285 2l-11.285 11.567-5.286-5.011-3.714 3.716 9 8.728 15-15.285z"/></svg>';
var wrongSVG =
'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="rgb(182, 24, 24)" style="float:right; margin-top: 2px;" viewBox="0 0 24 24"><path d="M23 20.168l-8.185-8.187 8.185-8.174-2.832-2.807-8.182 8.179-8.176-8.179-2.81 2.81 8.186 8.196-8.186 8.184 2.81 2.81 8.203-8.192 8.18 8.192z"/></svg>';


function save_answer(answer) {
    var answerData = {
      quizId: quizId,
      answer: answer
    };

    $.ajax({
      url: "/save_answer",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(answerData),
      success: function (response) {
        window.location.href = "/quiz/results/" + quizId;

      },
      error: function () {
        console.log("Error saving results");
      },
    });
  }

  function next_page() {
      window.location.href = "/quiz/" + quizNext;
  }

  function back_page(){
    window.location.href = '/quiz/results/' + (quizId-1)
  }

  $(document).ready(function () {

    $("#next").click(function () {
      next_page();
    });

    $("#back").click(function () {
      back_page();
    });
  });