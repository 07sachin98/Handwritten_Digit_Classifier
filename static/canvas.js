window.addEventListener('load', ()=>{ 
        
    document.addEventListener('mousedown', initial); 
    document.addEventListener('mouseup', finish); 
    document.addEventListener('mousemove', draw);
	header();
}); 

function header() {	
 var x = prompt("Enter Window title", "Digit Recognition"); 
  document.getElementById("header").innerHTML = x; } 
	 
const canvas = document.querySelector('#canvas'); 
const ctx = canvas.getContext('2d'); 
canvas.width = 280;
canvas.height = 280;

let coord = {x:0 , y:0};  
let paint = false; 
  
function getPosition(event){ 
  coord.x = event.clientX - canvas.offsetLeft; 
  coord.y = event.clientY - canvas.offsetTop; 
} 
function initial(event){ 
  paint = true; 
  getPosition(event); 
} 
function finish(){ 
  paint = false; 
} 
   
function draw(event){ 
  if (!paint) return; 
  ctx.beginPath(); 
    
  ctx.lineWidth = 10; 
  ctx.lineCap = 'round';   
  ctx.strokeStyle = 'black'; 
  ctx.moveTo(coord.x, coord.y); 
  getPosition(event); 
  ctx.lineTo(coord.x , coord.y);  
  ctx.stroke(); 
} 
 document.getElementById('clear').addEventListener('click', function cl() {
        ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
      }, false);