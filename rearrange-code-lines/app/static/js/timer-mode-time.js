var interval;
let startTime = localStorage.getItem('startTime');
let currentTime = localStorage.getItem('currentTime');
let endTimeTaken = localStorage.getItem('endTimeTaken');
let timer = document.getElementById('timer');

if (currentTime == null) {
  currentTime = new Date();
  startTime = currentTime; // Set start time here
  localStorage.setItem('startTime', startTime); // Store start time
  localStorage.setItem('currentTime', currentTime);
}
else {
  currentTime = new Date(currentTime);
  startTime = new Date(startTime);
}

if (!checkComplete()) {
  interval = setInterval(checkComplete, 1000);
}

function checkComplete() {
  currentTime = new Date();
  var time_in_ms = currentTime.getTime() - startTime.getTime();
  var time_in_s = parseInt(time_in_ms / 1000);
  var minutes = parseInt(time_in_s / 60).toString().padStart(2, '0');
  var seconds = parseInt(time_in_s % 60).toString().padStart(2, '0');
  var time_text = minutes + ":" + seconds;
  timer.innerHTML = "<h2>" + time_text + "</h2>";
  localStorage.setItem('timeTaken', time_text);
}

document.onbeforeunload = function () {
  localStorage.setItem('currentTime', currentTime);
};