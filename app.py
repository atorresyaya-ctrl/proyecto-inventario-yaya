# ==============================================================================
# PROGRAMA: Sistema de Inventario y Cotización - YAYA Joyería Artesanal
# AUTORA: Anjie Torres Yaya
# DESCRIPCIÓN: Programa estructurado con Entrada, Proceso y Salida en interfaz web
# ==============================================================================

import streamlit as st

# Configuración estética de la página web
st.set_page_config(page_title="YAYA | Gestión y Diseño", page_icon="✨", layout="centered")

# Estilos visuales (Identidad YAYA: Fondo oscuro y acentos dorados)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #f0f6fc; }
    h1, h2, h3 { color: #d4af37 !important; }
    .stButton>button {
        background-color: #d4af37; color: #0d1117; font-weight: bold;
        border-radius: 6px; width: 100%; border: none; padding: 10px;
    }
    .stButton>button:hover { background-color: #f3e5ab; color: #0d1117; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ YAYA | Joyería Artesanal y Dirección Creativa")
st.write("Sistema automatizado de consulta de inventario en bodega y cálculo de producción.")

# Base de datos del inventario actual en gramos / metros
inventario_bodega = {
    "Miyuki Delica Dorado Galvanizado 11/0 (gramos)": 45.0,
    "Miyuki Duracoat Negro Mate 11/0 (gramos)": 60.5,
    "Miyuki Delica Turquesa Prehispánico (gramos)": 25.0,
    "Hilo Aptan Especial para Tejido (metros)": 120.0,
    "Hilo Encerado Slam 1.0mm (metros)": 85.0
}

# Mostrar tabla de inventario actual en la interfaz
st.subheader("📦 1. Estado Actual del Inventario YAYA")
for insumo, stock in inventario_bodega.items():
    st.write(f"• **{insumo}:** `{stock}` disponibles")

st.markdown("---")

# ==============================================================================
# 1. ENTRADA DE DATOS (Captura de variables en la interfaz)
# ==============================================================================
st.subheader("🎨 2. Parámetros de Entrada para Producción")

nombre_pieza = st.text_input("Nombre de la pieza o colección a producir:", "Aretes Tejidos Sol")
tecnica_tejido = st.selectbox("Selecciona la técnica artesanal:", ["Tejido Peyote", "Tejido Brick", "Tejido en Telar"])
material_seleccionado = st.selectbox("Selecciona el insumo principal a verificar:", list(inventario_bodega.keys()))

col1, col2 = st.columns(2)
with col1:
    cantidad_por_pieza = st.number_input("Gramos o metros requeridos por pieza:", min_value=0.5, value=4.5, step=0.5)
    unidades_lote = st.number_input("Cantidad de piezas a tejer en el lote:", min_value=1, value=6, step=1)

with col2:
    horas_por_pieza = st.number_input("Horas de diseño y tejido por pieza:", min_value=0.5, value=3.0, step=0.5)
    valor_hora = st.number_input("Valor por hora de trabajo creativo ($ COP):", min_value=5000.0, value=25000.0, step=1000.0)

costo_insumo_unidad = st.number_input("Costo por gramo/metro del insumo ($ COP):", min_value=500.0, value=4800.0, step=200.0)

# Botón de ejecución
ejecutar = st.button("PROCESAR INVENTARIO Y PRESUPUESTO")

# ==============================================================================
# 2. PROCESAMIENTO DE LA INFORMACIÓN (Cálculos aritméticos secuenciales)
# ==============================================================================
if ejecutar:
    stock_disponible = inventario_bodega[material_seleccionado]
    total_material_necesario = cantidad_por_pieza * unidades_lote
    diferencia_stock = stock_disponible - total_material_necesario
    
    tiempo_total_produccion = horas_por_pieza * unidades_lote
    costo_total_materiales = total_material_necesario * costo_insumo_unidad
    costo_total_mano_obra = tiempo_total_produccion * valor_hora
    costo_total_lote = costo_total_materiales + costo_total_mano_obra
    
    # Margen de ganancia comercial del 35%
    precio_sugerido_unitario = (costo_total_lote / unidades_lote) * 1.35
    venta_total_lote = precio_sugerido_unitario * unidades_lote
    utilidad_neta = venta_total_lote - costo_total_lote

    # ==============================================================================
    # 3. SALIDA DE RESULTADOS (Impresión de reporte en pantalla)
    # ==============================================================================
    st.markdown("---")
    st.subheader(f"📋 3. Reporte de Salida: {nombre_pieza.upper()}")
    st.write(f"**Técnica aplicada:** {tecnica_tejido} | **Lote:** {unidades_lote} unidades")
    
    # Validación condicional de stock
    if diferencia_stock >= 0:
        st.success(f"✅ **STOCK SUFICIENTE:** Necesitas {total_material_necesario} de {material_seleccionado} y tienes {stock_disponible}. Quedarán {diferencia_stock:.1f} en bodega.")
    else:
        faltante = abs(diferencia_stock)
        st.error(f"⚠️ **ALERTA DE STOCK:** Necesitas {total_material_necesario} de {material_seleccionado}, pero solo hay {stock_disponible}. Te faltan {faltante:.1f} para completar el lote.")

    # Métricas financieras y de tiempo
    m1, m2, m3 = st.columns(3)
    m1.metric("Costo Total Lote", f"${costo_total_lote:,.0f} COP")
    m2.metric("Precio Venta c/u", f"${precio_sugerido_unitario:,.0f} COP")
    m3.metric("Tiempo Total", f"{tiempo_total_produccion:.1f} Horas")

    st.info(f"""
    **Desglose Financiero de Dirección Creativa:**
    * **Costo de insumos del lote:** ${costo_total_materiales:,.0f} COP
    * **Costo de mano de obra creativa:** ${costo_total_mano_obra:,.0f} COP
    * **Ingreso total proyectado en ventas:** ${venta_total_lote:,.0f} COP
    * **Utilidad neta estimada para YAYA (35%):** ${utilidad_neta:,.0f} COP
    """)
