from enum import Enum

class Dia(Enum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4
    SABADO = 5

diccionario_nombre_dia = {Dia.LUNES : "LUNES",
                          Dia.MARTES : "MARTES",
                          Dia.MIERCOLES : "MIERCOLES",
                          Dia.JUEVES : "JUEVES",
                          Dia.VIERNES : "VIERNES",
                          Dia.SABADO : "SABADO"
                          }