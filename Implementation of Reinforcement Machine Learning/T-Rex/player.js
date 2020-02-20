class Player {

    constructor(brain) {
        this.ground = 50;
        this.x = 200;
        this.y = height - this.ground - this.ground;
        this.vY = 0;
        if(brain){
            this.brain = brain.copy();
        }
        else{
        this.brain = new NeuralNetwork(3, 2, 2);}
        this.gravityY = 1.5;
        this.points=0;
        this.fitness=0;

    }

    jump() {
        if (this.y == height - 100)
            this.vY = -25;
    }
    mutate(){
        this.brain.mutate(0.1);
    }

    move() {
        this.points++;
        this.y += this.vY;
        this.vY += this.gravityY;
        this.y = constrain(this.y, 0, height - this.ground - this.ground);
    }
    think(obstacles) {
        let inputs = [];
        inputs[0] = this.y/height;
        inputs[1] = obstacles[0].y/height;
        inputs[2] = obstacles[0].x/width;


        let output = this.brain.predict(inputs);
        if (output[0] > output[1]) {
            this.jump();
        }
    }

    collides(obstacle) {
        if(collideRectRect(this.x,this.y,50,50,obstacle.x,obstacle.y,50,100)){
            return true;
        }
        else return false;
    }

    show() {
        rect(this.x, this.y, 50, 50);
        fill(180);
    }
}