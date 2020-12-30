# Uso listas de personas, muestro, añado y borro. Para la gestion hago un menu y utilizo try catch
import persona;
import os;
personas = [];

def mostrar():
    for persona in personas:
        persona.mostrarDatos();


def borrar():
    try:
        dni = input("Dime DNI: ");
        #Si encuentra una persona que sobreescriba el equals la borra (Solo una persona con el mismo dni)
        personas.remove(persona.persona(dni, "", ""));
        print("Persona Borrada");
    #Al no encontrar persona, en vez de devolver -1, lanza una excepcion
    except:
        print("No encontrado");

def crear():
        nombre = input("Dime Nombre: ");
        apellido = input("Dime Apellido: ");
        dni = input("Dime DNI: ");
        person = persona.persona(dni,nombre,apellido);
        if(buscaPersona(person) == -1):
            personas.append(person);
            print("Persona Creada");
        else:
            print("Ya existe una persona con ese dni");

def buscaPersona(person):
    try:
        return personas.index(person);
    except:
        return -1;

def menu():
    print("-" * 20)
    print("1 - Crear Persona")
    print("2 - Borrar Persona")
    print("3 - Mostrar Personas")
    print("0 - Salir")
    print("-" * 20)
   

def main():
    personas.append(persona.persona("79340319W", "Daniel", "Dipas"));
    personas.append(persona.persona("22255533W", "Juan", "Alvarez"));
    personas.append(persona.persona("11122233A", "Marta", "Castro"));
    salir = False;

    while not salir:
        try:
            menu();
            opcion = int(input("Dime opcion: " ))
            print ("\n" * 100);

            if(opcion == 1):
                crear();

            elif(opcion == 2):
                borrar();

            elif(opcion == 3):
                mostrar();

            elif(opcion == 0):
                salir = True
                print("Adios!");

            else:
                raise Exception;

        except:
            print ("\n" * 100);
            print("Opcion no valida");

if __name__ == "__main__":
    main();