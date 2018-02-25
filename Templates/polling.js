function updateBoard(boardState) {
  let gameOver = boardState[1]
  let board = document.getElementById("board")
  let elements = board.children
  let count = 0;
  boardState[0].forEach(row => {
    for(let i=0;i<3;i++) {
      elements[count].innerHTML = row[i]
      count++
    }
  });
}

function sendRequest() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() { 
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          //console.log(JSON.parse(xmlHttp.responseText))
          updateBoard(JSON.parse(xmlHttp.responseText))
  }
  xmlHttp.open("GET", "/update", true); // true for asynchronous 
  xmlHttp.send(null);
}

setInterval(sendRequest,1000)