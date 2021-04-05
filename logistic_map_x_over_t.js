let x = 0.2
let px;

let r =1; 


let rSlider;



function setup() {
  createCanvas(600, 400);
  background(0);
  stroke(255);
  
  rSlider = createSlider(1,4,2,0.001);
  rSlider.changed(showgraph);
  showgraph();
  
  
}
 

function showgraph(){
  x=0.2;
  background(0);
  noFill();
  beginShape();
  r = rSlider.value();
  text(`R value ${r}`,10,10);
    for(let t = 0; t< width; t+=10){
      let x2 = r*(x - x**2);  // x2 is next x Using the same equation as introduction to complexity
      y = map(x2, 0, 1, height, 0); // map the values for plotting
      
      
      vertex(t,y);
      
      
      x = x2;
      
     
      
      
    }
  endShape();
  
}
