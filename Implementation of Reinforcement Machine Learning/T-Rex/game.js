let players = [];
var Population = 1000;
let allPlayers = [];
var next;
var n=0;
var score = 0;
var fpss = 0;

let obstacles = [];

var counter = 0;
// var slider = document.getElementById("myRange");
// var output = document.getElementById("demo");
//output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
// slider.oninput = function() {
//   output.innerHTML = this.value;
//   fpss = this.value;
// }
function setup() {
    createCanvas(1600, 800);
    next = document.getElementById("tttt");
    for (let i = 0; i < Population; i++) {
        players[i] = new Player();
    }
    

}

// function mousePressed() {
//     player.jump();
// }

// function keyPressed() {
//     if (key == " ")
//         player.jump();
// }

function draw() {
    // if (frameCount % 60 == 0) {
    //     if (random(1) < 0.5) {
    //         obstacles.push(new Obstacle());
    //     }
    // }
   // frameRate(1200);
    console.log(fpss);
    counter += random(17);
    if (random(500, 900) <= counter) {
        obstacles.push(new Obstacle());
        counter = 0;
    }


    if (frameCount % 30 == 0) {
        updateScore();
        console.log("Score is " + score);
    }

    background(245);
    line(0, 751, 1600, 751);
    for (let i of obstacles) {
        i.move();
        i.show();
        if (i.isOut()) {
            obstacles.splice(i, 1);
        }
        if (random(1) > 0.1) {
            i.wide = 80;
        }
        for (let j = 0; j <= players.length - 1; j++) {
            if (players[j].collides(i)) {
                //noLoop();
                allPlayers.push(players.splice(j, 1)[0]);
            }
        }
    }
    for (let player of players) {
        player.show();
        player.move();
        if (obstacles.length) {
            player.think(obstacles);
        }
    }


    if (players.length == 0) {
        score = 0;
        n +=1;
        next.textContent ="Generation: "+ n;
        nextgeneration();
        obstacles = [];
        console.log("called");

    }
    
}

function updateScore() {
    score += 1;
}