from Persona import Persona
from Empleado import Empleado


cantidad=int(input("Cantidad de empleados a quieres registrar:"))
empleados=[]
n = len(empleados)
for i in range(cantidad):
	nombre = input("Nombre del empleado:")
	domicilio = input("Domicilio del empleado:")
	telefono = int(input("Telefono del empleado:"))
	correo = input("Correo del empleado")
	numero= int(input("Identificador del empleado"))
	rfc = input("Rfc del empleado")
	limite = int(input("Limite de credido del empleado"))
	dia= int(input("Dia de registro del empleado"))
	mes= int(input("Mes de registro del empleado"))
	anio=int(input("Anio de registro del empleado"))
	nuevo = empleado()
	nuevo.setNombre(nombre)
	nuevo.setDomicilio(domicilio)
	nuevo.setTelefono(telefono)
	nuevo.setCorreo(correo)
	nuevo.setId(numero)
	nuevo.setRfc(rfc)
	nuevo.setLimiteCredito(limite)
	nuevo.setRegistro(dia,mes,anio)	
	empleados.append[i]=nuevo;
	
	
for z in range(n):
	for j in range(0, n-z-1):
             # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
		if empleados[j].id > empleados[j+1] :
			empleados[j], empleados[j+1] = empleados[j+1], empleados[j]

for i in range(len(empleados)):
	print (empleados[i].getNombre())
	
