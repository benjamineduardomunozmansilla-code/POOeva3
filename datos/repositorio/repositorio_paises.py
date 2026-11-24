from datos.modelos.pais import Pais
from datos.conexion import base_datos


def _conectar():
    if base_datos.is_closed():
        base_datos.connect()


def listado_paises():
    """Obtiene todos los países habilitados desde la base de datos."""
    try:
        _conectar()
        return list(Pais.select().where(Pais.habilitado == True))
    except Exception as e:
        print(f"Error al listar países: {e}")
        return []


def buscar_paises(termino):
    """Busca países habilitados por nombre, nacionalidad, iso2 o iso3."""
    try:
        _conectar()
        condicion = (
            (Pais.pais.contains(termino)) |
            (Pais.nacionalidad.contains(termino)) |
            (Pais.iso2.contains(termino)) |
            (Pais.iso3.contains(termino))
        )
        return list(Pais.select().where(condicion & (Pais.habilitado == True)))
    except Exception as e:
        print(f"Error al buscar países: {e}")
        return []


def obtener_pais_por_id(id_pais):
    """Obtiene un país habilitado por su ID."""
    try:
        _conectar()
        return Pais.get_or_none((Pais.id_pais == id_pais) & (Pais.habilitado == True))
    except Exception as e:
        print(f"Error al obtener país: {e}")
        return None


def guardar_pais(pais):
    """Guarda o actualiza un país en la base de datos."""
    try:
        _conectar()
        pais.save()
        return True
    except Exception as e:
        print(f"Error al guardar país: {e}")
        return False


def eliminar_pais_por_id(id_pais):
    """Realiza la baja lógica de un país por su ID."""
    try:
        _conectar()
        pais = Pais.get_or_none((Pais.id_pais == id_pais) & (Pais.habilitado == True))
        if not pais:
            return False
        pais.habilitado = False
        pais.save()
        return True
    except Exception as e:
        print(f"Error al eliminar país: {e}")
        return False