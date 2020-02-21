class Obstacle {
    constructor() {
        this.x = width;
        this.y = height - 150;
      }
    
      move() {
        this.x -= 8;
      }
    
      show() {
        rect(this.x, this.y, 50, 100);
      }


      isOut() {
        if (this.x <= -50) {
          return true;
        }
        else{
          return false;
        }
      }
}