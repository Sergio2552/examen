from Persona import Persona

class Empleado(Persona):
	numEmpleado=0
	curp="Sin Curp"
	rfc="Sin rfc"
	imss="Sin NSS"
	
	def setNumEmpleado(self, numero):
		if numero>0:
			self.numEmpleado=numero
			
	def setCurp(self,curp):
		if len(curp)==18:
			self.curp=curp
	
	def setRfc(self, rfc):
		coincide=0
		if len(rfc)==13:
			for letra in range(8):
				if self.curp[letra]==rfc[letra]:
					coincide=coincide+1
			if coincide==8:
				self.rfc=rfc

			
			
	def setImss(self, num):
		if len(num)>7:
			self.imms=num
	
	def getNumEmpleado(self):
		return self.numEmpleado
		
	def getCurp(self):
		return self.curp
		
	def getRfc(self):
		return self.rfc
		
	def getImss(self):
		return self.imss
