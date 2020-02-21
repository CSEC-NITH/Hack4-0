class Obstacle {

  constructor(type) {
    this.rightBlockWidth = 250;
    this.leftBlockWidth = width - 650;
    this.blockY = -50;
    this.type = random(type-1, type);
  }

  move() {
    this.rightX = width - this.rightBlockWidth;
    this.rightY = width - this.rightBlockWidth;
    this.blockY += 5;
  }

  show() {
    fill(0, 244, 0);
    if (this.type <= 1) {
      rect(0, this.blockY, this.leftBlockWidth, 50);
      rect(width-250, this.blockY, this.rightBlockWidth, 50);
    }
    else if (this.type <= 2){
      rect(300, this.blockY, width-300, 50);
    }
    else if(this.type <= 3){
      rect(0, this.blockY, width-400, 50);
    }
    else if(this.type <= 4){
      rect(400, this.blockY, width-400, 50);
    }
  }

  isOut(){
    if(this.blockY > height + 50){
     return true;
    }
  }
}