var score = 0;

var gen = 1;

var Population = 500;

let obstacles = [];

var realPlayers = [];

var deadPlayers = [];

function setup() {
    createCanvas(1600, 800);
    console.log("Generation: " + gen);
    for (let i = 0; i < Population; i++) {
        let player = new Player();
        player.x = i * (width / Population);
        realPlayers.push(player);
    }
}

// function mousePressed() {
//     player.moveRight();
// }

// var slider = document.getElementById("myRange");
// var output = document.getElementById("demo");
// output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
// slider.oninput = function () {
//     output.innerHTML = this.value;
// }


// function keyPressed() {
//     if (key == "A" || key.keyCode == "65")
//         player.moveLeft();
//     else if (key == "d" || key == "D")
//         player.moveRight();
// }

function draw() {
    if (random(1) < 0.7) {
        if (frameCount % 100 == 0) {
            var b = new Obstacle(random(1, 5));
            obstacles.push(b);
        }
    }

    if (frameCount % 30 == 0) {
        score += 1;
        console.log("Score is " + score);
    }

    background(125);

    for (let i of obstacles) {
        i.show();
        i.move();
        if (i.isOut())
            obstacles.splice(i, 1);
        for (let j = 0; j < realPlayers.length; j++) {
            if (realPlayers[j].collides(i)) {
                deadPlayers.push(realPlayers.splice(j, 1)[0]);
            }
        }
    }
    for (i of realPlayers) {
        i.show();
        i.move();
        if (obstacles.length)
            i.think(obstacles);
    }
    if (realPlayers.length == 0) {
        restart();
    }
}

function restart() {
    score = 0;
    nextgeneration();
    gen++;
    console.log("Generation: " + gen);
    obstacles = [];

}