document.cookie = "fontboxchecked=0; path=/";
let fontbox = document.cookie;

function changeFont() {
  var decider = document.getElementById('changefont');
  const li = document.querySelectorAll("li");
  const p = document.querySelectorAll("p");

  if (decider.checked || fontbox.includes("fontboxchecked=1")) {
    li.forEach(element => {
      element.style.fontFamily = "Open Dyslexic";
      element.style.fontSize = "1.3em";
    });
    p.forEach(element => {
      element.style.fontFamily = "Open Dyslexic";
      element.style.fontSize = "1.3em";
    });
    document.cookie = "fontboxchecked=1; path=/";
  } else if (!decider.checked) {
    li.forEach(element => {
      element.style.fontFamily = "Warung Kopi";
      element.style.fontSize = "1.6em";
    });
    p.forEach(element => {
      element.style.fontFamily = "Warung Kopi";
      element.style.fontSize = "1.6em";
    });
  }
}

window.onload = changeFont();
