
# Genero una función que se comporta como main del programa e instancio una clase (Previamente importada de otro archivo)
def main():
    import clase;
    per = clase.persona("79340319W", "Daniel", "Dipas");
    per.mostrarDatos();

if __name__ == "__main__":
    main()