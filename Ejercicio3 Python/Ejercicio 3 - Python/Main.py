
  
###
#Haz un programa con un menú que permita gestionar la cola de espera de un médico. Hay
#tres tipos de pacientes: los que vienen a consulta (se le pide al usuario nombre, fecha de nacimiento,
#motivo de la consulta), los que viene por recetas (se le pide: nombre, fecha de nacimiento, lista de
#medicamentos) y el que viene a revisión (se le pide nombre, fecha de nacimiento y fecha de la visita
#anterior).
#    • Las tarifas del médico son: Consulta: 100 eur. Recetas: 5 eur por cada unidad. Revisión: 30 eur para
#    mayores de 65 años, 50 eur para resto.
#    • Crear una clase para cada tipo de paciente en el propio archivo del programa con los constructores
#    necesarios y el método de facturar() en cada una de las clases. Implementa herencia si lo crees
#    necesario.
#    • El programa tendrá un menú para: 
#    a) Registrar la llegada del paciente: se le preguntará por qué viene al médico y se le piden
#    sus datos.
#    b) Llamar a consulta (por orden de llegada). Se le cobra la tarifa correspondiente.
#    c) Consultar total facturado hasta ese momento
###


import Paciente;
import Constantes;
import datetime;
from datetime import date;
from dateutil.relativedelta import relativedelta

pacientes = [];

def main():
    salir = False;
    while(salir is False):
            menu();
            opcion = int(input("Dime Opcion: "));
            print("\n" * 50);
            if(opcion == 1):
                regLlegada();
            elif(opcion == 2):
                print("op2");
            elif(opcion == 3):
                print("op3");
            elif(opcion == 0):
                salir = True;
            else: 
                raise exception;

    

def menu():
    print("-" * 20);
    print("1 - Registrar Llegada");
    print("2 - Llamar a Consulta");
    print("3 - Consultar Total Facturado");
    print("0 - Salir");
    print("-" * 20);

def menuLlegada():
    print("-" * 20);
    print("MOTIVO PACIENTE");
    print("-" * 20);
    print("1 - Consulta");
    print("2 - Recetas");
    print("3 - Revision");
    print("0 - Salir");
    print("-" * 20);

  
def regLlegada():
    elegir = False;
    while(elegir is False):
            menuLlegada();
            op=int(input("Dime tipo de Paciente: "))
            print("\n" * 50);
            if(op==1 or op==2 or op==3):
                elegir=True;
                aniadirPaciente(op);
            elif(op==0): 
                elegir=True;
            else:
                raise Exception;

def aniadirPaciente(op):
    dni = input("Dime DNI: ");
    nombre = input("Dime Nombre: ");
    fecha = datetime.datetime.strptime(input("Dime Fecha de Nacimiento (DD-MM-AAAA): "), '%d-%m-%Y')
    fecha = fecha.date();
    time_difference = relativedelta(fecha, date.today())
    difference_in_years = abs(time_difference.years);
    print(difference_in_years);   

def pacienteConsulta():
    print("Consulta");

def pacienteRecetas():
    print("Recetas");

def pacienteRevision():
    print("Revision");

if __name__ == "__main__":
    main();