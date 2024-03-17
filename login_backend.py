# login_backend.py

usuarios_registrados = {
    'bandev': {'contraseña': '123456', 'roles': ['cifrado_moderno']},
    'nakamura': {'contraseña': '123456', 'roles': ['cifrado_clasico']},
    'xamira': {'contraseña': '123456', 'roles': ['cifrado_clasico', 'cifrado_moderno', 'todos_los_cifrados']},
    'eduardo': {'contraseña': 'pass789', 'roles': ['cifrado_clasico', 'cifrado_moderno', 'todos_los_cifrados']}
}

def verificar_usuario(usuario, contraseña):
    """Verificar las credenciales de un usuario existente y devuelve los roles si es correcto."""
    datos_usuario = usuarios_registrados.get(usuario)
    if datos_usuario and datos_usuario['contraseña'] == contraseña:
        return datos_usuario['roles']
    return None

