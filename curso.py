class Curso():
    def __init__(self, materia, numero, bloques: list):
        self.materia = materia
        self.numero = numero
        self.clave = materia + numero
        self.bloques = bloques

    def obtener_clave_curso(self):
        return self.clave

    def obtener_bloques_horarios(self):
        return self.bloques

    def se_superpone(self, curso_nuevo):
        for bloque_nuevo in curso_nuevo.obtener_bloques_horarios():
            for bloque_guardado in self.bloques:

                if bloque_guardado.se_superpone(bloque_nuevo) is True:
                    return True

        return False

    def imprimir_curso(self):
        print("Materia: " + self.materia)
        print("Curso: " + self.numero)
        self.__imprimir_bloques_horarios()
    
    def __imprimir_bloques_horarios(self):
        for bloque in self.bloques:
            bloque.imprimir()