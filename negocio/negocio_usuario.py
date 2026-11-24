import re
from prettytable import PrettyTable
from datos.modelos.usuario import Usuario
from datos.repositorio.repositorio_usuarios import (
    listado_usuarios,
    buscar_usuarios,
    obtener_usuario_por_id,
    guardar_usuario,
    eliminar_usuario_por_id,
)


def _limpiar_rut(rut):
    return re.sub(r"[^0-9kK]", "", rut or "").upper()


def _validar_rut_chileno(rut):
    limpio = _limpiar_rut(rut)
    if len(limpio) < 2:
        return False
    cuerpo, dv = limpio[:-1], limpio[-1]
    if not cuerpo.isdigit():
        return False
    suma = 0
    multiplicador = 2
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1
    resto = 11 - (suma % 11)
    dv_esperado = "0" if resto == 11 else ("K" if resto == 10 else str(resto))
    return dv == dv_esperado


def _formatear_rut(rut):
    limpio = _limpiar_rut(rut)
    if len(limpio) < 2:
        return rut.strip()
    cuerpo, dv = limpio[:-1], limpio[-1]
    cuerpo_formateado = f"{int(cuerpo):,}".replace(",", ".")
    return f"{cuerpo_formateado}-{dv}"


def _validar_correo(correo):
    if not correo:
        return True
    patron = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(patron, correo.strip()) is not None


def construir_tabla_usuarios(usuarios):
    tabla = PrettyTable()
    tabla.field_names = ["ID", "RUT", "Nombre", "Apellido", "Correo", "Estado"]
    for u in usuarios:
        nombre = getattr(u, "nombre", None) or getattr(u, "nombres", None) or "-"
        apellido = getattr(u, "apellido", None) or getattr(u, "apellidos", None) or "-"
        correo = getattr(u, "correo", None) or getattr(u, "email", None) or "-"
        estado = "Habilitado" if getattr(u, "habilitado", True) else "Deshabilitado"
        tabla.add_row([
            getattr(u, "id_usuario", None) or getattr(u, "id", "-"),
            getattr(u, "rut", "-"),
            nombre,
            apellido,
            correo,
            estado,
        ])
    return tabla


def obtener_tabla_usuarios():
    return construir_tabla_usuarios(listado_usuarios())


def obtener_tabla_busqueda_usuarios(termino):
    return construir_tabla_usuarios(buscar_usuarios(termino.strip()))


def obtener_usuario(id_usuario):
    return obtener_usuario_por_id(id_usuario)


def crear_usuario(rut, nombre, apellido, correo=None):
    if not _validar_rut_chileno(rut):
        raise ValueError("El RUT ingresado no es válido.")
    if not nombre or not nombre.strip():
        raise ValueError("El nombre es obligatorio.")
    if not apellido or not apellido.strip():
        raise ValueError("El apellido es obligatorio.")
    if not _validar_correo(correo):
        raise ValueError("El formato del correo electrónico no es válido.")

    nuevo = Usuario()
    if hasattr(nuevo, "rut"):
        nuevo.rut = _formatear_rut(rut)
    if hasattr(nuevo, "nombre"):
        nuevo.nombre = nombre.strip()
    elif hasattr(nuevo, "nombres"):
        nuevo.nombres = nombre.strip()
    if hasattr(nuevo, "apellido"):
        nuevo.apellido = apellido.strip()
    elif hasattr(nuevo, "apellidos"):
        nuevo.apellidos = apellido.strip()
    if correo and correo.strip():
        if hasattr(nuevo, "correo"):
            nuevo.correo = correo.strip()
        elif hasattr(nuevo, "email"):
            nuevo.email = correo.strip()
    if hasattr(nuevo, "habilitado"):
        nuevo.habilitado = True

    return nuevo if guardar_usuario(nuevo) else None


def editar_usuario(id_usuario, rut=None, nombre=None, apellido=None, correo=None):
    usuario = obtener_usuario_por_id(id_usuario)
    if not usuario:
        return None

    if rut is not None and rut.strip() != "":
        if not _validar_rut_chileno(rut):
            raise ValueError("El RUT ingresado no es válido.")
        if hasattr(usuario, "rut"):
            usuario.rut = _formatear_rut(rut)

    if nombre is not None and nombre.strip() != "":
        if hasattr(usuario, "nombre"):
            usuario.nombre = nombre.strip()
        elif hasattr(usuario, "nombres"):
            usuario.nombres = nombre.strip()

    if apellido is not None and apellido.strip() != "":
        if hasattr(usuario, "apellido"):
            usuario.apellido = apellido.strip()
        elif hasattr(usuario, "apellidos"):
            usuario.apellidos = apellido.strip()

    if correo is not None and correo.strip() != "":
        if not _validar_correo(correo):
            raise ValueError("El formato del correo electrónico no es válido.")
        if hasattr(usuario, "correo"):
            usuario.correo = correo.strip()
        elif hasattr(usuario, "email"):
            usuario.email = correo.strip()

    return usuario if guardar_usuario(usuario) else None


def eliminar_usuario(id_usuario):
    return eliminar_usuario_por_id(id_usuario)