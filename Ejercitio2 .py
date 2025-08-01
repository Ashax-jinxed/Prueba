import mysql.connector

def conectar():
    """Establece la conexión a la base de datos MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mandrake99",
        database="clientes_bayma"
    )

def listar_clientes_activos():
    """Lista los clientes activos dados de alta en los últimos 60 días."""
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = """
    SELECT * FROM clientes
    WHERE activo = 1 AND fecha_alta >= CURDATE() - INTERVAL 60 DAY
    ORDER BY fecha_alta DESC
    """
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    print("\nClientes activos dados de alta en los últimos 60 días:")
    if resultados:
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}, Fecha Alta: {fila[3]}, Activo: {fila[4]}")
    else:
        print("No hay clientes activos recientes.")
    cursor.close()
    conexion.close()

def insertar_cliente():
    """Agrega un nuevo cliente a la base de datos."""
    nombre = input("Ingrese el nombre del cliente: ").strip()
    email = input("Ingrese el email del cliente: ").strip()
    from datetime import date
    fecha_alta = date.today()
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "INSERT INTO clientes (nombre, email, fecha_alta, activo) VALUES (%s, %s, %s, 1)"
    valores = (nombre, email, fecha_alta)
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print(f"Cliente '{nombre}' insertado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar cliente: {err}")
    cursor.close()
    conexion.close()

def desactivar_cliente():
    """Desactiva un cliente por su email."""
    email = input("Ingrese el email del cliente a desactivar: ").strip()
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = "UPDATE clientes SET activo = 0 WHERE email = %s"
    try:
        cursor.execute(consulta, (email,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"Cliente con email '{email}' desactivado correctamente.")
        else:
            print(f"No se encontró cliente con email '{email}'.")
    except mysql.connector.Error as err:
        print(f"Error al desactivar cliente: {err}")
    cursor.close()
    conexion.close()

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    print("Bienvenido al sistema de gestión de clientes.")
    while True:
        print("\nSelecciona una opción:")
        print("1 - Listar clientes activos dados de alta en los últimos 60 días")
        print("2 - Insertar un nuevo cliente")
        print("3 - Desactivar un cliente por email")
        print("0 - Salir")
        opcion = input("Ingresa el número de opción: ").strip()
        if opcion == "1":
            listar_clientes_activos()
        elif opcion == "2":
            insertar_cliente()
        elif opcion == "3":
            desactivar_cliente()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
