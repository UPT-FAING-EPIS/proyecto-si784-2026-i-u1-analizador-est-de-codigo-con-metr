<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto *Analizador Estático de Código con Métricas***

Curso: *Calidad y Pruebas de Software*

Docente: *Mag. Patrick Cuadros Quiroga*

Integrantes:

***Ramos Atahuachi, Fabricio Farid Edmilson (2023076798)***
***Colque Quispe, Rodrigo Sídney (2023077078)***

**Tacna – Perú**

***2026***

**  
**
</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

Sistema *Analizador Estático de Código con Métricas*

Informe de Factibilidad

Versión *{1.0}*

| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :-: | :- | :- | :- | :- | :- |
| 1.0 | F.R. / R.C. | | | 27/03/2026 | Versión Original |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **INDICE GENERAL**

[1. Descripción del Proyecto](#_Toc52661346)

[2. Riesgos](#_Toc52661347)

[3. Análisis de la Situación actual](#_Toc52661348)

[4. Estudio de Factibilidad](#_Toc52661349)

[4.1 Factibilidad Técnica](#_Toc52661350)

[4.2 Factibilidad económica](#_Toc52661351)

[4.3 Factibilidad Operativa](#_Toc52661352)

[4.4 Factibilidad Legal](#_Toc52661353)

[4.5 Factibilidad Social](#_Toc52661354)

[4.6 Factibilidad Ambiental](#_Toc52661355)

[5. Análisis Financiero](#_Toc52661356)

[6. Conclusiones](#_Toc52661357)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Factibilidad</u>**

1. <span id="_Toc52661346" class="anchor"></span>**Descripción del Proyecto**

    1.1. Nombre del proyecto
         Analizador Estático de Código con Métricas

    1.2. Duración del proyecto
         Estimada en 5 fases de desarrollo iterativo, específicamente 2 meses de duración.

    1.3. Descripción
         El proyecto consiste en la creación de una herramienta automatizada que procese y analice el código fuente de aplicaciones (principalmente en entornos C# y Java) sin necesidad de ejecutarlas. A través de la generación de un Árbol de Sintaxis Abstracta (AST), el sistema evaluará métricas de calidad, detectará code smells y verificará el cumplimiento de estándares de programación, exportando los resultados en reportes estructurados.

    1.4. Objetivos

        1.4.1 Objetivo general
              Desarrollar un analizador estático capaz de calcular métricas de complejidad y detectar malas prácticas en el código fuente, garantizando el aseguramiento de la calidad del software.
        1.4.2 Objetivos Específicos
              - Definir lenguajes objetivo y configurar el pipeline inicial de Integración Continua mediante GitHub Actions.
              - Implementar un motor de análisis y parsing que genere el AST a partir de la lectura de archivos fuente.
              - Desarrollar algoritmos de cálculo de métricas clave como Líneas de Código (LOC), Complejidad Ciclomática, Profundidad de Herencia y conteo de parámetros.
              - Crear reglas para la detección de código muerto, clases "Dios" y validación de nomenclaturas (PascalCase, camelCase), exportando reportes en formatos JSON o HTML.
              - Ejecutar pruebas unitarias exhaustivas y de rendimiento, integrando reportes de Code Coverage junto con la redacción del manual de usuario y README.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

2. <span id="_Toc52661347" class="anchor"></span>**Riesgos**

    - **Complejidad del Parsing:** La generación precisa del Árbol de Sintaxis Abstracta (AST) puede ser altamente compleja ante estructuras de código muy anidadas o sintaxis avanzadas de C# y Java.
    - **Falsos positivos:** Las reglas de detección podrían marcar como "código muerto" o code smells fragmentos de código que, por la arquitectura del sistema analizado, sí son necesarios.
    - **Degradación de rendimiento:** El procesamiento de proyectos monolíticos o repositorios con miles de archivos podría consumir excesiva memoria y tiempo si el recorrido de directorios no está optimizado.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

3. <span id="_Toc52661348" class="anchor"></span>**Análisis de la Situación actual**

    3.1. Planteamiento del problema
         En la actualidad, los equipos de desarrollo acumulan deuda técnica y vulnerabilidades debido a la falta de revisiones exhaustivas y estandarizadas. Las auditorías de código manuales consumen demasiado tiempo, son propensas a errores humanos y no logran medir objetivamente la complejidad ciclomática ni la profundidad de anidamiento, lo que dificulta el mantenimiento a largo plazo.

    3.2. Consideraciones de hardware y software
         La solución se desarrollará utilizando herramientas y librerías compatibles con lenguajes fuertemente tipados. Requiere repositorios en GitHub para las Actions de CI/CD, librerías open-source para el análisis léxico/sintáctico, y equipos con recursos estándar para ejecutar pruebas de estrés procesando proyectos de gran tamaño (Mock Data).

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

4. <span id="_Toc52661349" class="anchor"></span>**Estudio de Factibilidad**

    4.1. <span id="_Toc52661350" class="anchor"></span>Factibilidad Técnica
         El proyecto es completamente viable a nivel técnico. Se puede aprovechar el ecosistema de herramientas de integración continua (GitHub Actions) y librerías existentes para el manejo de AST. La lógica recae en la creación de los algoritmos matemáticos y estructurales para las métricas, lo cual es alcanzable con las tecnologías propuestas.

    4.2. <span id="_Toc52661351" class="anchor"></span>Factibilidad Económica

        4.2.1. Costos Generales
               Equipos de cómputo para programación e insumos de escritorio.

        4.2.2. Costos operativos durante el desarrollo
               Gastos de energía eléctrica y servicios de internet durante el desarrollo.

        4.2.3. Costos del ambiente
               Servicios de alojamiento de repositorios (GitHub es gratuito para estos alcances) y uso de herramientas de Code Coverage de acceso libre.

        4.2.4. Costos de personal
               Valoración de las horas-hombre dedicadas al diseño del linter, desarrollo de algoritmos de métricas y redacción de pruebas unitarias exhaustivas.

        4.2.5. Costos totales del desarrollo del sistema
               Estimación final basada en el cronograma de ejecución de los 20 issues definidos.

    4.3. <span id="_Toc52661352" class="anchor"></span>Factibilidad Operativa
         La exportación de resultados en formatos estandarizados (JSON/HTML) garantiza que los desarrolladores y equipos de QA puedan integrar los reportes de auditoría en sus flujos de trabajo diarios sin fricciones.

    4.4. <span id="_Toc52661353" class="anchor"></span>Factibilidad Legal
         No existen impedimentos legales. Se utilizarán librerías bajo licencias de código abierto compatibles y el análisis se realizará estrictamente sobre código fuente autorizado o de propiedad del equipo.

    4.5. <span id="_Toc52661354" class="anchor"></span>Factibilidad Social
         Mejora la cultura de ingeniería de software, promoviendo la adopción de buenas prácticas, la escritura de código limpio y el respeto por las convenciones de nomenclatura en el equipo.

    4.6. <span id="_Toc52661355" class="anchor"></span>Factibilidad Ambiental
         El proyecto no tiene impacto negativo sobre el medio ambiente, al ser un desarrollo enteramente digital.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

5. <span id="_Toc52661356" class="anchor"></span>**Análisis Financiero**

    Este se enfoca en la valoración de la eficiencia ganada y la reducción de la deuda técnica frente a los costos operativos mínimos del desarrollo. Su objetivo es demostrar la viabilidad del proyecto como una inversión en el aseguramiento de la calidad del software.

    5.1. Justificación de la Inversión

        5.1.1. Beneficios del Proyecto

            Beneficios tangibles:
            - Reducción de costos de revisión: Ahorro significativo en horas-hombre al automatizar el cálculo de complejidad ciclomática y detección de code smells, tareas que manualmente consumirían el 20% del tiempo de un desarrollador senior.
            - Detección temprana de fallos: Reducción de costos de mantenimiento futuro al identificar problemas estructurales antes de que el código llegue a producción.
            - Disponibilidad de recursos técnicos: Al automatizar el análisis, el personal de QA puede enfocarse en pruebas de integración y seguridad de mayor valor.

            Beneficios intangibles:
            - Mejora en la mantenibilidad: El software resultante es más fácil de entender y modificar, reduciendo la frustración del equipo de desarrollo.
            - Cultura de Código Limpio: Fomenta la adopción de estándares internacionales de programación (como los de la ISO 25010) en todo el equipo.
            - Reducción de Deuda Técnica: Evita la acumulación de código difícil de mantener, lo que mejora la salud a largo plazo del repositorio.

        5.1.2. Criterios de Inversión

            5.1.2.1. Relación Beneficio/Costo (B/C)
                     Costos (C): Se estima una inversión de S/ 500.00 que cubre energía eléctrica, conectividad a internet y recursos de hardware ya disponibles durante los 2 meses de ejecución.
                     Beneficios (B): El ahorro anual estimado por la detección automática de malas prácticas y la mejora en la velocidad de revisión asciende a S/ 2,400.00 (calculado sobre el valor del tiempo ahorrado a un equipo de desarrollo estándar).
                     B/C = 2400 / 500 = 4.8
                     Evaluación: Al ser mayor a 1, se acepta el proyecto.

            5.1.2.2. Valor Actual Neto (VAN)
                     Este indicador mide el valor actual de los ahorros netos que el analizador generará en su primer año de uso continuo.
                     - Inversión Inicial: S/ 500.00.
                     - Ahorro Mensual Proyectado: S/ 200.00 tras la implementación de la Fase 5.
                     - Tasa de Descuento (COK): 10% anual.
                     Tras el cálculo, el VAN es de S/ 1,681.82.
                     Criterio de aceptación: Al ser mayor a cero, se confirma que el proyecto es financieramente rentable y aporta un valor positivo a la organización desde el primer mes de despliegue.

            5.1.2.3. Tasa Interna de Retorno (TIR)
                     Representa la rentabilidad anual de los recursos destinados al desarrollo de los algoritmos de parsing y cálculo de métricas.
                     - TIR Estimada: 75%
                     - Costo de Oportunidad (COK): 10%
                     Evaluación: Con una TIR del 75%, que supera ampliamente el costo de oportunidad del capital (10%), se acepta el proyecto. Esto indica que invertir tiempo y recursos en este analizador estático propio es significativamente más beneficioso que cualquier otra alternativa financiera tradicional para la institución.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

6. <span id="_Toc52661357" class="anchor"></span>**Conclusiones**

    El proyecto del Analizador Estático de Código con Métricas demuestra ser altamente factible y pertinente. La estructuración en 5 fases permite un desarrollo escalonado, desde el motor de parsing hasta la detección avanzada de code smells. Su implementación dotará a los equipos de desarrollo de una herramienta automática esencial para el aseguramiento de la calidad, reduciendo la deuda técnica y mejorando la mantenibilidad del software sin requerir inversiones cuantiosas en infraestructura.
