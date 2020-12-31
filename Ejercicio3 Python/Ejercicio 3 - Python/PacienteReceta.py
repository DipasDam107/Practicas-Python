import Paciente;
import Constantes;

class PacienteReceta(Paciente.Paciente):
    def __init__(self, dni, nombre, fecha, medicamentos):
        super().__init__(dni, nombre, fecha)
        self.__medicamentos = medicamentos;

    def facturar(self):
        super().atendido();
        self._Paciente__tarifaFinal = len(self.__medicamentos) * Constantes.Constantes.PRECIO_RECETA;

    def __str__(self):
        try:
            prefijo=super().__str__();
            return prefijo + " Tipo: Receta Recetas: "+  str(len(self.__medicamentos));
        except Exception as e:
            print(e);
