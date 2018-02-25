function updateBoard(boardState) {

}

function sendRequest() {
  let player = document.getElementById("player")
  let letter = player[player.length]
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() { 
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          console.log(xmlHttp.responseText)
          updateBoard(xmlHttp.responseText)
  }
  xmlHttp.open("GET", "/update/"+letter, true); // true for asynchronous 
  xmlHttp.send(null);
}

setInterval(sendRequest(),1000)