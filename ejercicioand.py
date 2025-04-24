

#este programa nos ayudara a aolicar los docuentos por el numero de compras realizadas
#si se realiza una compra de 10 relojes se hara un descuento del 10%
#si se realiza una compra de 20 relojes se hara un descuento del 20%

reloj = int(input("ingresar numero de relojes"))
precio_unitario= int(input("ingresar precio del reloj"))

if reloj >= 10:
    descuento = 0.10

elif reloj >= 20:
    descuento = 0.20

subtotal= reloj * precio_unitario 
total= (subtotal*descuento)

print(f"|subtotal|{subtotal}")
print(f"descuento aplicado: {descuento*100}%")
print(f"|total a pagar:|{total}")