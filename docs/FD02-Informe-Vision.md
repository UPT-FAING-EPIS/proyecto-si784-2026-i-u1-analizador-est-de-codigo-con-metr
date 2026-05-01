<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto: Analizador Estático de Código con Métricas**

Curso: Calidad y Pruebas de Software

Docente: Mag. Patrick Cuadros Quiroga

Integrantes:

**Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)**
**Colque Quispe, Rodrigo Sidney (2023077078)**

**Tacna - Perú**

**2026**

**  
**
</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

| CONTROL DE VERSIONES | | | | | |
| :---: | :--- | :--- | :--- | :--- | :--- |
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| 1.0 | R.A. / C.Q. | P.C. | P.C. | 04/04/2026 | Versión Original |

**Sistema: Analizador Estático de Código con Métricas**

**Documento de Visión**

**Versión *{1.0}***
**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


**ÍNDICE GENERAL**

1. [Introducción](#1-introducción)
2. [Posicionamiento](#2-posicionamiento)
3. [Descripción de los interesados y usuarios](#3-descripción-de-los-interesados-y-usuarios)
4. [Vista General del Producto](#4-vista-general-del-producto)
5. [Características del producto](#5-características-del-producto)
6. [Restricciones](#6-restricciones)
7. [Rangos de calidad](#7-rangos-de-calidad)
8. [Precedencia y Prioridad](#8-precedencia-y-prioridad)
9. [Otros requerimientos del producto](#9-otros-requerimientos-del-producto)
[CONCLUSIONES](#conclusiones)
[RECOMENDACIONES](#recomendaciones)
[BIBLIOGRAFÍA](#bibliografía)
[WEBGRAFÍA](#webgrafía)

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 1. Introducción

**1.1. Propósito**
El propósito de este documento es definir la visión, el alcance y los objetivos del Analizador Estático de Código con Métricas. Este sistema busca implementar un mecanismo de evaluación automatizada para medir la calidad interna del software, calculando métricas de complejidad y detectando malas prácticas sin necesidad de ejecutar el código fuente.

**1.2. Alcance**
El proyecto abarca la creación de una herramienta que procese archivos. Incluye la generación de un Árbol de Sintaxis Abstracta (AST) para capturar métricas de Complejidad Ciclomática, Líneas de Código (LOC) y la identificación de anomalías estructurales.

**1.3. Definiciones, Siglas y Abreviaturas**
* **AST (Abstract Syntax Tree):** Representación jerárquica de la estructura lógica del código fuente generada durante el parsing.
* **Complejidad Ciclomática:** Métrica de software que mide el número de caminos linealmente independientes a través del código fuente.
* **Code Smell:** Síntoma en el código fuente que indica un problema profundo de diseño o calidad que dificulta el mantenimiento.
* **Análisis Estático:** Técnica de depuración que consiste en el examen del código sin ejecutar el programa.
* **Deuda Técnica:** Costo implícito de un desarrollo acelerado que prioriza la rapidez sobre la calidad de código a largo plazo.

**1.4. Referencias**
* Informe de Factibilidad del Analizador Estático de Código con Métricas (FD01).
* Manual de usuario y archivo README del sistema.

**1.5. Visión General**
El sistema se desarrollará en 5 fases de desarrollo iterativo con una duración estimada de 2 meses. Se utilizarán tecnologías de integración continua como GitHub Actions y librerías especializadas en parsing para garantizar el aseguramiento de la calidad sin incurrir en altos costos de infraestructura.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 2. Posicionamiento

**2.1. Oportunidad de negocio**
Existe la necesidad de reducir la deuda técnica y mejorar la mantenibilidad de los sistemas en desarrollo. La implementación de este analizador permite prevenir ineficiencias operativas estimadas en S/ 2,400.00 anuales al automatizar revisiones que anteriormente eran manuales y propensas a errores.

**2.2. Definición del problema**

| | |
| :--- | :--- |
| **El problema de** | La acumulación de deuda técnica y falta de revisiones exhaustivas de código. |
| **Afecta a** | La mantenibilidad del software a largo plazo y la eficiencia de los equipos de desarrollo. |
| **El impacto es** | Auditorías manuales lentas, errores humanos y dificultad para medir objetivamente la complejidad del sistema. |
| **Una solución exitosa sería** | Una herramienta automatizada que genere reportes de calidad basados en métricas precisas y detección de code smells. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 3. Descripción de los interesados y usuarios

**3.1. Resumen de los interesados**
* **Líderes Técnicos:** Interesados en la reducción de deuda técnica y cumplimiento de estándares internacionales (ISO 25010).
* **Equipos de QA:** Se benefician de reportes estructurados que facilitan el aseguramiento de la calidad.
* **Gerencia de Desarrollo:** Interesados en la rentabilidad del proyecto y el ahorro en horas-hombre de revisión.

**3.2. Entorno de usuario**
El sistema se integra en el flujo de Integración Continua (CI/CD) a través de GitHub. La interacción ocurre de forma automatizada durante el proceso de push o pull request, entregando resultados de forma asíncrona sin interrumpir el desarrollo activo.

**3.3. Perfiles de los interesados**
* **Gerencia Institucional:** Interesada en la mitigación de riesgos operativos y en la rentabilidad financiera del sistema (TIR del 75%).
* **Equipo de Desarrollo (Ingenieros):** Responsables de la programación de los algoritmos de métricas y la validación de nomenclaturas.

**3.4. Perfiles de los Usuarios**
* **Perfil de Calidad (QA):** Usuario enfocado en el cumplimiento de métricas como la profundidad de herencia y el conteo de parámetros para asegurar un código limpio.
* **Perfil de Arquitectura:** Usuario que utiliza el analizador para detectar clases "Dios" que violan los principios de diseño modular.

**3.5. Necesidades de los interesados y usuarios**
* **Automatización:** Necesidad de que las pruebas de calidad no requieran intervención manual constante.
* **Analizabilidad:** Capacidad de diagnosticar deficiencias en el código de forma objetiva.
* **Eficiencia:** Garantizar que el procesamiento de grandes volúmenes de archivos no afecte el rendimiento del pipeline de desarrollo.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 4. Vista General del Producto

**4.1. Perspectiva del producto**
El sistema funciona como un motor de análisis autónomo integrado en el ecosistema de GitHub. Procesa el código fuente antes de que llegue a producción para actuar como un filtro de calidad preventiva.

**4.2. Resumen de capacidades**
* Cálculo automático de Complejidad Ciclomática y volumen de código.
* Generación de reportes de calidad.
* Detección de malas prácticas de nomenclatura.

**4.3. Suposiciones y dependencias**
El éxito depende de la correcta configuración de las GitHub Actions y la disponibilidad de las librerías de parsing. Se depende de la estabilidad de la plataforma GitHub y de un suministro eléctrico constante durante el desarrollo.

**4.4. Costos y precios**
* **Inversión Inicial:** S/ 500.00 (energía, internet y hardware existente).
* **Ahorro proyectado:** S/ 200.00 mensuales tras la implementación final en la Fase 5.
* **Indicadores Financieros:** VAN de S/ 1,681.82 y una TIR del 75% anual.

**4.5. Licenciamiento e instalación**
El software se distribuye bajo licencias de código abierto, permitiendo su uso y mejora continua. La instalación consiste en la integración del motor de análisis en el repositorio mediante scripts específicos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 5. Características del producto
* **Modularidad:** Arquitectura dividida en motor de parsing, cálculo de métricas y generador de reportes.
* **Escalabilidad:** Optimización para procesar proyectos monolíticos o con gran cantidad de archivos.
* **Bajo Costo:** Aprovechamiento de infraestructura gratuita de GitHub y herramientas open-source.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 6. Restricciones
* **Hardware:** El procesamiento de AST en proyectos muy extensos puede requerir optimización de memoria en los servidores de CI/CD.
* **Sintaxis Avanzada:** Posible complejidad ante nuevas versiones de lenguajes con sintaxis altamente anidada.
* **Falsos Positivos:** Necesidad de calibrar las reglas para evitar el marcado incorrecto de código válido.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 7. Rangos de calidad
* **Aseguramiento de Calidad:** Pruebas unitarias exhaustivas y reportes de Code Coverage.
* **Eficacia:** El motor de parsing debe representar fielmente la lógica del código fuente para métricas precisas.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 8. Precedencia y Prioridad
(Esta sección se define conforme al cronograma de implementación de las 5 fases iterativas).

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# 9. Otros requerimientos del producto

**9.1. Estándares legales**
* **Licenciamiento Open Source:** Uso de librerías con licencias compatibles (MIT o Apache).
* **Propiedad Intelectual:** Análisis estrictamente sobre código propio o con autorización explícita.
* **Protección de Activos Digitales:** Confidencialidad de la lógica de los algoritmos desarrollados.

**9.2. Estándares de comunicación**
* **Interoperabilidad de Reportes:** Salidas en formatos estandarizados para otros módulos de QA.
* **Estándar CI:** GitHub Actions como canal de comunicación automatizado tras cada commit.
* **Documentación Técnica:** Centralización de manuales en archivos README y formato Markdown.

**9.3. Estándares de cumplimiento de la plataforma**
* Integración nativa con GitHub para manejo de repositorios y automatización.
* Uso de formatos de intercambio de datos estándar para interoperabilidad.

**9.4. Estándares de calidad y seguridad**
* **Mantenibilidad:** Diseño que facilita la evolución para soportar nuevos lenguajes.
* **Seguridad:** Análisis seguro garantizando la privacidad del código fuente analizado.
* **Integridad:** Reportes que reflejan exactamente el estado actual del código sin omisiones.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# CONCLUSIONES
* El proyecto es técnicamente factible y financieramente rentable con un beneficio/costo de 4.8.
* La implementación dota a los equipos de una herramienta esencial para reducir la deuda técnica y asegurar la calidad interna.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# RECOMENDACIONES
* Monitorear constantemente el rendimiento del motor de análisis en proyectos de gran escala.
* Refinar periódicamente las reglas de detección de code smells para reducir falsos positivos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# BIBLIOGRAFÍA
* Ramos Atahuachi, F. F. E., & Colque Quispe, R. S. (2026). *Informe de Factibilidad: Analizador estático de código con métricas (Documento interno FD01)*. Escuela Profesional de Ingeniería de Sistemas, Universidad Privada de Tacna.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# WEBGRAFÍA
* **ISO/IEC 25010 (System and Software Quality Models):** Guía principal para la definición de métricas de calidad. https://iso25000.com/
* **GitHub Actions Documentation:** Estándar utilizado para la automatización de los procesos de análisis. https://docs.github.com/en/actions
