const fs = require('fs');
fs.readFile('input.txt', 'utf8', (err, data) => {
	if (err) {
		console.error('Error al leer el archivo:', err);
        	return;
      	}
	lineas = data.split("\n");
	lineas.pop()
	datos = lineas.map(x=>{return x.split("   ")});
	let lista1_ej = [3,4,2,1,3,3];
	let lista2_ej = [4,3,5,3,9,3];
	let lista1_input = datos.map(x=>{return Number(x[0])});
	let lista2_input = datos.map(x=>{return Number(x[1])});

	let lista1 = lista1_input;	
	let lista2 = lista2_input;
	let longitud = datos.length;
	//let longitud = lista1.length;

	let lista1_ord = lista1.sort((a,b)=>a-b);
	let lista2_ord = lista2.sort((a,b)=>a-b);

	console.log('Primera Parte')
	let suma = 0;
	for(let i=0; i<longitud; i++){
		let distancia = Math.abs(lista1_ord[i]-lista2_ord[i]);
		suma += distancia;
	}
	console.log('SUMA DE DISTANCIAS: ',suma)
	
	console.log('Segunda Parte')
	let puntajeT = 0;
	lista2_ord.forEach(e=>{
		let repeticiones = lista1_ord.filter(x=>x==e).length;
		let puntaje = e*repeticiones;
		puntajeT += puntaje
	})
	console.log('PUNTAJE DE SIMILITUD FINAL: ', puntajeT)
	
});



