<!DOCTYPE html>
<html>
  <head>
    <title>Robot_1</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0">
    <script src="js/script.js"></script>
    <script>
window.addEventListener('load', initialize_page);

var host = location.hostname;         
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
    var theUrl = "http://"+host+":8080/action="+actionStr;
    var xmlHttp = new XMLHttpRequest();
    console.log(theUrl);
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {};
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
};
    </script>
    <style>
#move_buttons {
    width: 50vh;
    min-width: 110vw;
    margin-left: -25vh; /*half the width to correctly center*/
    position: fixed;
    bottom: 1vh;
    left: 50%;
}

.move_icon {  /* the icons*/
    height: 15vh;
    max-height: 33vw;
    width: 15vh;
    max-width: 33vw;            
}

.buttons_row * {display: inline;}
.left {margin: auto auto auto 0;}
.center {margin: auto;}
.right {margin: auto 0 auto auto;}

#arrow_left_up {-webkit-transform: rotate(45deg); transform: rotate(45deg);}
#arrow_up {-webkit-transform: rotate(90deg); transform: rotate(90deg);}
#arrow_right_up {-webkit-transform: rotate(135deg); transform: rotate(135deg);}
#arrow_left_rotate {-webkit-transform: scaleX(-1); transform: scaleX(-1);}
#arrow_right_rotate {-webkit-transform: rotate(0deg); transform: rotate(0deg);}
#arrow_left_down {-webkit-transform: rotate(315deg); transform: rotate(315deg);}
#arrow_down {-webkit-transform: rotate(270deg); transform: rotate(270deg);}
#arrow_right_down {-webkit-transform: rotate(225deg); transform: rotate(225deg);}

mjpeg_dest {
    width: auto;
    max-width: 100vw;
    height: 50vh;
    object-fit: scale-down;
    margin: 0 auto;
    padding: 0;
    display: block;
}
    </style>
    
	<link rel="stylesheet" href="css/style_minified.css" />
  </head>
  <body onload="setTimeout('init(0,25,1);', 100);">
    <center>
      <div><img id="mjpeg_dest" /></div>
    </center>

    <div id="move_buttons">
      <div id="forwards_buttons" class="buttons_row">
        <img id="arrow_left_up" class="move_icon left" src="image/basic_arrow.png">
        <img id="arrow_up"  class="move_icon center" src="image/basic_arrow.png">
        <img id="arrow_right_up" class="move_icon right" src="image/basic_arrow.png">
      </div>
      <div id="rotate_buttons"  class="buttons_row">
        <img id="arrow_left_rotate" class="move_icon left" src="image/arrow_semi_circle.png">
 		<img id="stop" class="move_icon center" src="image/stop.png">
        <img id="arrow_right_rotate" class="move_icon right" src="image/arrow_semi_circle.png">
	  </div>
  	  <div id="backwards_buttons"  class="buttons_row">
        <img id="arrow_left_down" class="move_icon left" src="image/basic_arrow.png">
 		<img id="arrow_down" class="move_icon center" src="image/basic_arrow.png">
        <img id="arrow_right_down" class="move_icon right" src="image/basic_arrow.png">
	  </div>
    </div>


 </body>
</html>
