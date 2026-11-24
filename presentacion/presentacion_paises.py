from datos.auxiliar import pausar
from negocio.negocio_paises import (
    obtener_tabla_paises,
    obtener_tabla_busqueda_paises,
    obtener_pais,
    crear_pais,
    editar_pais,
    eliminar_pais,
)


def mostrar_paises():
    tabla = obtener_tabla_paises()
    print("\n" + "=" * 45)
    print("     LISTADO OFICIAL DE PAÍSES     ")
    print("=" * 45)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print("No hay países registrados en la base de datos.")
    pausar()


def buscar_pais_ui():
    print("\n" + "=" * 45)
    print("           BUSCAR PAÍS           ")
    print("=" * 45)
    termino = input("Ingrese nombre, nacionalidad, ISO2 o ISO3: ").strip()
    if not termino:
        print("El criterio de búsqueda no puede estar vacío.")
        pausar()
        return
    tabla = obtener_tabla_busqueda_paises(termino)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print(f"No se encontraron países para '{termino}'.")
    pausar()


def crear_pais_ui():
    print("\n" + "=" * 45)
    print("       REGISTRAR NUEVO PAÍS      ")
    print("=" * 45)
    nombre = input("Ingrese el nombre del nuevo País: ").strip()
    iso2 = input("Ingrese el ISO2 (2 letras): ").strip()
    iso3 = input("Ingrese el ISO3 (3 letras): ").strip()
    nacionalidad = input("Ingrese la nacionalidad: ").strip()

    if nombre and iso2 and iso3:
        creado = crear_pais(nombre, nacionalidad, iso2, iso3)
        if creado:
            print(f"\n¡ÉXITO! El país '{creado.pais}' fue guardado correctamente.")
        else:
            print("\nNo se pudo guardar el país en la base de datos.")
    else:
        print("Nombre, ISO2 e ISO3 son campos obligatorios.")
    pausar()


def editar_pais_ui():
    print("\n" + "=" * 45)
    print("           EDITAR PAÍS           ")
    print("=" * 45)
    try:
        id_pais = int(input("Ingrese el ID del país a editar: ").strip())
    except ValueError:
        print("Debe ingresar un número de ID válido.")
        pausar()
        return

    actual = obtener_pais(id_pais)
    if not actual:
        print(f"No se encontró el país con ID {id_pais}.")
        pausar()
        return

    nombre = input(f"Nuevo Nombre [{actual.pais}]: ").strip()
    nacionalidad = input(f"Nueva Nacionalidad [{actual.nacionalidad or ''}]: ").strip()
    iso2 = input(f"Nuevo ISO2 [{actual.iso2}]: ").strip()
    iso3 = input(f"Nuevo ISO3 [{actual.iso3}]: ").strip()

    modificado = editar_pais(
        id_pais=id_pais,
        nombre=nombre or None,
        nacionalidad=nacionalidad or None,
        iso2=iso2 or None,
        iso3=iso3 or None,
    )
    if modificado:
        print("\n¡ÉXITO! País actualizado correctamente.")
    else:
        print("\nNo se pudo actualizar el país.")
    pausar()


def eliminar_pais_ui():
    print("\n" + "=" * 45)
    print("          ELIMINAR PAÍS          ")
    print("=" * 45)
    try:
        id_pais = int(input("Ingrese el ID del país a eliminar: ").strip())
        confirmar = input(f"¿Está seguro de eliminar el país ID {id_pais}? (s/n): ").strip().lower()
        if confirmar == 's':
            if eliminar_pais(id_pais):
                print("País deshabilitado/eliminado correctamente.")
            else:
                print("No se encontró el país especificado.")
    except ValueError:
        print("Debe ingresar un número de ID válido.")
    pausar()