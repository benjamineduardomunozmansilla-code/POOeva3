from datos.auxiliar import pausar
from negocio.negocio_libros import (
    obtener_tabla_libros,
    obtener_tabla_busqueda_libros,
    obtener_libro,
    crear_libro,
    editar_libro,
    eliminar_libro,
)


def mostrar_libros():
    tabla = obtener_tabla_libros()
    print("\n" + "=" * 50)
    print("        LISTADO OFICIAL DE LIBROS       ")
    print("=" * 50)
    if tabla.rowcount > 0:
        print(tabla)
    else:
        print("No hay libros registrados en la base de datos.")
    pausar()


def buscar_libro_ui():
    print("\n" + "=" * 50)
    print("          BUSCAR LIBRO POR TÍTULO       ")
    print("=" * 50)
    titulo = input("Ingrese el título o parte del título a buscar: ").strip()

    if titulo:
        tabla = obtener_tabla_busqueda_libros(titulo)
        if tabla.rowcount > 0:
            print(tabla)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")
    else:
        print("El título no puede estar vacío.")
    pausar()


def crear_libro_ui():
    print("\n" + "=" * 50)
    print("          REGISTRAR NUEVO LIBRO         ")
    print("=" * 50)
    isbn = input("Ingrese el ISBN del libro (opcional): ").strip()
    titulo = input("Ingrese el Título del libro: ").strip()
    autor = input("Ingrese el Autor del libro: ").strip()

    if titulo and autor:
        creado = crear_libro(isbn, titulo, autor)
        if creado:
            print(f"\n¡ÉXITO! El libro '{creado.titulo}' fue registrado correctamente.")
        else:
            print("\nNo se pudo guardar el libro en la base de datos.")
    else:
        print("El Título y el Autor son campos obligatorios.")
    pausar()


def editar_libro_ui():
    print("\n" + "=" * 50)
    print("            EDITAR LIBRO              ")
    print("=" * 50)
    try:
        id_libro = int(input("Ingrese el ID del libro a editar: ").strip())
    except ValueError:
        print("Debe ingresar un número de ID válido.")
        pausar()
        return

    actual = obtener_libro(id_libro)
    if not actual:
        print(f"No se encontró el libro con ID {id_libro}.")
        pausar()
        return

    isbn = input(f"Nuevo ISBN [{actual.isbn or 'Sin ISBN'}]: ").strip()
    titulo = input(f"Nuevo Título [{actual.titulo}]: ").strip()
    autor = input(f"Nuevo Autor [{actual.autor}]: ").strip()

    modificado = editar_libro(
        id_libro=id_libro,
        isbn=isbn or None,
        titulo=titulo or None,
        autor=autor or None,
    )
    if modificado:
        print("\n¡ÉXITO! Libro actualizado correctamente.")
    else:
        print("\nNo se pudo actualizar el libro.")
    pausar()


def eliminar_libro_ui():
    print("\n" + "=" * 50)
    print("            ELIMINAR LIBRO              ")
    print("=" * 50)
    try:
        id_libro = int(input("Ingrese el ID del libro que desea eliminar: ").strip())
        confirmar = input(f"¿Está seguro de eliminar el libro ID {id_libro}? (s/n): ").lower()
        if confirmar == 's':
            if eliminar_libro(id_libro):
                print("Libro deshabilitado/eliminado correctamente.")
            else:
                print("No se encontró el libro especificado.")
    except ValueError:
        print("Debe ingresar un número de ID válido.")
    pausar()