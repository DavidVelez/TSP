#TSP
#Autor: David Felipe Velez Cadavid
#Colaborador: Juan Manuel Vergara Alvarez

#encoding: utf-8
import itertools 


# En primera instancia se crea una matriz de 6x6, dicha matriz es asimetrica,
#esto se debe a que los costos para viajar de ciudad en ciudad varian.

w = [
	[0, 300, 700, 570, 420, 198 ],
	[450, 0, 800, 50, 530, 160  ],
	[230, 580, 0, 850, 255, 370 ],
	[560, 120, 356, 0, 480, 240 ],
	[311, 414, 250, 669, 0, 418 ],
	[800, 356, 700, 432, 234, 0 ]
    ]

#Funcion travel: realiza los calculos necesarios a traves de comparaciones entre costos de viaje, para ir de ciudad en ciuadad, almacenando #respectivamente los costos minimos en listas.

 
def travel(w):
	
	n = len(w) 


	#valor inicial de 0 a todos los demas puntos
	A = {(frozenset([0, i+1]), i+1): (costo, [0, i+1]) for i, costo in enumerate(w[0][1:])}

	

	for m in range(2, n):
		B = {}
		#en esta etapa se usa la recurisividad, ademas se utilizan el modulo 'combinations' que permite realizar
		#agrupaciones y comparaciones de datos.         
		for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
			for j in S - {0}:
				#se busca la ruta menos costosa para el viaje, es decir se buscan los valores minimos. 
				B[(S, j)] =min((A[(S-{j},k)][0] + w[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j) 
		A = B
		#Ahora se agregan camino inicial y camino final
	res = min([(A[d][0] + w[0][d[1]], A[d][1]) for d in iter(A)])
	#Encontrado el valor minimo se tiene la solucion optima.

	Resultado = res[0], ["Ciudad "+str(i+1) for i in  res[1] ] 
	#con el ordenamiento de costos, se tiene solo que mostrar cual es la ruta a seguir en el viaje, es decir
	#se posicionan las ciudades en relacion con sus costos.
	
	return Resultado 

print "\nMejor ruta de viaje con vuelta a la ciudad 1 es:\n", travel(w)[1], "\n\nCon un costo total de:\n", travel(w)[0]






