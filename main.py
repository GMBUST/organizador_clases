from entrada_datos import obtener_materias
from organizador_clases import buscar_cronogramas_posibles
from salida_datos import imprimir_cronogramas

def main():
    # Obtener materias con sus cursos.
    materias = obtener_materias()

    # Obtener cronogramas posibles.
    opciones = buscar_cronogramas_posibles(materias)

    # Imprimir cronogramas.
    imprimir_cronogramas(opciones)

if __name__ == "__main__":
    main()