from datos.auxiliar import pausar
from negocio.negocio_autores import (
    obtener_tabla_autores,
    obtener_tabla_busqueda_autores,
    obtener_autor,
    crear_autor,
    editar_autor,
    eliminar_autor,
)


def mostrar_autores():
    tabla = obtener_tabla_autores()
    print("\n" + "=" * 55)
    print("            LISTADO OFICIAL DE AUTORES           ")
    print("=" * 55)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print("No hay autores registrados en la base de datos.")
    pausar()


def buscar_autor_ui():
    print("\n" + "=" * 55)
    print("                  BUSCAR AUTOR                   ")
    print("=" * 55)
    termino = input("Ingrese nombre o pseudónimo: ").strip()
    if not termino:
        print("El criterio de búsqueda no puede estar vacío.")
        pausar()
        return
    tabla = obtener_tabla_busqueda_autores(termino)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print(f"No se encontraron autores para '{termino}'.")
    pausar()


def crear_autor_ui():
    print("\n" + "=" * 55)
    print("               REGISTRAR NUEVO AUTOR             ")
    print("=" * 55)
    nombre = input("Nombre del autor (*): ").strip()
    pseudonimo = input("Pseudónimo (opcional): ").strip()
    id_pais = input("ID País (opcional): ").strip()
    fecha_nac = input("Fecha nacimiento YYYY-MM-DD (opcional): ").strip()
    fecha_def = input("Fecha defunción YYYY-MM-DD (opcional): ").strip()

    try:
        creado = crear_autor(nombre, pseudonimo, id_pais, fecha_nac, fecha_def)
        if creado:
            print(f"\n¡ÉXITO! Autor '{creado.nombre}' registrado con ID {creado.id_autor}.")
        else:
            print("\nNo se pudo registrar el autor.")
    except ValueError as e:
        print(f"\nError: {e}")
    pausar()


def editar_autor_ui():
    print("\n" + "=" * 55)
    print("                  EDITAR AUTOR                   ")
    print("=" * 55)
    try:
        id_autor = int(input("Ingrese el ID del autor a editar: ").strip())
    except ValueError:
        print("Debe ingresar un número de ID válido.")
        pausar()
        return

    actual = obtener_autor(id_autor)
    if not actual:
        print(f"No se encontró el autor con ID {id_autor}.")
        pausar()
        return

    nombre = input(f"Nuevo Nombre [{actual.nombre or ''}]: ").strip()
    pseudonimo = input(f"Nuevo Pseudónimo [{actual.pseudonimo or ''}]: ").strip()
    id_pais = input(f"Nuevo ID País [{actual.pais or ''}]: ").strip()
    fecha_nac = input(f"Nueva F. Nacimiento [{actual.fecha_nacimiento or ''}]: ").strip()
    fecha_def = input(f"Nueva F. Defunción [{actual.fecha_defuncion or ''}]: ").strip()

    try:
        modificado = editar_autor(
            id_autor=id_autor,
            nombre=nombre or None,
            pseudonimo=pseudonimo or None,
            id_pais=id_pais or None,
            fecha_nac=fecha_nac or None,
            fecha_def=fecha_def or None,
        )
        if modificado:
            print("\n¡ÉXITO! Autor actualizado correctamente.")
        else:
            print("\nNo se pudo actualizar el autor.")
    except ValueError as e:
        print(f"\nError: {e}")
    pausar()


def eliminar_autor_ui():
    print("\n" + "=" * 55)
    print("                 ELIMINAR AUTOR                  ")
    print("=" * 55)
    try:
        id_autor = int(input("Ingrese el ID del autor a eliminar: ").strip())
        confirmar = input(f"¿Está seguro de eliminar el autor ID {id_autor}? (s/n): ").strip().lower()
        if confirmar == 's':
            if eliminar_autor(id_autor):
                print("Autor eliminado/deshabilitado correctamente.")
            else:
                print("No se encontró el autor especificado.")
    except ValueError:
        print("Debe ingresar un número de ID válido.")
    pausar()