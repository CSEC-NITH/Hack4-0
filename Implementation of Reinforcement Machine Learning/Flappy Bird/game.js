let player;

let players =[];
let total =1000;
let allPlayers=[];
var n=0;
var next;

var score =0;


let sum=0;

let obstacles = [];

function setup() {
    createCanvas(1600, 800);
    next = document.getElementById("tttt");
    for (let i=0 ; i<total;i++) {
        players[i] = new Player();  
    }
 
    
    
}

//function mousePressed() {
//    player.fly();
//}

//function keyPressed() {
//    if (key == " ")
//        player.fly();
//}

function draw() {
    if (random(1) < 0.6) {
        if (frameCount % 60 == 0) {
            var b = new Obstacle();
            let newTopBoxHeight = random(0, 2 * (height / 3));
            let newBottomBoxHeight = height - 200 - newTopBoxHeight;

            b.bottomBoxHeight = newBottomBoxHeight;
            b.topBoxHeight = newTopBoxHeight;

            obstacles.push(b);
        }
    }

    if (frameCount % 30 == 0) {
        score += 1;
        
    }

    updateScore(score);


    background(125);

    for (let i of obstacles) {
        i.show();
        i.move();
        for (let j=0;j<players.length;j++) {
            if (players[j].collides(i)) {
                allPlayers.push(players.splice(j, 1));
                
                
            }
            
        }
        
    }

    for (let player of players)
    {
        
    player.show();
    player.move();
    
    if (obstacles.length) {
        player.think(obstacles);
    }
    }
    if (players.length ==0) {
        obstacles=[];
        n +=1;
        next.textContent = "Generation"+n;
        nextgeneration();  
       
      }

    
}



function updateScore(sc) {
    // The text() function needs three parameters:
    // the text to draw, the horizontal position,
    // and the vertical position
    fill(10);
    text('Current High Score', 50, 50);
}
