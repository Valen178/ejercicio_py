from clase8.Vehiculo import Vehiculo

class Main:
    # auto = Automovil("rojo", "ferrari", 10, 5)
    # print(f"Numero de ruedas: {auto.ruedas}")
    # print(f"Aceleración: {auto.aceleracion}")

    # auto.aceleracion = 20
    # print(f"Aceleración: {auto.aceleracion}")

    # auto2 = Automovil("azul", "fiat", 20, 10)
    
    # # print(f"El auto acelera a {auto2.acelera()} km")
    # print(f"El auto frena a {auto2.frena()} km")

    # autoVolador = AutomovilVolador("negro", "ford", 15, 10,True)

    # print(autoVolador.color)
    # print(autoVolador.marca)
    # print(autoVolador.velocidad)
    # print(autoVolador.aceleracion)
    # print(autoVolador.esta_volando)

    # autoVolador.aterriza()
    # autoVolador.vuela()

    # # print("El auto " + auto.conducir())
    # print("El auto " + autoVolador.conducir())

    vehiculo1 = Vehiculo("rojo","ferrari",10,20,2012)
    # print(f"Color: {vehiculo1.color}")
    # #print(f"Marca: {vehiculo1.__marca}")
    # print(f"Aceleracion: {vehiculo1.aceleracion}")
    # print(f"Velocidad: {vehiculo1.velocidad}")
    # #print(f"Anio: {vehiculo1.__anio}")

    print(f"Marca: {vehiculo1.getMarca()}")
    print(f"Marca: {vehiculo1.getAnio()}")

    vehiculo1.setAnio(2018)
    vehiculo1.setMarca("Lamborghini")

    print(f"Marca: {vehiculo1.getMarca()}")
    print(f"Marca: {vehiculo1.getAnio()}")