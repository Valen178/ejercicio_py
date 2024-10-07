import sqlite3
from AutomovilVolador import AutomovilVolador
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

    # vehiculo1 = Vehiculo("rojo","ferrari",10,20,2012)
    # # print(f"Color: {vehiculo1.color}")
    # # #print(f"Marca: {vehiculo1.__marca}")
    # # print(f"Aceleracion: {vehiculo1.aceleracion}")
    # # print(f"Velocidad: {vehiculo1.velocidad}")
    # # #print(f"Anio: {vehiculo1.__anio}")

    # print(f"Marca: {vehiculo1.getMarca()}")
    # print(f"Marca: {vehiculo1.getAnio()}")

    # vehiculo1.setAnio(2018)
    # vehiculo1.setMarca("Lamborghini")

    # print(f"Marca: {vehiculo1.getMarca()}")
    # print(f"Marca: {vehiculo1.getAnio()}")

    # vehiculo1 = Vehiculo("rojo","ferrari",10,20,2012)
    # autoVolador = AutomovilVolador("negro", "ford", 15, 10,True)

    # vehiculo1.datos()
    # autoVolador.datos()

    # conexion = sqlite3.connect("base_datos/mi_bd.db")
    # cursor = conexion.cursor()

    # create_table_query = """
    # CREATE TABLE vehiculo (
    # id INTEGER PRIMARY KEY,
    # marca TEXT,
    # ruedas INTEGER,
    # color TEXT,
    # aceleracion INTEGER,
    # velocidad INTEGER,
    # anio TEXT
    # )
    # """
    # cursor.execute(create_table_query)

    # conexion.commit()
    # cursor.close()
    # conexion.close()

    # vehicle_data = (1, "Toyota", 4, "Red", 8, 180, "2020")

    # conexion = sqlite3.connect("base_datos/mi_bd.db")
    # cursor = conexion.cursor()

    # insert_query = """
    # INSERT INTO vehiculo (id, marca, ruedas, color, aceleracion, velocidad, anio) 
    # VALUES (?, ?, ?, ?, ?, ?, ?);
    # """

    # cursor.execute(insert_query, vehicle_data)

    # conexion.commit()

    # cursor.close()
    # conexion.close()

    conexion = sqlite3.connect("base_datos/mi_bd.db")
    cursor = conexion.cursor()

    select_query = "SELECT * FROM vehiculo;"

    cursor.execute(select_query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conexion.close()