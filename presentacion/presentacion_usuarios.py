from datos.auxiliar import pausar
from negocio.negocio_usuarios import (
    obtener_tabla_usuarios,
    obtener_tabla_busqueda_usuarios,
    obtener_parametros_genero,
    obtener_usuario,
    crear_usuario,
    editar_usuario,
    eliminar_usuario,
)


def mostrar_usuarios():
    tabla = obtener_tabla_usuarios()
    print("\n" + "=" * 60)
    print("               LISTADO OFICIAL DE USUARIOS               ")
    print("=" * 60)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print("No hay usuarios registrados en la base de datos.")
    pausar()


def buscar_usuario_ui():
    print("\n" + "=" * 60)
    print("                     BUSCAR USUARIO                      ")
    print("=" * 60)
    termino = input("Ingrese nombre, apellido, RUT o correo: ").strip()
    if not termino:
        print("El criterio de búsqueda no puede estar vacío.")
        pausar()
        return

    tabla = obtener_tabla_busqueda_usuarios(termino)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print(f"No se encontraron usuarios que coincidan con '{termino}'.")
    pausar()


def crear_usuario_ui():
    print("\n" + "=" * 60)
    print("                 REGISTRAR NUEVO USUARIO                 ")
    print("=" * 60)
    rut = input("RUT (ej: 12345678-9, Enter para omitir): ").strip()
    nombre = input("Nombre (*): ").strip()
    apellido = input("Apellido (*): ").strip()
    correo = input("Correo electrónico (*): ").strip()
    id_pais = input("ID País (Enter para omitir): ").strip()
    fecha_nac = input("Fecha de nacimiento YYYY-MM-DD (Enter para omitir): ").strip()

    parametros = obtener_parametros_genero()
    if parametros:
        print("\nParámetros disponibles (ID - Código - Nombre):")
        for pid, cod, nom in parametros[:15]:
            print(f"  [{pid}] {cod} - {nom}")
    genero = input("ID Género (*, según tabla parámetros): ").strip()
    fecha_inc = input("Fecha de incorporación YYYY-MM-DD (Enter = fecha de hoy): ").strip()

    try:
        creado = crear_usuario(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            id_pais=id_pais,
            fecha_nac=fecha_nac,
            genero=genero,
            fecha_inc=fecha_inc
        )
        print(f"\n¡ÉXITO! Usuario '{creado.nombre} {creado.apellido}' creado con ID {creado.id_usuario}.")
    except (ValueError, RuntimeError) as e:
        print(f"\nError: {e}")
    pausar()


def editar_usuario_ui():
    print("\n" + "=" * 60)
    print("                     EDITAR USUARIO                      ")
    print("=" * 60)
    try:
        id_usuario = int(input("Ingrese el ID del usuario a modificar: ").strip())
    except ValueError:
        print("Debe ingresar un número de ID válido.")
        pausar()
        return

    actual = obtener_usuario(id_usuario)
    if not actual:
        print(f"No se encontró un usuario activo con ID {id_usuario}.")
        pausar()
        return

    print(f"Editando a: {actual.nombre} {actual.apellido} ({actual.correo})")
    print("Presione [ENTER] en los campos que no desee modificar.\n")

    rut = input(f"RUT [{actual.rut or 'S/N'}]: ").strip()
    nombre = input(f"Nombre [{actual.nombre}]: ").strip()
    apellido = input(f"Apellido [{actual.apellido}]: ").strip()
    correo = input(f"Correo [{actual.correo}]: ").strip()
    id_pais = input(f"ID País [{actual.pais_id or '-'}]: ").strip()
    fecha_nac = input(f"Fecha nacimiento [{actual.fecha_nacimiento or '-'}]: ").strip()
    genero = input(f"ID Género [{actual.genero}]: ").strip()

    try:
        modificado = editar_usuario(
            id_usuario=id_usuario,
            rut=rut or None,
            nombre=nombre or None,
            apellido=apellido or None,
            correo=correo or None,
            id_pais=id_pais or None,
            fecha_nac=fecha_nac or None,
            genero=genero or None
        )
        print(f"\n¡ÉXITO! Usuario ID {modificado.id_usuario} actualizado correctamente.")
    except (ValueError, RuntimeError) as e:
        print(f"\nError: {e}")
    pausar()


def eliminar_usuario_ui():
    print("\n" + "=" * 60)
    print("                    ELIMINAR USUARIO                     ")
    print("=" * 60)
    try:
        id_usuario = int(input("Ingrese el ID del usuario que desea eliminar: ").strip())
        confirmar = input(f"¿Está seguro de eliminar el usuario ID {id_usuario}? (s/n): ").strip().lower()
        if confirmar == 's':
            if eliminar_usuario(id_usuario):
                print("Usuario deshabilitado/eliminado correctamente.")
            else:
                print("No se encontró el usuario especificado.")
    except ValueError:
        print("Debe ingresar un número de ID válido.")
    pausar()
