import Paciente;
import Constantes;

class PacienteReceta(Paciente.Paciente):
    def __init__(self, dni, nombre, fecha, medicamentos):
        super().__init__(dni, nombre, fecha)
        self.__medicamentos = medicamentos;

    def facturar(self):
        self._Paciente__tarifaFinal = medicamentos.len() * Constantes.Constantes.PRECIO_RECETA;


