function nextgeneration(){



    calculatefitness();

    for(let i=0;i<Population;i++){
        players[i]= pick();
    }
    allPlayers=[];
}
//clone
function pick() {
    let index = 0;
    let r = random(1);
    
    while (r > 0) {
      r -= allPlayers[index].fitness;
      index += 1;
    }
    index -= 1;

    let pl = allPlayers[index];//something
    let c= new Player(pl.brain);
      c.brain.mutate(0.1);
        return c;
  }

function calculatefitness(){
    let sum = 0;
    for(let player of allPlayers){
        sum += player.points;

    }


    for(let i of allPlayers){
        i.fitness = i.points/sum;
     //   i.fitness=i.fitness*100;


    }



}