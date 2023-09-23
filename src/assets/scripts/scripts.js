var check = localStorage.setItem("isChecked", "0");

function changeFont() {
  const li = document.querySelectorAll("li");
  const p = document.querySelectorAll("p");

  var decider = document.getElementById('changefont');

  if (decider.checked || check == "1") {
    li.forEach(element => {
      element.style.fontFamily = "Open Dyslexic";
      element.style.fontSize = "1.1em";
    });
    p.forEach(element => {
      element.style.fontFamily = "Open Dyslexic";
      element.style.fontSize = "1.1em";
    });
    decider.checked = true;
    localStorage.setItem("isChecked", "1");
  } else {
    li.forEach(element => {
      element.style.fontFamily = "Warung Kopi";
      element.style.fontSize = "1.3em";
    });
    p.forEach(element => {
      element.style.fontFamily = "Warung Kopi";
      element.style.fontSize = "1.3em";
    });
  }
}
