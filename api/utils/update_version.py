import os

import tomlkit


toml_path = os.path.abspath("pyproject.toml")
init_path = os.path.abspath("api/__init__.py")

# Lee el archivo de configuración
with open(toml_path, "r") as f:
    config = tomlkit.parse(f.read())

# Obtiene la versión actual
current_version = config["tool"]["poetry"]["version"]

# Separa la versión en sus componentes
major, minor, patch = map(int, current_version.split("."))

# Incrementa el tipo de versión deseado
# Por ejemplo, para incrementar el patch
patch += 1

# Verifica si el tercer número alcanzó 99
if patch > 99:
    patch = 0
    minor += 1

    # Verifica si el segundo número alcanzó 99
    if minor > 99:
        minor = 0
        major += 1

# Actualiza la versión en el archivo de configuración
new_version = f"{major}.{minor}.{patch}"
config["tool"]["poetry"]["version"] = new_version

# Escribe el archivo de configuración preservando el orden
with open(toml_path, "w") as f:
    f.write(tomlkit.dumps(config))

# Guarda el número de versión en el archivo __init__.py
with open(init_path, "w") as f:
    f.write(f"__version__ = '{new_version}'")
