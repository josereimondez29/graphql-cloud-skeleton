# graphql-cloud-skeleton

Skeleton básico para una API GraphQL usando Django, ASGI y Uvicorn.

## Descripción

Este proyecto es un punto de partida para construir APIs GraphQL modernas en Python con Django como backend, ASGI para soporte async y Uvicorn como servidor ASGI.

## Tecnologías

- Python 3.12+
- Django
- Strawberry GraphQL
- ASGI
- Uvicorn
- Virtualenv

## Instalación

1. Clonar el repositorio

   ```bash
   git clone https://github.com/josereimondez29/graphql-cloud-skeleton.git
   cd graphql-cloud-skeleton

2. Crear y activar un entorno virtual

  ```bash
  python3 -m venv skeleton
  source skeleton/bin/activate  # Mac/Linux
  skeleton\Scripts\activate     # Windows
  ```

3. Instalar dependencias

  ```bash
   pip install -r requirements.txt
  ```

4. Aplicar migraciones

  ```bash
  python manage.py migrate
  ```

5. Ejecutar servidor de desarrollo

   ```bash
   uvicorn project.asgi:application --reload
   ```

Uso

Acceder a http://127.0.0.1:8000/graphql para interactuar con la API GraphQL.
Definir consultas y mutaciones según el esquema definido en core/schema.py.
Contribuciones

Las contribuciones son bienvenidas. Por favor abre un issue o pull request.

Licencia

MIT License © Jose Reimondez

