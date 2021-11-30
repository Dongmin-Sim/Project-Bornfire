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
      alert("아이디를 찾을 수 없습니다 🤦‍♂️");
    },
  });
});

$("#answer-btn").click(function () {
  const user_answer = $("#user_answer").val().replace(/(\s*)/g, "");

  if (answer == user_answer) {
    $(".change-form").removeClass("change-form");
  } else {
    alert("답이 틀렸습니다. 다시 한번 입력해주세요 🤦‍♂️");
  }
});

$("#change-pw-btn").click(function (e) {
  e.preventDefault();
  const pw = $("#floatingInput").val();
  const pw2 = $("#floatingPassword").val();
  const form = $("#pw-change-form");

  if (checkPasswordsMatch(pw, pw2) == true) {
    form.submit();
  }
});

function checkPasswordsMatch(input1, input2) {
  if (input1 !== input2) {
    alert("비밀번호가 일치하지 않습니다 🤦‍♂️");
    return false;
  } else {
    return true;
  }
}
