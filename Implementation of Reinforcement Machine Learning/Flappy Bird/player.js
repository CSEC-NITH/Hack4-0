class Player {

    constructor(brain) {
        this.ground = height;
        this.x = 100;
        this.y = height / 2;
        this.force = 0;
        this.gravityY = 0.5;
        if(brain){
            this.brain = brain.copy();
        }else
        this.brain = new NeuralNetwork(3, 3, 2);
        
    }

    fly() {
        this.force = -12;
    }

    move() {
        this.y += this.force;
        this.force += this.gravityY;
        this.y = constrain(this.y, 25, height - 25);
    }

    think(obstacles) {

        let closest = obstacles[0];
        // console.log(this.y/height);
        // console.log(closest.topBoxHeight/height);
        // console.log(closest.boxX/(width-300));
       let inputs = [];
        inputs[0] = this.y/height;
        inputs[1] = closest.topBoxHeight/height;
        inputs[2] = closest.boxX/width;
        


        // let inputs =[1.0, 0.1, 0.1];
        let output = this.brain.predict(inputs);
        
        if (output[0] > output[1]) {
            this.fly();
            
        }
    }

    collides(obstacle) {
        if(collideRectCircle(obstacle.boxX, obstacle.topY, 50, obstacle.topBoxHeight, this.x, this.y, 50 ))
            return true;
        if(collideRectCircle(obstacle.boxX, obstacle.bottomY, 50, obstacle.bottomBoxHeight, this.x, this.y, 50 ))
        return true;

    }

    show() {
        fill(255, 170, 29);
        ellipse(this.x, this.y, 50, 50);
    }
}