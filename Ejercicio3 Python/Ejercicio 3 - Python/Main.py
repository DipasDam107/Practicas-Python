
  
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


from PacienteReceta import PacienteReceta;
from PacienteConsulta import PacienteConsulta;
from PacienteRevision import PacienteRevision;
from Paciente import Paciente;
import Constantes;
import datetime;
from datetime import date;
from dateutil.relativedelta import relativedelta

pacientes = [];

def main():
    salir = False;
    while(salir is False):
        try:
            menu();
            opcion = int(input("Dime Opcion: "));
            print("\n" * 50);
            if(opcion == 1):
                regLlegada();
            elif(opcion == 2):
                if(llamarConsulta()):
                    print("Se ha atendido al paciente");
                else:
                    print("No hay pacientes en cola");
            elif(opcion == 3):
                print("Se han facturado " + str(consultarTotalFacturado()) + " €");
            elif(opcion == 4):
                listarPacientes();
            elif(opcion == 0):
                salir = True;
            else: 
                raise exception;
        except:
            print("Eleccion incorrecta");

    

def menu():
    print("-" * 20);
    print("1 - Registrar Llegada");
    print("2 - Llamar a Consulta");
    print("3 - Consultar Total Facturado");
    print("4 - Listar Pacientes");
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

def listarPacientes():
    for paciente in pacientes:
        print(str(paciente));

def regLlegada():
    elegir = False;
    while(elegir is False):
        try:
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
        except:
            print("Eleccion incorrecta");

def aniadirPaciente(op):
    dni = input("Dime DNI: ");
    nombre = input("Dime Nombre: ");
    try:
        fecha = datetime.datetime.strptime(input("Dime Fecha de Nacimiento (DD-MM-AAAA): "), '%d-%m-%Y')
        fecha = fecha.date();
    except:
        print("Fecha Incorrecta");

    if(op == 1):
        aniadirPacienteConsulta(dni,nombre,fecha);
    elif(op==2):
        aniadirPacienteRecetas(dni,nombre,fecha);
    else:
        aniadirPacienteRevision(dni,nombre,fecha);


def aniadirPacienteConsulta(dni, nombre, fecha):
    motivo = input("Dime motivo de la visita: ");
    pacientes.append(PacienteConsulta(dni, nombre, fecha, motivo));

def aniadirPacienteRecetas(dni, nombre, fecha):
    medicinas=[];
    salir=False;
    while salir is False:
        medicina = input("Dime medicina: ");
        if(medicina != ""):
            medicinas.append(medicina);
        else:
            salir = True;
    pacientes.append(PacienteReceta(dni, nombre, fecha, medicinas));

def aniadirPacienteRevision(dni, nombre, fecha):
    try:
        fechaVisita = datetime.datetime.strptime(input("Dime Fecha de visita anterior (DD-MM-AAAA): "), '%d-%m-%Y')
        fechaVisita = fechaVisita.date();
        pacientes.append(PacienteRevision(dni, nombre, fecha, fechaVisita));

    except Exception as e:
        print("Fecha Incorrecta");
    
def llamarConsulta():
    for paciente in pacientes:
        if(paciente._Paciente__atendido is False):
            paciente.facturar();
            return True;
    return False;

def consultarTotalFacturado():
    total=0;
    for paciente in pacientes:
        if(paciente._Paciente__atendido):
            total += paciente._Paciente__tarifaFinal;
    return total;

if __name__ == "__main__":
    main();