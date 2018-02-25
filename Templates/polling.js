function updateBoard(boardState) {
  document.getElementById("board")
}

function sendRequest() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() { 
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          console.log(xmlHttp.responseText)
          updateBoard(xmlHttp.responseText)
  }
  xmlHttp.open("GET", "/update", true); // true for asynchronous 
  xmlHttp.send(null);
}

setInterval(sendRequest,1000)