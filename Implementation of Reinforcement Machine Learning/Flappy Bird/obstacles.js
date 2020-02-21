class Obstacle {

  constructor() {
    this.topBoxHeight = height/2 - 100;
    this.bottomBoxHeight = height/2 +100;
    this.topY = 0;
    this.boxX = width;
    this.bottomY = 0;
  }

  move() {
    this.boxX -= 8;
    this.bottomY = height - this.bottomBoxHeight;
  }

  show() {
    fill(0,244,0);
    rect(this.boxX, this.topY, 50, this.topBoxHeight);
    rect(this.boxX, this.bottomY, 50, this.bottomBoxHeight  );
  }

}