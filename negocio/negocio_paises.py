from prettytable import PrettyTable
from datos.modelos.pais import Pais
from datos.repositorio.repositorio_paises import (
    listado_paises,
    buscar_paises,
    obtener_pais_por_id,
    guardar_pais,
    eliminar_pais_por_id,
)


def construir_tabla_paises(paises):
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'País', 'Nacionalidad', 'ISO2', 'ISO3', 'Estado']
    for p in paises:
        estado = "Habilitado" if getattr(p, 'habilitado', True) else "Deshabilitado"
        tabla.add_row([p.id_pais, p.pais, p.nacionalidad or '-', p.iso2, p.iso3, estado])
    return tabla


def obtener_tabla_paises():
    return construir_tabla_paises(listado_paises())


def obtener_tabla_busqueda_paises(termino):
    return construir_tabla_paises(buscar_paises(termino.strip()))


def obtener_pais(id_pais):
    return obtener_pais_por_id(id_pais)


def crear_pais(nombre, nacionalidad, iso2, iso3):
    nuevo = Pais(
        pais=nombre.strip(),
        nacionalidad=nacionalidad.strip(),
        iso2=iso2.strip().upper()[:2],
        iso3=iso3.strip().upper()[:3],
        habilitado=True,
    )
    return nuevo if guardar_pais(nuevo) else None


def editar_pais(id_pais, nombre=None, nacionalidad=None, iso2=None, iso3=None):
    pais = obtener_pais_por_id(id_pais)
    if not pais:
        return None
    if nombre:
        pais.pais = nombre.strip()
    if nacionalidad:
        pais.nacionalidad = nacionalidad.strip()
    if iso2:
        pais.iso2 = iso2.strip().upper()[:2]
    if iso3:
        pais.iso3 = iso3.strip().upper()[:3]
    return pais if guardar_pais(pais) else None


def eliminar_pais(id_pais):
    return eliminar_pais_por_id(id_pais)