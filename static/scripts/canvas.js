(function() {
  var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame ||
                window.webkitRequestAnimationFrame || window.msRequestAnimationFrame || function( callback ){
              window.setTimeout(callback, 1000 / 60);
            };
//   window.requestAnimationFrame = requestAnimationFrame;
})();

var canvas = document.getElementById('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var c = canvas.getContext('2d');
// document.body.style.background = "url(" + canvas.toDataURL() + ")";
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function getStarProps(isStatic){
    let x = getRandomInt(canvas.width);
    let y = getRandomInt(canvas.height/2);
    let radius = getRandomInt(4);
    let blur = getRandomInt(6)/10+4;
    if (isStatic){
      var dy= 0
      var dx = 0
    }
    else {
      var dy = Math.random()*.1
      let isRight = Math.random() > .5;
      if(isRight){
        var dx = Math.random()*.1
      }
      else{
        var dx = -Math.random()*.1
      }
    }
    return {x:x, y:y, radius:radius, blur:blur, dy:dy, dx:dx};
}

var Star = class Star{
  constructor({x, y, radius, blur, dy, dx}){
    this.x = x;
    this.y = y;
    this.dy = dy
    this.dx = dx
    this.blur = blur;
    this.radius = radius;
    // console.log(x,y,radius,blur,isStatic);
  }
}

Star.prototype.reset = function(){
  console.log('reset star');
  var {x,y,dx,dy,radius,blur} = getStarProps(true);
  this.x = x
  this.y = y
  this.dx = dx
  this.dy = dy
  this.radius = radius
  this.blur = blur
}

Star.prototype.update = function(){
  if(this.x<0 ||  this.x >= canvas.width || this.y <= 0 || this.y >= canvas.height){
			  this.reset();
	}
  else{
    this.x = this.x+this.dx
    this.y = this.y+this.dy
    c.shadowBlur = this.blur;
    c.shadowOffsetX = 0;
    c.shadowOffsetY = 0;
    c.fillStyle="#ffd800";
    c.shadowColor="#ffe760"; //set the shadow colour to that of the fill
    c.beginPath();
    c.arc(this.x,this.y,this.radius,0,Math.PI*2,true);
    c.fill();
  }
}
////////////SHOOTING STAR///////////////////
function getShootingStarProps(){
  let x = getRandomInt(canvas.width);
  let y = 0;
  let radius = getRandomInt(4);
  let blur = (getRandomInt(6)/10)+4;
  var dy =  10;
  let isRight = Math.random() > .5;
  if(isRight){
    var dx = getRandomInt(3)+3;
  }
  else{
    var dx= -getRandomInt(3)-3;
  }
  return {x:x, y:y, radius:radius, blur:blur, dy:dy, dx:dx};
}

var ShootingStar = class ShootingStar{
  constructor({x, y, radius, blur, dy, dx}){
    this.x = x;
    this.y = y;
    this.dy = dy;
    this.dx = dx;
    this.blur = blur;
    this.radius = radius;
  }
}

ShootingStar.prototype.reset = function(){
  var {x,y,dx,dy,radius,blur} = getShootingStarProps(true);
  this.x = x
  this.y = 0
  this.dx = dx
  this.dy = dy
  this.radius = radius
  this.blur = blur
}

ShootingStar.prototype.update = function(){
  if(this.x<0 ||  this.x >= canvas.width || this.y >= canvas.height){
			  this.reset();
	}
  else{
    this.x = this.x+this.dx
    this.y = this.y+this.dy
    c.shadowBlur = this.blur;
    c.shadowOffsetX = 0;
    c.shadowOffsetY = 0;
    c.fillStyle="#ffd800";
    c.shadowColor="#ffe760"; //set the shadow colour to that of the fill
    c.beginPath();
    c.arc(this.x,this.y,this.radius,0,Math.PI*2,true);
    c.moveTo(this.x, this.y-this.radius/2);
    c.lineTo(this.x+(20*(-this.dx)),this.y+(20*(-this.dy)))
    c.lineTo(this.x-this.radius/2,this.y)
    c.fill();
  }
}

//Static Stars
var stars = []
for(var i=0; i<30; i++){
  stars.push(new Star(getStarProps(true)));
}
//Moving Stars
for(var j=0; j<20; j++){
  stars.push(new Star(getStarProps(false)))
}
//Moving Stars
var shootingStars = []
for(var k=0; k<1; k++){
  shootingStars.push(new ShootingStar(getShootingStarProps()))
}

function init(){
  draw();
}

function draw(){
  c.clearRect(0, 0, canvas.width, canvas.height)
  for(var x=0; x<stars.length; x++){
    stars[x].update();
  }
  for(var y=0; y<ShootingStar.length; y++){
    shootingStars[y].update();
  }
  requestAnimationFrame(draw)
}

init();
