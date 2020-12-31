from Paciente import Paciente;
import Constantes;

class PacienteConsulta(Paciente):
    def __init__(self, dni, nombre, fecha, motivo):
        super().__init__(dni, nombre, fecha);
        self.__motivo = motivo;

    def facturar(self):
        super().atendido();
        self._Paciente__tarifaFinal = Constantes.Constantes.PRECIO_CONSULTA;

    def __str__(self):
            prefijo=super().__str__();
            return prefijo + " Tipo: Consulta Motivo: "+  self.__motivo;

        


