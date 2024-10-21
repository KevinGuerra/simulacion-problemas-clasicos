
# Proyecto Final de Sistemas Operativos 1 - UMG

Este repositorio contiene la simulación de dos problemas clásicos de la concurrencia en sistemas operativos:

1. **Algoritmo de Dekker**  
   Simulación del algoritmo de Dekker para la solución del problema de la exclusión mutua.

   Ejecuta el algoritmo de Dekker:
   ```bash
   python -m simulacion_problemas_clasicos dekker
   ```

2. **Problema de los Filósofos Comensales**  
   Implementación del problema clásico de sincronización de los filósofos comensales.

   Ejecuta la simulación de los filósofos comensales:
   ```bash
   python -m simulacion_problemas_clasicos filosofos_comensales
   ```

## Entorno Virtual (VENV)

Para aislar las dependencias del proyecto, usa un entorno virtual con Python:

1. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Para verificar que estás dentro del entorno virtual:
   ```bash
   which python
   ```

   Debería mostrar una ruta similar a:
   ```bash
   simulacion-problemas-clasico/.venv/bin/python
   ```

## Gestor de Paquetes

1. Inicializa el proyecto con `pip` instalando las dependencias listadas en `requirements.txt`:
   ```bash
   python -m pip install -r requirements.txt
   ```

2. Instala el proyecto en modo editable para facilitar el desarrollo:
   ```bash
   pip install -e .
   ```

## Linting y Tipado

Este proyecto utiliza **Ruff** para garantizar la calidad del código y las convenciones de estilo. Ejecuta el siguiente comando para realizar una revisión de linting:

```bash
ruff check
```

### Configuración en Visual Studio Code

Para mejorar la experiencia de desarrollo en VSCode, instala las siguientes extensiones:

- **Python** *(ms-python.python)*
- **Pylance** *(ms-python.vscode-pylance)*

#### Configuración del entorno de desarrollo

1. Abre la configuración de usuario en formato JSON:
   - Presiona: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Selecciona: `Preferences: Open User Settings (JSON)`

2. Agrega las siguientes configuraciones para habilitar Ruff y Pylance:
   ```json
   {
       "python.linting.enabled": true,
       "python.linting.ruffEnabled": true,
       "python.linting.pylintEnabled": false,
       "python.languageServer": "Pylance"
   }
   ```

## Formateo del Código

Este proyecto utiliza **Black** como formateador de código.

### Configuración en Visual Studio Code

1. Instala la extensión:
   - **Black Formatter** *(ms-python.black-formatter)*

2. Configura el formato automático al guardar archivos:
   - Presiona: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Selecciona: `Preferences: Open User Settings (JSON)`

3. Agrega la siguiente configuración para el formateo en Python:
   ```json
   {
       "[python]": {
           "editor.defaultFormatter": "ms-python.black-formatter",
           "editor.formatOnSave": true
       }
   }
   ```
