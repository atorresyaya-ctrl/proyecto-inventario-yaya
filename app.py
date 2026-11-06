# ==============================================================================
# PROGRAMA: Sistema Integral de Inventario y Cotización - YAYA x ARTURO CALLE
# AUTORA: Anjie Torres Yaya
# ==============================================================================

import streamlit as st

# Configuración estética de la página web con identidad editorial YAYA
st.set_page_config(
    page_title="YAYA | Joyería Artesanal & Dirección Creativa", 
    page_icon="✨", 
    layout="centered"
)

# Estilos visuales: Fondo papel marfil cálido, tipografía sofisticada y acentos tierra / dorados
st.markdown("""
    <style>
    .stApp { 
        background-color: #f7f4ed; 
        color: #2c2a29; 
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2, h3 { 
        color: #1a1918 !important; 
        font-weight: 400;
        letter-spacing: 1.5px;
        border-bottom: 1px solid #d4af37;
        padding-bottom: 8px;
    }
    .stButton>button {
        background-color: #1a1918; 
        color: #f7f4ed; 
        font-weight: bold;
        border-radius: 2px; 
        width: 100%; 
        border: none; 
        padding: 12px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    .stButton>button:hover { 
        background-color: #d4af37; 
        color: #1a1918; 
    }
    .streamlit-expanderHeader {
        color: #1a1918 !important;
        background-color: #eae5d9 !important;
        border-radius: 2px;
        font-weight: bold;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #ffffff;
        color: #2c2a29;
        border: 1px solid #d4af37;
        border-radius: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado institucional con identidad de co-branding
st.title("✨ YAYA | Joyería Artesanal")
st.markdown("**Propuesta de Co-Branding / Edición Cápsula 2026 — Arturo Calle Woman**")
st.write("Sistema automatizado de control de inventario integral (Insumos, Hilos y Herrajes) y cálculo financiero de producción.")

# ==============================================================================
# BASE DE DATOS AMPLIADA: 22+ REFERENCIAS DE INVENTARIO (BODEGA YAYA)
# ==============================================================================
inventario_bodega = {
    "Miyuki Delica Dorado Galvanizado 11/0 (g)": 45.0,
    "Miyuki Duracoat Negro Mate 11/0 (g)": 60.5,
    "Miyuki Delica Turquesa Prehispánico (g)": 28.0,
    "Miyuki Delica Fucsia Vitalidad 11/0 (g)": 35.0,
    "Miyuki Delica Lila Espiritualidad 11/0 (g)": 22.0,
    "Miyuki Delica Bronce Antiguo 11/0 (g)": 50.0,
    "Miyuki Delica Blanco Marfil 11/0 (g)": 40.0,
    "Miyuki Delica Oro Rosa 11/0 (g)": 30.0,
    "Miyuki Delica Plata Brillante 11/0 (g)": 33.0,
    "Miyuki Delica Terracota Andino 11/0 (g)": 25.0,
    "Hilo Aptan Especial para Tejido (m)": 150.0,
    "Hilo Encerado Slam 1.0mm (m)": 90.0,
    "Hilo Nylon Monofilamento Fino (m)": 200.0,
    "Hilo C-Lon Beading Cord (m)": 110.0,
    "Herrajes Tubo Anodizado Silver (unidad)": 24.0,
    "Herrajes Tubo Oro 24k (unidad)": 18.0,
    "Argollas Loop Silver 15mm (par)": 32.0,
    "Bases Topos Triada Gold (par)": 15.0,
    "Broches Mosquetón Acero Inoxidable (unidad)": 40.0,
    "Cadenitas Extensoras Acero/Oro (unidad)": 25.0,
    "Dijes Geométricos Precolombinos (unidad)": 12.0,
    "Pines de Seguridad para Broches (unidad)": 50.0
}

with st.expander("📦 Ver Inventario Completo en Bodega (22+ Referencias)"):
    for insumo, stock in inventario_bodega.items():
        st.markdown(f"• **{insumo}:** `{stock}` en stock")

st.markdown("---")

# ==============================================================================
# ENTRADA DE DATOS
# ==============================================================================
st.subheader("🎨 Parámetros de Producción y Diseño")

nombre_pieza = st.text_input("Nombre de la pieza o referencia cápsula:", "Aretes Colección Tríada Dual")
tecnica_tejido = st.selectbox("Técnica de orfebrería y micro-tejido:", [
    "Tejido Peyote Circular", 
    "Tejido Brick Stitch", 
    "Tejido en Telar Tradicional", 
    "Ensamble y Modulación de Herrajes"
])

material_seleccionado = st.selectbox("Seleccionar insumo / herraje principal:", list(inventario_bodega.keys()))

col1, col2 = st.columns(2)
with col1:
    cantidad_por_pieza = st.number_input("Cantidad requerida por pieza (g / m / und):", min_value=0.1, value=4.5, step=0.5)
    unidades_lote = st.number_input("Tamaño del lote a producir (unidades):", min_value=1, value=10, step=1)

with col2:
    horas_por_pieza = st.number_input("Horas de trabajo artesanal por pieza:", min_value=0.5, value=2.5, step=0.5)
    valor_hora = st.number_input("Tarifa hora de diseño y tejido ($ COP):", min_value=5000.0, value=25000.0, step=1000.0)

costo_insumo_unidad = st.number_input("Costo unitario del insumo ($ COP):", min_value=100.0, value=5200.0, step=200.0)

ejecutar = st.button("PROCESAR CÁPSULA Y VALIDAR INVENTARIO")

# ==============================================================================
# PROCESAMIENTO Y SALIDA
# ==============================================================================
if ejecutar:
    stock_disponible = inventario_bodega[material_seleccionado]
    total_material_necesario = cantidad_por_pieza * unidades_lote
    diferencia_stock = stock_disponible - total_material_necesario
    
    tiempo_total_produccion = horas_por_pieza * unidades_lote
    costo_total_materiales = total_material_necesario * costo_insumo_unidad
    costo_total_mano_obra = tiempo_total_produccion * valor_hora
    costo_total_lote = costo_total_materiales + costo_total_mano_obra
    
    precio_sugerido_unitario = (costo_total_lote / unidades_lote) * 1.40
    venta_total_lote = precio_sugerido_unitario * unidades_lote
    utilidad_neta = venta_total_lote - costo_total_lote

    st.markdown("---")
    st.subheader(f"📋 Reporte Editorial de Producción: {nombre_pieza.upper()}")
    st.write(f"**Técnica:** {tecnica_tejido} | **Volumen de Lote:** {unidades_lote} unidades")
    
    if diferencia_stock >= 0:
        st.success(f"✅ **STOCK SUFICIENTE:** El lote requiere {total_material_necesario:.1f} y cuentas con {stock_disponible}. El remanente en bodega será de {diferencia_stock:.1f}.")
    else:
        faltante = abs(diferencia_stock)
        st.error(f"⚠️ **ALERTA DE ABASTECIMIENTO:** Se requieren {total_material_necesario:.1f} unidades/gramos, pero el stock actual es de {stock_disponible}. Faltan {faltante:.1f} para completar el lote.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Costo Total Lote", f"${costo_total_lote:,.0f} COP")
    m2.metric("Precio Sugerido c/u", f"${precio_sugerido_unitario:,.0f} COP")
    m3.metric("Tiempo de Tejido", f"{tiempo_total_produccion:.1f} Horas")

    st.info(f"""
    **Desglose Financiero para Co-Branding:**
    * **Inversión en insumos y herrajes:** ${costo_total_materiales:,.0f} COP
    * **Inversión en mano de obra artesanal:** ${costo_total_mano_obra:,.0f} COP
    * **Proyección de ingresos en tienda:** ${venta_total_lote:,.0f} COP
    * **Utilidad estimada (Margen de lujo 40%):** ${utilidad_neta:,.0f} COP
    """)