import Paciente;
import Constantes;

class PacienteConsulta(Paciente.Paciente):
    def __init__(self, dni, nombre, fecha, motivo):
        super().__init__(dni, nombre, fecha);
        self.__motivo = motivo;

    def facturar(self):
        self._Paciente__tarifaFinal = Constantes.Constantes.PRECIO_CONSULTA;


