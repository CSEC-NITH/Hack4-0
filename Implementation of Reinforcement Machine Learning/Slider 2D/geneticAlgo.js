function nextgeneration() {
    calculatefitness();

    for (let i = 0; i < Population; i++) {
        realPlayers.push(pick());
    }
    deadPlayers = [];
}
//clone
function pick() {
    let maxScore = deadPlayers[0].points;
    let minScore = deadPlayers[0].points;
    for (i of deadPlayers) {
        if (maxScore <= i.points)
            maxScore = i.points;
        if (minScore >= i.points)
            minScore = i.points;
    }
    // let index = 0;
    // let r = random(1);
    // while (r > 0) {

    //     r -= deadPlayers[index].fitness;
    //     index += 1;
    // }

    // index -= 1;

    while (1) {
        randm = Math.floor(Math.random() * Population);
        var c = deadPlayers[randm]
        if (c.points >= ( maxScore + minScore) / 2) {
            c = new Player(c.brain);
            c.x = random(1) * width;
            c.brain.mutate(0.1);
            return c;
        }

    }

    // let pl = deadPlayers[index];//something
    // let c = new Player(pl.brain);
    // c.x = random(1) * width;
    // c.brain.mutate(0.1);
    // return c;
}

function calculatefitness() {
    let sum = 0;
    for (let player of deadPlayers) {
        sum += player.points;
    }

    for (let i of deadPlayers) {
        i.fitness = i.points / sum;
        i.fitness = i.fitness * 100;
    }
}