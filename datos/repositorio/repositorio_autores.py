from datos.modelos.autor import Autor
from datos.conexion import base_datos


def _conectar():
    if base_datos.is_closed():
        base_datos.connect()


def listado_autores():
    """Lista autores activos (o todos si la columna habilitado no existe en BD)."""
    try:
        _conectar()
        try:
            return list(Autor.select().where(Autor.habilitado == True))
        except Exception:
            return list(Autor.select())
    except Exception as e:
        print(f"Error al listar autores: {e}")
        return []


def buscar_autores(termino):
    """Busca autores por nombre o pseudónimo."""
    try:
        _conectar()
        condicion = (Autor.nombre.contains(termino)) | (Autor.pseudonimo.contains(termino))
        try:
            return list(Autor.select().where(condicion & (Autor.habilitado == True)))
        except Exception:
            return list(Autor.select().where(condicion))
    except Exception as e:
        print(f"Error al buscar autores: {e}")
        return []


def obtener_autor_por_id(id_autor):
    """Obtiene un autor por su ID."""
    try:
        _conectar()
        return Autor.get_or_none(Autor.id_autor == id_autor)
    except Exception as e:
        print(f"Error al obtener autor: {e}")
        return None


def guardar_autor(autor):
    """Guarda o actualiza un autor en la base de datos."""
    try:
        _conectar()
        autor.save()
        return True
    except Exception as e:
        print(f"Error al guardar autor: {e}")
        return False


def eliminar_autor_por_id(id_autor):
    """Deshabilita un autor si tiene campo habilitado, o elimina si no."""
    try:
        _conectar()
        autor = Autor.get_or_none(Autor.id_autor == id_autor)
        if not autor:
            return False
        try:
            autor.habilitado = False
            autor.save()
        except Exception:
            autor.delete_instance()
        return True
    except Exception as e:
        print(f"Error al eliminar autor: {e}")
        return False