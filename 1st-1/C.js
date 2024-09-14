const cin = (() => {
	const tokens = require('fs').readFileSync(0, 'utf8').split(/[\n\s]+/).reverse();
	return (typeTo = Number) => typeTo(tokens.pop());
})();

const n=cin()
let b=cin(String)

const c=Array.from(b)

let ans =[]

c.map((a)=>{
	switch (a){
		case "J":
			ans.push("O")
			break
		case "O":
			ans.push("I")
			break
		case "I":
			ans.push("J")
			break
	}
})

console.log(ans.join(""))