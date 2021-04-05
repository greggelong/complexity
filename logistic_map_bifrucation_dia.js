let x;


function setup() {
  createCanvas(600, 400);
  background(0);
  stroke(255);
  biDi();
}
 
 

function biDi(){
  x=0.2;
  background(0);
  stroke(0,200,0,200);
  
  for (let r = 2.8; r<4; r+=0.00001){
     let x2 = r*(x - x**2);  // x2 is next x Using the same equation as introduction to complexity
      let y = map(x2, 0, 1, height, 0); // map the values for plotting
      let px = map(r,2.8,4,0,width);
      point(px,y);
      
      x = x2;
    
  }
  
}
