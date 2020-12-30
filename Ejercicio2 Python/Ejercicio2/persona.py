class persona:
	def __init__(self, dni, nombre, apellido):
		self.dni = dni;
		self.nombre = nombre;
		self.apellido = apellido;

	def mostrarDatos(self):
		print('-' * 20);
		print("Nombre: ",self.nombre);
		print("Apellido: ",self.apellido);
		print("DNI: ", self.dni)
		print('-' * 20);

# Manera de sobreescribir el equals
	def __eq__(self, obj):
		if isinstance(obj, persona):
			return obj.dni == self.dni;
		return NotImplemented
