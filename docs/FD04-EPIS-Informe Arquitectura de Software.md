<center>

![./media/logo-upt.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERÍA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto Analizador Estático de Código con Métricas**

Curso: *Calidad y Pruebas de Software*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***

***Colque Quispe, Rodrigo Sídney (2023077078)***

**Tacna – Perú**

***2026***

</center>

---

# Informe de Arquitectura de Software (FD04)

## CONTROL DE VERSIONES
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.0 | RF | PCQ | PCQ | 01/05/2026 | Versión Original |

---

## 1. Introducción

### 1.1. Propósito
El propósito de este documento es describir la arquitectura de software del Analizador Estático de Código. Este documento servirá como guía fundamental para el diseño, implementación y mantenimiento del sistema, asegurando la correcta integración entre la interfaz web de usuario, el motor de análisis de código fuente y la base de datos para el almacenamiento de métricas.

### 1.2. Alcance
El sistema permite a los usuarios:
*   Ingresar fragmentos de código fuente o archivos a través de una interfaz web.
*   Ejecutar un análisis automatizado que incluye fases léxicas, sintácticas y la generación de un Árbol de Sintaxis Abstracta (AST).
*   Visualizar reportes estadísticos y métricas de calidad de código mediante un panel de control interactivo (dashboard.html).
*   Gestionar un historial de análisis vinculados a su cuenta de usuario de forma segura.

### 1.3. Definición, siglas y abreviaturas
*   **AST (Abstract Syntax Tree)**: Árbol de Sintaxis Abstracta, una representación en forma de árbol de la estructura sintáctica del código fuente.
*   **Clean Architecture**: Arquitectura de software que promueve la separación de responsabilidades en capas concéntricas.
*   **Token**: Elemento básico (palabra clave, operador, identificador) identificado durante el análisis léxico.
*   **API REST**: Interfaz de programación de aplicaciones que permite la comunicación entre el frontend y el backend mediante el protocolo HTTP.
*   **Docker**: Plataforma utilizada para aislar y empaquetar el software en contenedores estandarizados.

### 1.4. Visión General
El sistema está construido sobre una arquitectura limpia (Clean Architecture) dividida en cuatro capas principales. El backend procesa el código a través de un motor de análisis independiente (motor_analisis) y expone los resultados mediante enrutadores (routers). El frontend utiliza HTML/JS para renderizar gráficas interactivas sin acoplarse directamente a la lógica de evaluación. Todo el ecosistema es orquestado mediante contenedores para garantizar su portabilidad.

---

## 2. Representación Arquitectónica

### 2.1. Escenarios
*   **Escenario de Usuario (Análisis)**: Un desarrollador autenticado ingresa código en la plataforma. El sistema tokeniza el texto, construye el AST, calcula la complejidad y devuelve un reporte visual.
*   **Escenario de Usuario (Historial)**: El usuario accede a su perfil para revisar métricas de análisis pasados y comparar la evolución de la calidad de sus proyectos.

### 2.2. Vista Lógica
*   **Capa de Presentación**: Contiene los enrutadores (analysis_router, auth_router) y los archivos estáticos (dashboard.html, index.html).
*   **Capa de Negocios**: Actúa como fachada (analysis_coordinator.py) para orquestar la ejecución del análisis y aplicar reglas de seguridad.
*   **Capa Core (Motor)**: Contiene la lógica pura de evaluación (lexical, syntactic, ast) sin dependencias externas.
*   **Capa de Persistencia**: Maneja el mapeo objeto-relacional (models) y el acceso a la base de datos a través de repositorios.

### 2.3. Vista del Proceso
*   **Recepción**: El cliente envía el código al controlador correspondiente.
*   **Evaluación**: El coordinador delega el texto al analizador léxico, luego al sintáctico y finalmente construye el AST.
*   **Cálculo y Persistencia**: Se extraen las métricas, se almacenan en la base de datos usando el repositorio de análisis y se retorna la respuesta.

### 2.4. Vista del desarrollo
*   **Tecnologías**: Desarrollado en Python, estructurado en módulos para garantizar alta cohesión y bajo acoplamiento.
*   **Despliegue**: Se utiliza un archivo docker-compose.yml para levantar tanto el servidor de la aplicación como el servicio de base de datos simultáneamente.

### 2.5. Vista Física
*   **Cliente**: Navegador web moderno desde cualquier sistema operativo.
*   **Servidor Host (Docker)**: Contenedor de la aplicación principal (Backend + Servidor Web embebido).
*   **Servidor de Base de Datos**: Contenedor aislado que almacena los esquemas de usuarios y métricas históricas.

---

## 3. Objetivos y limitaciones arquitectónicas

### 3.1. Disponibilidad
El sistema debe estar disponible para procesar solicitudes de análisis concurrentes. El uso de contenedores permite reiniciar servicios caídos automáticamente.

### 3.2. Seguridad
Aislamiento del código analizado: el motor estático lee el código como texto plano y genera árboles, pero no lo ejecuta, mitigando riesgos de inyección de código malicioso. Las rutas están protegidas mediante autenticación (auth_router).

### 3.3. Adaptabilidad
El motor de análisis está estrictamente separado de la web. Esto permite que en el futuro se puedan añadir nuevas reglas gramaticales o soporte para otros lenguajes sin reescribir la plataforma web.

### 3.4. Rendimiento
El análisis estático (tokenización y AST) debe realizarse en memoria de manera optimizada, garantizando que el reporte se genere en menos de 3 segundos para archivos estándar.

---

## 4. Análisis de Requerimientos

### 4.1. Requerimientos funcionales
| Código | Requerimiento Funcional | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| RF01 | Autenticación de Usuarios | El sistema debe permitir el login y registro mediante credenciales (auth_router). | Alta |
| RF02 | Ingreso de Código | El sistema debe permitir al usuario ingresar código fuente a través de la interfaz web. | Alta |
| RF03 | Análisis Léxico | El sistema debe tokenizar el código identificando palabras clave, operadores y literales. | Alta |
| RF04 | Análisis Sintáctico y AST | El sistema debe validar la estructura gramatical y construir el Árbol de Sintaxis Abstracta. | Alta |
| RF05 | Coordinación de Análisis | El sistema debe orquestar los pasos del análisis y calcular métricas mediante un servicio centralizado. | Alta |
| RF06 | Dashboard de Resultados | El sistema debe mostrar métricas, tokens y posibles errores en una vista de resumen. | Media |
| RF07 | Historial de Análisis | El sistema debe guardar el resultado de los análisis vinculados al usuario. | Media |

### 4.2. Requerimientos no funcionales
| Código | Requerimiento No Funcional | Descripción | Prioridad |
| :--- | :--- | :--- | :--- |
| RNF01 | Rendimiento | El análisis estático de un archivo promedio (<1000 líneas) debe completarse en < 3 segundos. | Alta |
| RNF02 | Despliegue | El sistema debe ser orquestado y desplegado mediante contenedores Docker. | Alta |
| RNF03 | Modularidad | El motor de análisis debe estar estrictamente desacoplado de la base de datos. | Alta |
| RNF04 | Seguridad | Las contraseñas en el user_repository deben almacenarse de forma encriptada. | Alta |

---

## 5. Vistas de Caso de Uso
<img width="519" height="527" alt="image" src="https://github.com/user-attachments/assets/fb8e2ccf-ea01-4b5d-9549-4eb27b91d716" />


---

## 6. Vista Lógica

### 6.1. Diagrama Contextual

<img width="1316" height="350" alt="image" src="https://github.com/user-attachments/assets/a88c0b9e-f35a-45d9-8a2d-f81b17f5fd51" />


---

## 7. Vista de Procesos

### 7.1. Diagrama de Proceso Actual

<img width="507" height="703" alt="image" src="https://github.com/user-attachments/assets/24b2a6b0-f962-495a-be3c-db6bbb54204f" />


### 7.2. Diagrama de Proceso Propuesto

<img width="411" height="778" alt="image" src="https://github.com/user-attachments/assets/efc70809-af71-42c7-bb0c-dfecde67a5a8" />


---

## 8. Vista de Despliegue

### 8.1. Diagrama de Contenedor

<img width="1125" height="622" alt="image" src="https://github.com/user-attachments/assets/8aba62d7-c1ad-4ce4-b612-070eb04b85a0" />


---

## 9. Vista de implementación

### 9.1. Diagrama de Componentes

<img width="1269" height="662" alt="image" src="https://github.com/user-attachments/assets/1767aeb4-7c42-48c9-ac59-dec3fc323ac0" />


---

## 10. Vista de Datos

### 10.1. Diagrama Entidad Relación

<img width="274" height="696" alt="image" src="https://github.com/user-attachments/assets/f5b1b46f-cf3e-4909-aea0-dfc9418336dd" />


---

## 11. Calidad

### 11.1. Escenario de Seguridad
*   **Fuente del estímulo**: Actor externo / Usuario malicioso.
*   **Estímulo**: Intento de inyectar código malicioso en la base de datos o ejecución de código arbitrario en el motor.
*   **Artefacto**: Capa de presentación (routers) y motor de base de datos.
*   **Entorno**: Operación normal de la aplicación expuesta a internet.
*   **Respuesta**: El sistema abstrae consultas mediante la capa de persistencia. El motor lee el código exclusivamente como texto plano para tokenizar sin ejecutarlo.
*   **Medida de respuesta**: 100% de los intentos de inyección son neutralizados.

### 11.2. Escenario de Usabilidad
*   **Fuente del estímulo**: Usuario desarrollador.
*   **Estímulo**: Deseo de interpretar rápidamente los resultados de un análisis complejo.
*   **Artefacto**: Vista dashboard.html.
*   **Entorno**: Navegador web en escritorio o dispositivo móvil.
*   **Respuesta**: La interfaz despliega gráficos interactivos, separando visualmente errores de sintaxis, tokens y complejidad en pestañas claras.
*   **Medida de respuesta**: El usuario identifica zonas problemáticas en menos de 5 segundos tras recibir el reporte.

### 11.3. Escenario de Adaptabilidad
*   **Fuente del estímulo**: Equipo de desarrollo / Requerimientos del negocio.
*   **Estímulo**: Necesidad de desplegar en nuevo entorno de nube o cambiar el motor de base de datos.
*   **Artefacto**: Archivo docker-compose.yml y capa de repositorios.
*   **Entorno**: Entorno de integración y despliegue (CI/CD).
*   **Respuesta**: Configuración de infraestructura empaquetada. Para cambiar de entorno, solo se ajustan variables dentro del archivo Docker.
*   **Medida de respuesta**: El despliegue en un entorno nuevo toma menos de 10 minutos sin modificar código fuente del motor.

### 11.4. Escenario de Disponibilidad
*   **Fuente del estímulo**: Falla del proceso interno o saturación del servidor.
*   **Estímulo**: Caída inesperada del servicio de base de datos o reinicio del contenedor principal.
*   **Artefacto**: Orquestador de contenedores (Docker Daemon).
*   **Entorno**: Producción con múltiples sesiones activas.
*   **Respuesta**: Políticas de reinicio de Docker levantan el servicio automáticamente. Arquitectura stateless asegura que ningún proceso bloquee el sistema.
*   **Medida de respuesta**: El sistema recupera la capacidad de aceptar nuevos análisis en menos de 15 segundos.

### 11.5. Otro Escenario (Escenario de Performance)
*   **Fuente del estímulo**: Analizador de código / Motor interno.
*   **Estímulo**: Recepción de un archivo de código fuente extenso (> 2000 líneas).
*   **Artefacto**: Módulos lexical y syntactic dentro de motor_analisis.
*   **Entorno**: Servidor bajo carga normal de procesamiento.
*   **Respuesta**: El motor procesa la lectura en memoria mediante expresiones regulares y construcciones de grafos eficientes, evitando I/O excesivo en disco.
*   **Medida de respuesta**: El AST se genera y las métricas se devuelven en un tiempo no mayor a 3 segundos para 2000 líneas.

---
