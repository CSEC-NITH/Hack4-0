var arr=[];
alert("WELCOME TO THE GAME");        
  var myVar,r,g,b,colors=[];
function generatorcolor(){
r=Math.floor(Math.random()*256);
g = Math.floor(Math.random() * 256);
b = Math.floor(Math.random() * 256);

colors = [
    "rgb(" + (r) + ", " + (g) + ", " + (b) + ")",
    "rgb(" + (r+40) + ", " + (g) + ", " + (b+20) + ")",
    "rgb(" + (r-30) + ", " + (g+20) + ", " + (b) + ")",
    "rgb(" + (r-30) + ", " + (g-30) + ", " + (b-30) + ")",
    "rgb(" + (r+20) + ", " + (g-30) + ", " + (b+40) + ")",
    "rgb(" + (r) + ", " + (g+10) + ", " + (b+30) + ")"
//    "rgb(210,120,129)",
//    "rgb(110,220,119)",
//    "rgb(10,220,229)",
//    "rgb(10,20,129)"
]
}
generatorcolor();
var count=0,timer=25,delay=200,round=0,score=0,best=200,i=0;
var squares = document.querySelectorAll(".dot");
 var pickedcolor;   
for(var i=0;i<squares.length;i++)
{

    squares[i].style.backgroundColor=colors[i];
}
function pickColor(){
	var random = Math.floor(Math.random() * colors.length);
//    i++;        '
    timer=25
                    clearInterval(myVar);

//    round++;
    round=Math.min(20,round )
	return colors[random];
}

function setupSquares(){
    round++;
   generatorcolor();
    for(var i=0;i<squares.length;i++)
{

    squares[i].style.backgroundColor=colors[i];
}

    round=Math.min(20,parseFloat(round));
     pickedcolor=pickColor()
    console.log(pickedcolor,'p')
    document.getElementById("colorDisplay").style.backgroundColor=pickedcolor;
     myVar =setInterval(()=>{
    document.getElementById("timer").innerHTML=timer;
        timer=Math.max(0,timer-1)
        if(timer==0 && parseFloat(round)<=20 ){round= parseFloat(round)+1;
            setupSquares();
                    }
},delay);
    
    


	for(var i = 0; i < squares.length; i++){
	//add click listeners to squares
		squares[i].addEventListener("click", function(){
			//grab color of clicked square
			var clickedColor = this.style.backgroundColor;
                console.log(clickedColor,'c')
            
			//compare color to pickedColor
			if(clickedColor  === pickedcolor){
//				alert("Correct!");
                document.getElementById("round").innerHTML=round;
                document.getElementById("score").innerHTML=score;
                clearInterval(myVar);
                if(parseFloat(round)!=20){  
                    score+=timer
                    timer=25
                    setupSquares();
                }
                else{
                    best=Math.max(best,score)
                    document.getElementById("best").innerHTML=best;
                    alert(`game ended Your Score is ${score}`)
                    timer=25
                }
                
    
				} else {
//				this.style.background = "#232323";
                        
//                            timer=Math.max(0,timer-5)
//				 alert("Try Again"); 
			}
		});
	}
}
//document.on('ready'){
setupSquares();
//}
