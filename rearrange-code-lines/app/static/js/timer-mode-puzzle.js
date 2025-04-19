var interval;
//let totalSeconds = {{GAME_DURATION}}
console.log("Total:" + totalSeconds);
let startTime = localStorage.getItem('startTime');
let currentTime = localStorage.getItem('currentTime');
let targetTime = localStorage.getItem('targetTime');
let endTime = localStorage.getItem('endTime')
let endTimeTaken = localStorage.getItem('endTimeTaken');
let timer = document.getElementById('timer');

if (targetTime == null && currentTime == null) {
  currentTime = new Date();
  targetTime = new Date(currentTime.getTime() + (totalSeconds * 1000));
  startTime = currentTime; // Set start time here
  localStorage.setItem('startTime', startTime); // Store start time
  localStorage.setItem('currentTime', currentTime);
  localStorage.setItem('targetTime', targetTime);
}
else {
  currentTime = new Date(currentTime);
  targetTime = new Date(targetTime);
  startTime = new Date(startTime); // Retrieve start time
}

if (!checkComplete()) {
  interval = setInterval(checkComplete, 1000);
}

function checkComplete() {
  if (endTime != undefined && endTimeTaken != undefined) {
    document.getElementById('timeOutInput').value = true;
    localStorage.clear();
    document.getElementById('endGameForm').submit()
  }
  else {
    if (currentTime > targetTime) {
      clearInterval(interval);
      if (endTime == null || endTime == undefined) {
        endTime = currentTime;
        endTimeTaken = localStorage.getItem('timeTaken')
        localStorage.setItem('endTime', endTime);
        localStorage.setItem('endTimeTaken', endTimeTaken)
        document.getElementById('timeOutInput').value = true;
        localStorage.clear();
        document.getElementById('endGameForm').submit()
      }
    }
    else {
      currentTime = new Date();
      var time_in_ms = currentTime.getTime() - startTime.getTime();
      var time_in_s = parseInt(time_in_ms / 1000);
      var minutes = parseInt(time_in_s / 60).toString().padStart(2, '0');
      var seconds = parseInt(time_in_s % 60).toString().padStart(2, '0');
      var time_text = minutes + ":" + seconds;
      timer.innerHTML = "<h2>" + time_text + "</h2>";
      localStorage.setItem('timeTaken', time_text);
    }
  }
}

document.onbeforeunload = function () {
  localStorage.setItem('currentTime', currentTime);
};