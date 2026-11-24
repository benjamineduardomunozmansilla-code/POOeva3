from prettytable import PrettyTable
from datos.modelos.libro import Libro
from datos.repositorio.repositorio_libros import (
    listado_libros,
    obtener_libro_por_id,
    guardar_libro,
    buscar_libro_por_titulo,
    eliminar_libro_por_id,
)


def construir_tabla_libros(libros):
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'ISBN', 'Título', 'Autor', 'Estado']
    for l in libros:
        estado = "Disponible" if getattr(l, 'habilitado', True) else "No disponible"
        tabla.add_row([l.id_libro, l.isbn or 'S/N', l.titulo, l.autor, estado])
    return tabla


def obtener_tabla_libros():
    return construir_tabla_libros(listado_libros())


def obtener_tabla_busqueda_libros(titulo):
    return construir_tabla_libros(buscar_libro_por_titulo(titulo.strip()))


def obtener_libro(id_libro):
    return obtener_libro_por_id(id_libro)


def crear_libro(isbn, titulo, autor):
    nuevo = Libro(
        isbn=isbn.strip() if isbn and isbn.strip() else 'Sin ISBN',
        titulo=titulo.strip(),
        autor=autor.strip(),
        habilitado=True,
    )
    return nuevo if guardar_autor_ok(nuevo) else None


def guardar_autor_ok(libro):
    return guardar_libro(libro)


def editar_libro(id_libro, isbn=None, titulo=None, autor=None):
    libro = obtener_libro_por_id(id_libro)
    if not libro:
        return None
    if isbn is not None and isbn.strip() != '':
        libro.isbn = isbn.strip()
    if titulo:
        libro.titulo = titulo.strip()
    if autor:
        libro.autor = autor.strip()
    return libro if guardar_libro(libro) else None


def eliminar_libro(id_libro):
    return eliminar_libro_por_id(id_libro)