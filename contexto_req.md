# Especificación de Requerimientos - Analizador Estático de Código

## 1. Objetivo del Sistema
Desarrollar una plataforma web integral que actúe como filtro preventivo para asegurar la mantenibilidad y reducir la deuda técnica en equipos de desarrollo.

## 2. Requerimientos Funcionales (RF)
* **RF01 Gestión de Sesión:** Registro e inicio de sesión mediante credenciales encriptadas.
* **RF02 Motor de Análisis:** El backend debe procesar archivos fuente para generar el Árbol de Sintaxis Abstracta (AST) y calcular métricas como Complejidad Ciclomática y LOC.
* **RF03 Persistencia Histórica:** Cada análisis debe guardarse en la BD con fecha, usuario, proyecto y resultados detallados.
* **RF04 Dashboard de Calidad:** La web debe mostrar gráficos comparativos de la evolución de la calidad del código.
* **RF05 Exportación de Reportes:** Capacidad de generar documentos en PDF o Excel con el resumen de la auditoría técnica.

## 3. Requerimientos No Funcionales (RNF)
* **RNF01 Disponibilidad:** Aplicación desplegada en la nube (Render/Railway) accesible 24/7.
* **RNF02 Seguridad:** Contraseñas protegidas mediante algoritmos de hashing (BCrypt).
* **RNF03 Rendimiento:** El análisis de un proyecto estándar no debe exceder los 30 segundos.

## 4. Reglas de Negocio (RN)
* **RN01 Inmutabilidad:** Los registros de auditoría almacenados son de solo lectura; no se pueden editar ni eliminar.
* **RN02 Exclusividad de Formato:** Solo se procesan archivos .java o .cs.
* **RN03 Procesamiento Asíncrono:** El análisis no debe bloquear la interfaz web.
* **RN04 Integridad:** Cada registro debe capturar obligatoriamente el usuario, fecha/hora, LOC y Complejidad.