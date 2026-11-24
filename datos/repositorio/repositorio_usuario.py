from datos.modelos.usuario import Usuario
from datos.modelos.pais import Pais
from datos.conexion import base_datos


def _conectar():
    if base_datos.is_closed():
        base_datos.connect()


def listado_usuarios():
    """Obtiene todos los usuarios habilitados."""
    try:
        _conectar()
        return list(Usuario.select().where(Usuario.habilitado == True))
    except Exception as e:
        print(f"Error al listar usuarios: {e}")
        return []


def buscar_usuarios(termino):
    """Busca usuarios habilitados por nombre, apellido, RUT o correo."""
    try:
        _conectar()
        filtro = (
            (Usuario.nombre.contains(termino)) |
            (Usuario.apellido.contains(termino)) |
            (Usuario.rut.contains(termino)) |
            (Usuario.correo.contains(termino))
        )
        return list(Usuario.select().where(filtro & (Usuario.habilitado == True)))
    except Exception as e:
        print(f"Error al buscar usuarios: {e}")
        return []


def obtener_usuario_por_id(id_usuario):
    """Obtiene un usuario habilitado por su ID."""
    try:
        _conectar()
        return Usuario.get_or_none(
            (Usuario.id_usuario == id_usuario) & (Usuario.habilitado == True)
        )
    except Exception as e:
        print(f"Error al obtener usuario: {e}")
        return None


def existe_correo(correo, excluir_id=None):
    """Verifica si el correo ya está registrado en otro usuario activo."""
    try:
        _conectar()
        query = Usuario.select().where(
            (Usuario.correo == correo) & (Usuario.habilitado == True)
        )
        if excluir_id is not None:
            query = query.where(Usuario.id_usuario != excluir_id)
        return query.exists()
    except Exception as e:
        print(f"Error al verificar correo: {e}")
        return False


def existe_pais(id_pais):
    """Valida que el ID de país exista en la tabla paises."""
    try:
        _conectar()
        return Pais.select().where(Pais.id_pais == id_pais).exists()
    except Exception:
        return False


def existe_parametro(id_parametro):
    """Valida que el ID de género exista en la tabla parametros."""
    try:
        _conectar()
        cursor = base_datos.execute_sql(
            "SELECT 1 FROM parametros WHERE id_parametro = %s AND habilitado = 1 LIMIT 1",
            (id_parametro,)
        )
        return cursor.fetchone() is not None
    except Exception:
        return False


def listar_generos_disponibles():
    """Obtiene los parámetros disponibles para mostrar opciones de género al usuario."""
    try:
        _conectar()
        cursor = base_datos.execute_sql(
            "SELECT id_parametro, codigo, parametro FROM parametros WHERE habilitado = 1 ORDER BY id_parametro"
        )
        return cursor.fetchall()
    except Exception:
        return []


def guardar_usuario(usuario):
    """Inserta o actualiza un usuario en la base de datos."""
    try:
        _conectar()
        usuario.save()
        return True
    except Exception as e:
        print(f"Error al guardar usuario: {e}")
        return False


def eliminar_usuario_por_id(id_usuario):
    """Realiza la baja lógica de un usuario (habilitado = False)."""
    try:
        _conectar()
        usuario = Usuario.get_or_none(
            (Usuario.id_usuario == id_usuario) & (Usuario.habilitado == True)
        )
        if not usuario:
            return False
        usuario.habilitado = False
        usuario.save()
        return True
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        return False