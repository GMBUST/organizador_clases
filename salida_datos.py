from cronograma import Curso

def imprimir_cronogramas(opciones):
    if len(opciones) == 0:
        print("No hay ningun cronograma posible")
        return

    cant = 1
    # Para cada cronograma imprimirlo.
    for cronograma in opciones:
        print("Opcion " + str(cant))
        print()
        # Para cada curso imprimirlo.
        for curso in cronograma:
            curso.imprimir_curso()
            print()

        print("-------------------------------------------------------")
        cant += 1