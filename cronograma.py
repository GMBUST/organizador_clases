from curso import Curso

class Cronograma():

    def __init__(self):
        self.cursos_guardados = {}

    def se_superpone(self, curso_nuevo):
        for clave in self.cursos_guardados:
            if self.cursos_guardados[clave].se_superpone(curso_nuevo) is True:
                return True

        return False
    
    def agregar_curso(self, curso):
        self.cursos_guardados[curso.obtener_clave_curso()] = curso

    def quitar_curso(self, curso):
        del self.cursos_guardados[curso.obtener_clave_curso()]

    def devolver_cronograma(self):
        return self.cursos_guardados