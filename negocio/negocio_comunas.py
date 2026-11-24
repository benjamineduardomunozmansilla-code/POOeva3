from prettytable import PrettyTable
from datos.modelos.comuna import Comuna
from datos.repositorio.repositorio_comunas import (
    listado_comunas,
    obtener_comuna_por_id,
    guardar_comuna,
    comuna_por_nombre,
)


def cargar_comunas(tabla: PrettyTable):
    comunas = listado_comunas()
    tabla.field_names = ['Id', 'Código', 'Comuna']

    if comunas:
        for comuna in comunas:
            tabla.add_row([comuna.id_comuna, comuna.codigo_comuna, comuna.nombre_comuna])

    return tabla


def buscar_comunas(tabla: PrettyTable, nombre):
    comunas = comuna_por_nombre(nombre)
    tabla.field_names = ['Id', 'Código', 'Comuna']

    if comunas:
        for comuna in comunas:
            tabla.add_row([comuna.id_comuna, comuna.codigo_comuna, comuna.nombre_comuna])

    return tabla


def obtener_comuna(id_comuna):
    return obtener_comuna_por_id(id_comuna)


def crear_comuna(codigo, nombre):
    nueva_comuna = Comuna()
    nueva_comuna.codigo_comuna = codigo
    nueva_comuna.nombre_comuna = nombre
    nueva_comuna.habilitado = True

    comuna = guardar_comuna(nueva_comuna)
    if comuna == 1 or nueva_comuna.id_comuna:
        print(f'Se ha guardado la comuna {nueva_comuna.nombre_comuna} con ID: {nueva_comuna.id_comuna}')
        return True
    return False


def editar_comuna(id_comuna, codigo=None, nombre=None):
    comuna = obtener_comuna_por_id(id_comuna)
    if not comuna:
        return None
    if codigo:
        comuna.codigo_comuna = codigo.strip()
    if nombre:
        comuna.nombre_comuna = nombre.strip()
    return comuna if guardar_comuna(comuna) else None