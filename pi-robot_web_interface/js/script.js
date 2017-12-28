window.addEventListener('load', initialize_page);
                  
var forward_left
var forward
var forward_right
var rotate_left
var stop
var rotate_right
var backward_left
var backward
var backward_right

function initialize_page(){
    console.log('initializing page');
    var dom_ids = ['arrow_left_up', 'arrow_up', 'arrow_right_up',
                   'arrow_left_rotate', 'stop', 'arrow_right_rotate',
                   'arrow_left_down', 'arrow_down', 'arrow_right_down'];
    var action_ids = ['forward_left', 'forward', 'forward_right',
                      'rotate_left', 'stop', 'rotate_right',
                      'backward_left', 'backward', 'backward_right'];
    var intervalIDs = [forward_left, forward, forward_right,
                       rotate_left, stop, rotate_right,
                       backward_left, backward, backward_right];

    for (let i = 0; i < 9; i++) {
        console.log(i + ' initiating DOM ' + dom_ids[i] + ' with action ' + action_ids[i]);
        console.log(dom_ids[i], action_ids[i])
        var mydom = document.getElementById(dom_ids[i]);
        mydom.addEventListener('touchstart', function(){intervalIDs[i] = setInterval(action, 500, action_ids[i])});
        mydom.addEventListener('touchend', function(){clearInterval(intervalIDs[i])});
        mydom.addEventListener('click', function(){action(action_ids[i])});
    };
    console.log('initialization complete');
};


// stops a context menu popup on a long press
window.oncontextmenu = function(event) {
     event.preventDefault();
     event.stopPropagation();
     return false;
};


function action(actionStr){
    var theUrl = "action="+actionStr;
    var xmlHttp = new XMLHttpRequest();
    console.log(theUrl);
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {};
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
};

