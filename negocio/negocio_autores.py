from datetime import datetime
from prettytable import PrettyTable
from datos.modelos.autor import Autor
from datos.repositorio.repositorio_autores import (
    listado_autores,
    buscar_autores,
    obtener_autor_por_id,
    guardar_autor,
    eliminar_autor_por_id,
)


def _parsear_fecha_opcional(fecha_str):
    if not fecha_str:
        return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(fecha_str.strip(), fmt).date()
        except ValueError:
            continue
    raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")


def construir_tabla_autores(autores):
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre', 'Pseudónimo', 'ID País', 'Nacimiento', 'Defunción']
    for a in autores:
        tabla.add_row([
            a.id_autor,
            a.nombre or '-',
            a.pseudonimo or '-',
            a.pais if a.pais else '-',
            str(a.fecha_nacimiento) if a.fecha_nacimiento else '-',
            str(a.fecha_defuncion) if a.fecha_defuncion else '-',
        ])
    return tabla


def obtener_tabla_autores():
    return construir_tabla_autores(listado_autores())


def obtener_tabla_busqueda_autores(termino):
    return construir_tabla_autores(buscar_autores(termino.strip()))


def obtener_autor(id_autor):
    return obtener_autor_por_id(id_autor)


def crear_autor(nombre, pseudonimo=None, id_pais=None, fecha_nac=None, fecha_def=None):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre del autor es obligatorio.")
    pais_val = int(id_pais) if id_pais and id_pais.strip().isdigit() else None
    fnac_val = _parsear_fecha_opcional(fecha_nac)
    fdef_val = _parsear_fecha_opcional(fecha_def)

    nuevo = Autor(
        nombre=nombre.strip(),
        pseudonimo=pseudonimo.strip() if pseudonimo and pseudonimo.strip() else None,
        pais=pais_val,
        fecha_nacimiento=fnac_val,
        fecha_defuncion=fdef_val,
        habilitado=True,
    )
    return nuevo if guardar_autor(nuevo) else None


def editar_autor(id_autor, nombre=None, pseudonimo=None, id_pais=None, fecha_nac=None, fecha_def=None):
    autor = obtener_autor_por_id(id_autor)
    if not autor:
        return None
    if nombre:
        autor.nombre = nombre.strip()
    if pseudonimo is not None and pseudonimo.strip() != '':
        autor.pseudonimo = pseudonimo.strip()
    if id_pais is not None and id_pais.strip() != '':
        if not id_pais.strip().isdigit():
            raise ValueError("El ID de país debe ser numérico.")
        autor.pais = int(id_pais.strip())
    if fecha_nac is not None and fecha_nac.strip() != '':
        autor.fecha_nacimiento = _parsear_fecha_opcional(fecha_nac)
    if fecha_def is not None and fecha_def.strip() != '':
        autor.fecha_defuncion = _parsear_fecha_opcional(fecha_def)
    return autor if guardar_autor(autor) else None


def eliminar_autor(id_autor):
    return eliminar_autor_por_id(id_autor)