from Persona import Persona
from datetime import datetime
class Cliente(Persona):
	id=0
	rfc="Sin RFC"
	registroDia=0
	registroMes=0
	registroAnio=0
	limiteCredito=0
	dia=datetime.now().day
	mes=datetime.now().month
	anio=datetime.now().year

	
	def setId(self,num):
		if num>0:
			self.id=num
	
	def setRfc(self ,rfc):
		if len(rfc)==5:
			self.rfc = rfc
	
	def setRegistro(self,dia,mes,anio):
		if ((self.registroAnio<anio)and(self.registroMes<mes)and(self.registroDia<dia)):
			self.registroAnio=anio
			self.registroMes=mes
			self.registroDia=dia
	
	def setLimiteCredito(self,limite):
		if limite>=0:
			self.limiteCredito=limite
	
	

