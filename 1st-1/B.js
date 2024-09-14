const { disconnect } = require('process');

const cin = (() => {
	const tokens = require('fs').readFileSync(0, 'utf8').split(/[\n\s]+/).reverse();
	return (typeTo = Number) => typeTo(tokens.pop());
})();

const x=cin()
let distance=0

for (let a=1;a<=x;a++){
	if(a%2!=0){
		distance+=3
	}else{
		distance-=2
	}
}

console.log(distance)