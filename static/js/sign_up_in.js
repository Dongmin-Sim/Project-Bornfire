// 슬라이드
const signUpButton = document.getElementById("signUp");
const signInButton = document.getElementById("signIn");
const container = document.getElementById("logincontainer");

signUpButton.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

signInButton.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

// input validation
const form = document.getElementById("form");
const email = document.getElementById("email");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");
const question = document.getElementById("question");
const user_answer = document.getElementById("user_answer");

// Check passwords match
function checkPasswordsMatch(input1, input2) {
  if (input1.value !== input2.value) {
    alert("비밀번호가 일치하지 않습니다.");
    return false;
  } else {
    return true;
  }
}

// Event listeners
form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (user_answer.value.length == 0 || question.value.length == 0) {
    return alert("비밀번호 찾기 질문과 답을 입력해주세요 🔥");
  }

  if (checkPasswordsMatch(password, password2) == true) {
    alert("회원가입이 완료되었습니다 🔥");

    form.submit();
  }
});
