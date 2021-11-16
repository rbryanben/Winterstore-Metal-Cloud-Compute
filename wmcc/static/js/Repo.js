//API CALLS
const CREATE_INSTANCE_API = "/console/createInstance" 


//Creates Server  
function createServer(server_name,callback){
    //xhr request to post json data with the server name, username and password
    var xhr = new XMLHttpRequest();
    xhr.open("POST", CREATE_INSTANCE_API, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            callback()
        }
    };
    var data = JSON.stringify({
        "server_name": server_name,
    });
    xhr.send(data);
}


//get instances 
function getInstances(callbackFunction){
    var oReq = new XMLHttpRequest();
    oReq.open("GET", "/console/getInstances");
    oReq.addEventListener("load", function(){
        callbackFunction(this.responseText)
    });
    oReq.send()
}

// Socket Functions
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/server/'
    + 'cloud'
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    window.location.reload();
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

