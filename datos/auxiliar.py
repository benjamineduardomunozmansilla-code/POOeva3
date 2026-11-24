import os

nombre_app = 'SISTEMA DE GESTIÓN DE BIBLIOTECA'
version_app = 'v2.0 - POO & MVC'

# Estructura del Menú Principal
main_menu = {
    '1': 'Gestión de Comunas',
    '2': 'Gestión de Países',
    '3': 'Gestión de Libros',
    '4': 'Gestión de Autores',
    '5': 'Gestión de Usuarios',
    '6': 'Salir del Sistema'
}

# Submenú Comunas
menu_comunas = {
    '1': 'Listar todas las Comunas',
    '2': 'Buscar Comuna por Nombre',
    '3': 'Registrar Nueva Comuna',
    '4': 'Editar Comuna',
    '5': 'Eliminar Comuna',
    '6': 'Volver al Menú Principal'
}

# Submenú Países
menu_paises = {
    '1': 'Listar Países',
    '2': 'Buscar País',
    '3': 'Registrar Nuevo País',
    '4': 'Editar País',
    '5': 'Eliminar País',
    '6': 'Volver al Menú Principal'
}

# Submenú Libros
menu_libros = {
    '1': 'Listar todos los Libros',
    '2': 'Buscar Libro por Título',
    '3': 'Registrar Nuevo Libro',
    '4': 'Editar Libro',
    '5': 'Eliminar Libro',
    '6': 'Volver al Menú Principal'
}

# Submenú Autores
menu_autores = {
    '1': 'Listar todos los Autores',
    '2': 'Buscar Autor',
    '3': 'Registrar Nuevo Autor',
    '4': 'Editar Autor',
    '5': 'Eliminar Autor',
    '6': 'Volver al Menú Principal'
}

# Submenú Usuarios (CRUD completo)
menu_usuarios = {
    '1': 'Listar todos los Usuarios',
    '2': 'Buscar Usuario',
    '3': 'Registrar Nuevo Usuario',
    '4': 'Editar Usuario',
    '5': 'Eliminar Usuario',
    '6': 'Volver al Menú Principal'
}

mensaje_error_orm = 'Ha ocurrido un error en la base de datos: '


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa la ejecución para que el usuario pueda leer la respuesta."""
    input("\nPresione [ENTER] para continuar...")