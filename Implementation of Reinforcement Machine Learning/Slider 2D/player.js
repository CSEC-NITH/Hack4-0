class Player {

    constructor(brain) {
        this.ground = height;
        this.x = width / 2;
        this.y = height - 100;
        this.forceX = 0;
        this.friction = 0.5;
        if (brain) {
            this.brain = brain.copy();
        }
        else {
            this.brain = new NeuralNetwork(4, 8, 2);
        }
        this.points = 0;
        this.fitness = 0;
        this.flag = 1;
    }

    think(obstacles) {
        let inputs = [];

        inputs[0] = this.x / width;
        if (this.flag) {
            inputs[1] = obstacles[0].blockY / height;
            if(obstacles[0].blockY - this.y == 0 )
                this.flag = 0;
        }
        else {
            if(obstacles[0].blockY - this.y > 98 || obstacles.length < 2){
                this.flag = 1;
                return;
            }
            inputs[1] = obstacles[1].blockY / height;
            
        }
        inputs[0] = this.x / width;
        inputs[2] = 0.5;
        inputs[3] = 0.5;
        this.type = obstacles[0].type;
        if (this.type <= 1) {
            inputs[2] = obstacles[0].leftBlockWidth / width;
            inputs[3] = 1 - obstacles.rightBlockWidth / width;
        }
        else if (this.type <= 2) {
            inputs[2] = 0 / width;
            inputs[3] = 300 / width;
        }
        else if (this.type <= 3) {
            inputs[2] = 1 - 300 / width;
            inputs[3] = 1;
        }
        else if (this.type <= 4) {
            inputs[2] = 0;
            inputs[3] = 400 / width;
        }
        let output = this.brain.predict(inputs);
        if (output[0] >= output[1]) {
            this.moveRight();
        }
        else {
            this.moveLeft();
        }
    }

    moveRight() {
        if (this.forceX > 5)
            this.forceX += 5;
        else
            this.forceX = 10;
    }

    moveLeft() {
        if (this.forceX < -5)
            this.forceX -= 5;
        else
            this.forceX = -10;
    }

    move() {
        this.x += this.forceX;;
        if (this.forceX > 0) {
            this.forceX -= this.friction;
        }
        else if (this.forceX < 0) {
            this.forceX += this.friction;
        }
        // if (this.forceX < 0.5 && this.forceX > -0.5)
        //     this.forceX = 0;
        // if (this.forceY < 0.5 && this.forceY > -0.5)
        //     this.forceY = 0;
        this.x = constrain(this.x, 0, width - 50);
    }

    collides(obstacle) {
        if ((this.y > obstacle.blockY && this.y < obstacle.blockY + 50) || (this.y + 50 > obstacle.blockY && this.y + 50 < obstacle.blockY + 50)) {
            if (obstacle.type <= 1) {
                if (this.x <= obstacle.leftBlockWidth || this.x + 50 >= width - obstacle.rightBlockWidth)
                    return true;
            }
            else if (obstacle.type <= 2) {
                if (this.x + 50 >= 300)
                    return true;
            }
            else if (obstacle.type <= 3) {
                if (this.x <= width - 400)
                    return true;
            }
            else if (obstacle.type <= 4) {
                if (this.x + 50 >= 400)
                    return true;
            }
        }
        else
            return false;
    }

    show() {
        fill(255, 170, 29);
        rect(this.x, this.y, 50, 50);
    }
}