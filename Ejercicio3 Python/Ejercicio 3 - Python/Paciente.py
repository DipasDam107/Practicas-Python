class Paciente():
    # Los atributos que empiezan por _ son protected, los que empiezan por __ son privados
    def __init__(self, dni, nombre, fecha):
        self.__dni = dni;
        self.__nombre=nombre;
        self.__fecha=fecha;
        self.__atendido = False;
        self.__tarifaFinal = 0;

    def atendido(self):
        self.__atendido = True;
        #hacer calculos

    def __str__(self):
        at = "No";
        if(self.__atendido):
            at = "Si";
        return "Nombre: "+ self.__nombre + " DNI: " + self.__dni + " Atendido: " + at ;
