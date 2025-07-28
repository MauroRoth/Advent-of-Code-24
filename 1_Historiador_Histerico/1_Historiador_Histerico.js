const fs = require('fs');
fs.readFile('input.txt', 'utf8', (err, data) => {
	if (err) {
		console.error('Error al leer el archivo:', err);
        	return;
      	}
	lineas = data.split("\n");
	lineas.pop()
	datos = lineas.map(x=>{return x.split("   ")});
	let lista1 = datos.map(x=>{return Number(x[0])});
	let lista2 = datos.map(x=>{return Number(x[1])});
	let lista1_ord = lista1.sort((a,b)=>a-b);
	let lista2_ord = lista2.sort((a,b)=>a-b);
	let suma = 0;
	for(let i=0; i<datos.length; i++){
		let distancia = Math.abs(lista1_ord[i]-lista2_ord[i]);
		suma += distancia;
	}
	console.log(suma)
	
});



