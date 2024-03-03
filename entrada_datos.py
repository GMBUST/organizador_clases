from dias import Dia
from curso import Curso
from bloque_horario import BloqueHorario

# Cosas de prueba.
nombre_orga_compu = "Organizacion del computador"
nombre_paradigmas = "Paradigmas de programacion"
nombre_teoria_algo = "Teoria de algoritmos"

# Función que crea las materias con sus cursos.
def obtener_materias():
    lista_orga_compu = []
    lista_paradigmas = []
    lista_teoria_algo = []
    
    # Organizacion del computador
    bloque1 = BloqueHorario(Dia.MARTES, "19:00", "23:00")
    bloque2 = BloqueHorario(Dia.MIERCOLES, "19:00", "23:00")
    curso = Curso(nombre_orga_compu, "1", [bloque1, bloque2])

    lista_orga_compu.append(curso)

    bloque1 = BloqueHorario(Dia.LUNES, "18:00", "22:00")
    bloque2 = BloqueHorario(Dia.MIERCOLES, "18:00", "22:00")
    curso = Curso(nombre_orga_compu, "2", [bloque1, bloque2])

    lista_orga_compu.append(curso)

    bloque1 = BloqueHorario(Dia.LUNES, "15:00", "19:00")
    bloque2 = BloqueHorario(Dia.MARTES, "19:00", "23:00")
    curso = Curso(nombre_orga_compu, "3", [bloque1, bloque2])

    lista_orga_compu.append(curso)


    # Paradigmas de programacion.
    bloque1 = BloqueHorario(Dia.MARTES, "19:00", "22:00")
    bloque2 = BloqueHorario(Dia.JUEVES, "19:00", "22:00")
    curso = Curso(nombre_paradigmas, "1", [bloque1, bloque2])

    lista_paradigmas.append(curso)

    bloque1 = BloqueHorario(Dia.MIERCOLES, "18:30", "21:30")
    bloque2 = BloqueHorario(Dia.VIERNES, "17:30", "20:30")
    curso = Curso(nombre_paradigmas, "2", [bloque1, bloque2])

    lista_paradigmas.append(curso)

    bloque1 = BloqueHorario(Dia.LUNES, "14:00", "17:00")
    bloque2 = BloqueHorario(Dia.JUEVES, "14:00", "17:00")
    curso = Curso(nombre_paradigmas, "3", [bloque1, bloque2])

    lista_paradigmas.append(curso)


    # Teoria de algoritmos.
    bloque1 = BloqueHorario(Dia.LUNES, "19:00", "22:00")
    bloque2 = BloqueHorario(Dia.MIERCOLES, "19:00", "22:00")
    curso = Curso(nombre_teoria_algo, "1", [bloque1, bloque2])

    lista_teoria_algo.append(curso)

    bloque1 = BloqueHorario(Dia.LUNES, "19:00", "22:00")
    bloque2 = BloqueHorario(Dia.JUEVES, "19:00", "22:00")
    curso = Curso(nombre_teoria_algo, "2", [bloque1, bloque2])

    lista_teoria_algo.append(curso)

    return [lista_orga_compu, lista_paradigmas, lista_teoria_algo]