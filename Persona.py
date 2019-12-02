class Persona():
	def __init__(self):
		self.nombre="Sin Nombre"
		self.domicilio="Sin Domicilio"
		self.telefono=000000
		self.correo="sinCorreo@sinCorreo.com"
		
	def setNombre(self,nombre):
		self.nombre=nombre
	
	def setDomicilio(self,direccion):
		if len(direccion)>4:
			self.domicilio= direccion
            
	def setTelefono(self, numero):
		if numero>1:
			self.telefono=numero
		
	def setCorreo(self,email):
		contador=0
		#verifico cantidad de @
		for i in email:
			if(i=="@"):
				contador = contador + 1		
		if contador==1:
			self.correo=email

	def getNombre(self):
		return self.nombre

	def getDomicilio(self):
		return self.domicilio

	def getTelefono(self):
		return self.telefono

	def getCorreo(self):
		return self.correo

