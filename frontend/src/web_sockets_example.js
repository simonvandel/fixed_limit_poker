let socket = new WebSocket("ws://127.0.0.1:6789");
let displayConsole = [];

socket.onopen = function(event) {
    let outgoingMessage = "hello from the front-end"
    socket.send(outgoingMessage);
}

socket.onmessage = function (event) {
    let message = event.data;

    displayConsole.push(message);
    var actionList = document.getElementById("action-list");
    actionList.children[0].innerHTML = "<li>" + displayConsole[displayConsole.length - 1] + "</li>" + actionList.children[0].innerHTML;

    // Must send a message back ...
    socket.send("ack")
}
