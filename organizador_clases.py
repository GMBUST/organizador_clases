from cronograma import *

# Armar posibles combinaciones de materias.
def buscar_cronogramas_posibles(materias):
	opciones = []
	cronograma = Cronograma()

	__armar_cronograma_rec(materias, 0, cronograma, opciones)

	return opciones

# Crea una nueva lista con los cursos.
def __reconstruir_cronograma_lista(cronograma):
	lista = []

	for clave in cronograma:
		lista.append(cronograma[clave])

	return lista

# Ubicar elementos de forma recursiva.
def __armar_cronograma_rec(materias, nivel, cronograma, opciones):

	if nivel == len(materias):
		nueva_opcion = __reconstruir_cronograma_lista(cronograma.devolver_cronograma())
		opciones.append(nueva_opcion)
		return

	for curso in materias[nivel]:

		if cronograma.se_superpone(curso) is False:
			cronograma.agregar_curso(curso)
			__armar_cronograma_rec(materias, nivel + 1, cronograma, opciones)
			cronograma.quitar_curso(curso)
