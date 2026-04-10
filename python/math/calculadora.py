# -*- coding: utf-8 -*-

# Mi primer programa en Phyton

# Calculadora básica

# Definición de funciones

def restar():
	num1 = input("Introduce el primer número: " )
	num2 = input("Introduce el segundo número: ")
	resta = float(num1) - float(num2)
	print ("La resta es:", resta)

def multiplicar():
	num1 = input("Introduce el primer número: " )
	num2 = input("Introduce el segundo número: ")
	producto = float(num1) * float(num2)
	print ("El producto es:", producto)

def dividir():
	num1 = input("Introduce el dividendo: " )
	num2 = input("Introduce el divisor: ")
	
	try:
		division = float(num1) / float(num2)
		print ("La división es:", division)
	
	except ZeroDivisionError:
		print ("No se puede dividir por 0")
		
# Bucle principal

while True:
	print ("\n", "Opciones: ")
	print ("-----------------")
	print ("1 Sumar")
	print ("2 Restar")
	print ("3 Multiplicar")
	print ("4 Dividir")
	print ("5 Salir \n")
	
	
	opcion = input ("Introduce opción: ")
	
	if opcion == "5":
		break
		
	elif opcion == "1":
		num1 = input("Introduce el primer número: " )
		num2 = input("Introduce el segundo número: ")
		suma = float(num1) + float(num2)
		print ("La suma es:", suma)
		
	elif opcion == "2":
		restar()
		
	elif opcion == "3":
		multiplicar()
	
	elif opcion == "4":
		dividir()
		