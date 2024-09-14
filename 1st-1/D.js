const cin = (() => {
	const tokens = require('fs').readFileSync(0, 'utf8').split(/[\n\s]+/).reverse();
	return (typeTo = Number) => typeTo(tokens.pop());
})();

const n=cin()
const m=cin()

let a=[]
let b=[]

for(let i=1;i<=n;i++){
	a.push(cin())
}

for(let i=1;i<=m;i++){
	b.push(cin())
}

let ans=0
let c=0

for(ann of a){
	for(kawa of b){
		if(ann>kawa){
			c=(ann+kawa)*ann
		}else{
			c =(ann+kawa)*kawa
		}
		ans+=c
	}
}

console.log(ans)