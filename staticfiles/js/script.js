// Change Theme
let theme = localStorage.getItem('theme');

if (theme == null) {
  setTheme('blue');
} else {
  setTheme(theme);
}

let themeDots = document.getElementsByClassName('theme-dot');

for (var i = 0; themeDots.length > i; i++) {
  themeDots[i].addEventListener('click', function () {
    let mode = this.dataset.mode;
    console.log('Option clicked', mode);
    setTheme(mode);
  });
}

// Function to set page theme
function setTheme(mode) {
  if (mode == 'light') {
    document.getElementById('theme-style').href = '/staticfiles/css/light.css';
  }

  if (mode == 'blue') {
    document.getElementById('theme-style').href = '/staticfiles/css/blue.css';
  }

  if (mode == 'green') {
    document.getElementById('theme-style').href = '/staticfiles/css/green.css';
  }

  if (mode == 'purple') {
    document.getElementById('theme-style').href = '/staticfiles/css/purple.css';
  }

  localStorage.setItem('theme', mode);
}

// Function to reveal section
function reveal() {
  var reveals = document.querySelectorAll('.reveal');
  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;
    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add('active');
    } else {
      reveals[i].classList.remove('active');
    }
  }
}

window.addEventListener('scroll', reveal);
reveal();
