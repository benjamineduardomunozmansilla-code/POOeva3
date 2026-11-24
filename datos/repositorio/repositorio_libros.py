from datos.modelos.libro import Libro
from datos.conexion import base_datos


def _conectar():
    if base_datos.is_closed():
        base_datos.connect()


def listado_libros():
    """Obtiene todos los libros habilitados desde la base de datos."""
    try:
        _conectar()
        return list(Libro.select().where(Libro.habilitado == True))
    except Exception as e:
        print(f"Error al listar libros: {e}")
        return []


def obtener_libro_por_id(id_libro):
    """Obtiene un libro habilitado por su ID."""
    try:
        _conectar()
        return Libro.get_or_none((Libro.id_libro == id_libro) & (Libro.habilitado == True))
    except Exception as e:
        print(f"Error al obtener libro: {e}")
        return None


def guardar_libro(libro):
    """Guarda o actualiza un libro en la base de datos."""
    try:
        _conectar()
        libro.save()
        return True
    except Exception as e:
        print(f"Error al guardar libro: {e}")
        return False


def buscar_libro_por_titulo(titulo):
    """Busca libros por coincidencia en el título."""
    try:
        _conectar()
        return list(Libro.select().where(
            (Libro.titulo.contains(titulo)) & (Libro.habilitado == True)
        ))
    except Exception as e:
        print(f"Error al buscar libro: {e}")
        return []


def eliminar_libro_por_id(id_libro):
    """Realiza la baja lógica de un libro por su ID."""
    try:
        _conectar()
        libro = Libro.get_or_none((Libro.id_libro == id_libro) & (Libro.habilitado == True))
        if not libro:
            return False
        libro.habilitado = False
        libro.save()
        return True
    except Exception as e:
        print(f"Error al eliminar libro: {e}")
        return False