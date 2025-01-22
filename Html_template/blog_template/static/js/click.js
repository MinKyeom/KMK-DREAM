function is_checked() {

  // 1. checkbox element를 찾습니다.
  const checkbox = document.getElementById('my_checkbox');

  // 2. checked 속성을 체크합니다.
  const is_checked = checkbox.checked;

  // 3. 결과를 출력합니다.
  document.getElementById('result').innerText = is_checked;

}