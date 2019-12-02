from Persona import Persona
from Empleado import Empleado

def main(args):
    print("give me a bottle of rum!")
    cantidad=int(input("Cantidad de clientes a quieres registrar:"))
    clientes=[]
    for i in range(cantidad):
		nombre = input("Nombre del cliente:")
		domicilio = input("Domicilio del cliente:")
		telefono = int(input("Telefono del cliente:"))
		correo = input("Correo del cliente")
		numero= int(input("Identificador del cliente"))
		rfc = input("Rfc del cliente")
		limite = int(input("Limite de credido del cliente"))
		dia= int(input("Dia de registro del cliente"))
		mes= int(input("Mes de registro del cliente"))
		anio=int(input("Anio de registro del cliente"))
		nuevo = Cliente()
		nuevo.setNombre(nombre)
		nuevo.setDomicilio(domicilio)
		nuevo.setTelefono(telefono)
		nuevo.setCorreo(correo)
		nuevo.setId(numero)
		nuevo.setRfc(rfc)
		nuevo.setLimiteCredito(limite)
		nuevo.setRegistro(dia,mes,anio)	
		clientes.append[i]=nuevo
		
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
