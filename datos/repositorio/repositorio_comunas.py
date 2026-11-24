from datos.modelos.comuna import Comuna
from datos.conexion import base_datos


def _conectar():
    if base_datos.is_closed():
        base_datos.connect()


def listado_comunas():
    """Obtiene todas las comunas habilitadas desde la base de datos."""
    try:
        _conectar()
        return list(Comuna.select().where(Comuna.habilitado == True))
    except Exception as e:
        print(f"Error al listar comunas: {e}")
        return []


def obtener_comuna_por_id(id_comuna):
    """Obtiene una comuna habilitada por su ID."""
    try:
        _conectar()
        return Comuna.get_or_none((Comuna.id_comuna == id_comuna) & (Comuna.habilitado == True))
    except Exception as e:
        print(f"Error al obtener comuna: {e}")
        return None


def guardar_comuna(comunas):
    """Guarda o actualiza una comuna en la base de datos."""
    try:
        _conectar()
        comunas.save()
        return True
    except Exception as e:
        print(f"Error al guardar comuna: {e}")
        return False


def comuna_por_nombre(nombre):
    """Busca comunas por nombre que estén habilitadas."""
    try:
        _conectar()
        return list(Comuna.select().where(
            (Comuna.nombre_comuna.contains(nombre)) & (Comuna.habilitado == True)
        ))
    except Exception as e:
        print(f"Error al buscar comuna por nombre: {e}")
        return []


def eliminar_comuna_por_id(id_comuna):
    """Realiza la baja lógica de una comuna por su ID."""
    try:
        _conectar()
        comuna = Comuna.get_or_none((Comuna.id_comuna == id_comuna) & (Comuna.habilitado == True))
        if not comuna:
            return False
        comuna.habilitado = False
        comuna.save()
        return True
    except Exception as e:
        print(f"Error al eliminar comuna: {e}")
        return False