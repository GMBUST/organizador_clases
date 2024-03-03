from dias import Dia, diccionario_nombre_dia

class BloqueHorario():
    def __init__(self, dia, inicio, fin):
        self.dia = dia
        self.inicio = inicio
        self.fin = fin

    def obtener_dia(self):
        return self.dia

    def obtener_hora_inicio(self):
        return self.inicio
    
    def obtener_hora_fin(self):
        return self.fin
    
    def se_superpone(self, bloque):
        # Si el día de los cursos coincide.
        if bloque.obtener_dia() == self.dia:

            # Verifica si el horario de inicio está dentro del rango del bloque que llama a la primitiva. 
            if self.inicio <= bloque.obtener_hora_inicio() and bloque.obtener_hora_inicio() < self.fin:
                return True

            # Verifica si el horario de finalización está dentro del rango del bloque que llama a la primitiva. 
            if self.inicio < bloque.obtener_hora_fin() and bloque.obtener_hora_fin() <= self.fin:
                return True

            # Verifica que el bloque pasado por argumento no encapsule al que llama a la primitiva.
            if bloque.obtener_hora_inicio() <= self.inicio and self.fin <= bloque.obtener_hora_fin():
                return True

        return False
    
    def imprimir(self):
        print("Dia: " + diccionario_nombre_dia[self.dia] + " - Horario: " + self.inicio + " a " + self.fin)