import Paciente;
from Constantes import Constantes;
import datetime;
from datetime import date;
from dateutil.relativedelta import relativedelta

class PacienteRevision(Paciente.Paciente):
    def __init__(self, dni, nombre, fecha, fechaAnterior):
        super().__init__(dni, nombre, fecha)
        self.__fechaVisitaAnterior = fechaAnterior;

    def facturar(self):
        super().atendido();
        edad=self.__calcEdad();
        if(edad >= Constantes.EDAD_MAYOR):
            self._Paciente__tarifaFinal = Constantes.REVISION_MAYOR;
        else:
            self._Paciente__tarifaFinal = Constantes.REVISION_RESTO;

    def __calcEdad(self):
        edad = abs(relativedelta(self._Paciente__fecha, date.today()).years)
        return edad;
    
    def __str__(self):
        prefijo=super().__str__();
        return prefijo + " Tipo: Revision Revision Previa: "+   str(self.__fechaVisitaAnterior);

