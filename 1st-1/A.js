const cin = (() => {
	const tokens = require('fs').readFileSync(0, 'utf8').split(/[\n\s]+/).reverse();
	return (typeTo = Number) => typeTo(tokens.pop());
})();

const a=cin()
console.log(Math.trunc(a/5))