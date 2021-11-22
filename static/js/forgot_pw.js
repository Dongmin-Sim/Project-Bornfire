$("#button-addon2").click(function () {
  const email_input = $("#context").val();

  $.ajax({
    type: "POST",
    url: "/forgot-pw",
    data: JSON.stringify({ User_email: email_input }),
    dataType: "JSON",
    contentType: "application/json",
    success: function (res) {
      $(".pw-container").removeClass("pw-container");
      const question = Object.keys(res)[0];
      answer = Object.values(res)[0];
      // 전역 변수 지정
      $(".card-title").html(question);
    },
    error: function (request, status, error) {
      alert("ajax 통신 실패");
      alert(error);
    },
  });
});

$("#answer-btn").click(function () {
  const user_answer = $("#user_answer").val().replace(/(\s*)/g, "");

  if (answer == user_answer) {
    $(".change-form").removeClass("change-form");
  } else {
    alert("답이 틀렸습니다. 다시 한번 입력해주세요.");
  }
});
