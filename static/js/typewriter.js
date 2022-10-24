var typeWriter = document.getElementsByClassName('preview-typewriter')[0];

var typewriter = new Typewriter(typeWriter, {
  loop: true,
  delay: 75,
  deleteSpeed: 300,
});

typewriter
  .pauseFor(500)
  .typeString('Data Analyst')
  .pauseFor(1000)
  .deleteAll()
  .typeString('Software Engineer')
  .pauseFor(1000)
  .deleteAll()
  .typeString('Penetration Tester')
  .pauseFor(1000)
  .deleteAll()
  .typeString('Graduate Student')
  .pauseFor(1000)
  .deleteAll()
  .start();
