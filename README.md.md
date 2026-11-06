# ✨ YAYA | Sistema de Inventario, Cotización y Planificación Creativa

**Autora:** Anjie Torres Yaya  
**Programa:** Especialización en Diseño y Creación con Inteligencia Artificial  
**Asignatura:** Programación en Python — Actividad: *Mi primer programa en Python*  

---

## 📌 1. Descripción del Proyecto y Problema Propuesto

En la dirección creativa y producción artesanal de la marca de joyería tejida **YAYA**, la planificación de colecciones requiere verificar la disponibilidad de insumos especializados (cuentas Miyuki Delica, Miyuki Duracoat e hilos técnicos) y calcular de manera precisa los costos de producción, tiempos de tejido y precios de venta sugeridos.

Este proyecto implementa una aplicación web interactiva desarrollada en **Python** y desplegada con **Streamlit** que automatiza este flujo mediante programación estructurada secuencial y validación lógica.

---

## ⚙️ 2. Arquitectura del Programa (Entrada, Proceso y Salida)

El código fuente (`app.py`) está estructurado siguiendo los pilares fundamentales de la programación en Python:

1. **Entrada de Datos (Input):**
   * Nombre de la pieza o colección a diseñar.
   * Selección de la técnica artesanal (*Peyote*, *Brick* o *Telar*) y del insumo principal en bodega.
   * Cantidad de gramos o metros requeridos por unidad y tamaño del lote a producir.
   * Horas estimadas de diseño/tejido por pieza, tarifa por hora creativa y costo unitario del insumo.

2. **Procesamiento de la Información (Process):**
   * **Cálculo de inventario:** Compara el stock actual en bodega frente al consumo total proyectado del lote.
   * **Cálculo financiero y operativo:** Determina el tiempo total de producción en horas, el costo de materiales, el costo de mano de obra creativa, la inversión total del lote y el precio unitario sugerido aplicando un margen comercial del 35%.

3. **Salida de Resultados (Output):**
   * Estado del inventario en tiempo real (aprobación de stock o alerta de faltante).
   * Tarjetas ejecutivas con las métricas clave (Costo Total del Lote, Precio de Venta Unitario y Tiempo Total de Tejido).
   * Desglose financiero detallado listo para orden de producción.

---

## 🛠️ 3. Tecnologías y Herramientas Utilizadas

* **Lenguaje de programación:** Python 3
* **Interfaz Gráfica Web:** Streamlit
* **Entorno de Desarrollo:** Google Antigravity IDE
* **Control de Versiones y Despliegue:** GitHub & Streamlit Community Cloud

---

## 🚀 4. Estructura del Repositorio

* `app.py`: Código fuente principal de la aplicación en Python con comentarios descriptivos.
* `requirements.txt`: Archivo de dependencias para el despliegue automático en la nube.
* `README.md`: Documentación técnica y descriptiva del proyecto.
