const particles = [];
function setup(){
	createCanvas(windowWidth, windowHeight);
	let oldWidth = window.innerWidth;
	// window.addEventListener("resize", handleResize);

	// function handleResize(initial = false){
	// 	if (window.innerWidth !== oldWidth || initial) {
	// 		target.classList.add("setting-100vh");
	// 		const h = target.clientHeight;
	// 		target.classList.remove("setting-100vh");
	// 		target.style.minHeight = h + "px";
	// 	}
	// }

	const particlesLength = Math.max(Math.floor(window.innerWidth / 15), 100);
	for (let i = 0; i < particlesLength; i++) {
		particles.push(new Particle());
	}
}

function draw(){
	background(0);
	particles.forEach((particle, idx) => {
		particle.update();
		particle.draw();
		particle.checkParticles(particles.slice(idx));
	});
}

class Particle{
	constructor(){
		this.pos = createVector(random(width), random(height));
		this.vel = createVector(random(-1, 1), random(-1, 1));
		this.size = 0.75;
	}

	update(){
		this.pos.add(this.vel);
		this.edges();
	}

	draw(){
		noStroke();
		fill("rgba(0, 255, 0, 0.5)");
		circle(this.pos.x, this.pos.y, this.size * 2);
	}

	edges(){
		if(this.pos.x < 0 || this.pos.x > width) {
			this.vel.x *= -1;
		}

		if(this.pos.y < 0 || this.pos.y > height) {
			this.vel.y *= -1;
		}
	}

	checkParticles(particles){
		particles.forEach((particle) => {
			const d = dist(this.pos.x, this.pos.y, particle.pos.x, particle.pos.y);
			if (d < 150){
				const alpha = map(d, 0, 120, 0, 0.25);
				stroke(`rgba(0, 255, 0, ${alpha})`);
				line(this.pos.x, this.pos.y, particle.pos.x, particle.pos.y);
			}
		});
	}
}
