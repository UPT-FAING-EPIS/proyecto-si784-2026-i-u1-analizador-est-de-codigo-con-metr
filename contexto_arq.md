# Arquitectura del Sistema - Analizador Estático de Código

## 1. Perfiles de Usuario
* **Desarrollador (Auditor Técnico):** Carga código, ejecuta el motor de análisis y visualiza el historial y dashboard.
* **Administrador del Sistema:** Gestiona cuentas de acceso y monitorea la infraestructura.

## 2. Estructura de Paquetes (4 Capas)
* **Capa de Presentación:** Dashboard, Interfaz de Login, Visualización de métricas.
* **Capa de Negocios:** Servicios de Auditoría, Gestión de Usuario y Seguridad (BCrypt).
* **Capa del Motor de Análisis:** Analizador Léxico y Sintáctico, Generador de AST (Python javalang).
* **Capa de Persistencia:** Modelos de Datos (SQLAlchemy), Repositories, Conexión a PostgreSQL.

## 3. Modelo de Datos (Base de Datos)
* **Tabla USUARIO:** id_usuario (PK), nombre_usuario (Unique), password_hash (BCrypt), rol_sistema, estado_activo.
* **Tabla REPORTE_ANALISIS:** id_reporte (PK), id_usuario (FK), nombre_proyecto, fecha_analisis, lineas_codigo_totales (LOC), complejidad_ciclomatica, code_smells_detectados (JSON).

## 4. Tecnologías Elegidas
* **Backend:** Python (FastAPI).
* **Motor:** javalang (para análisis de Java).
* **Database:** PostgreSQL.
* **Frontend:** React o HTML/Bootstrap (JinJa2 templates para simplicidad).