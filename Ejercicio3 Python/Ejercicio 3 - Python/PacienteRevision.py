import Paciente;
import Constantes;
import datetime;
from datetime import date;

class PacienteRevision(Paciente.Paciente):
    def __init__(self, dni, nombre, fecha, fechaAnterior):
        super().__init__(dni, nombre, fecha)
        self.__fechaVisitaAnterior = fechaAnterior;

    def facturar(self):
        pass

    def calcEdad(self):
        time_difference = relativedelta(self._Paciente__fecha, date.today())
        difference_in_years = time_difference.years


