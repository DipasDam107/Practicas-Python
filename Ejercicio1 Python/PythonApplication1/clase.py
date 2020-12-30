class persona:
	def __init__(self, dni, nombre, apellido):
		self.dni = dni;
		self.nombre = nombre;
		self.apellido = apellido;

	def mostrarDatos(self):
		print("Nombre: ",self.nombre);
		print("Apellido: ",self.apellido);
		print("DNI: ", self.dni)