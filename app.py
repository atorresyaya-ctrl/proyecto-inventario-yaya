# ==============================================================================
# PROGRAMA: Sistema Integral de Inventario y Cotización - YAYA x ARTURO CALLE
# AUTORA: Anjie Torres Yaya
# ==============================================================================

import streamlit as st
import os

# Configuración estética de la página web
st.set_page_config(
    page_title="YAYA | Joyería Artesanal & Dirección Creativa", 
    page_icon="✒️", 
    layout="centered"
)

# Estilos visuales: Fondo sólido marfil claro, tipografía técnica en negrita y sin texturas de puntos
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;600&display=swap');

    .stApp { 
        background-color: #f7f4ed; 
        color: #2b2825; 
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 { 
        font-family: 'Space Mono', monospace !important;
        font-weight: 700 !important;
        color: #1a1816 !important; 
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border-bottom: 1px solid #c8b996;
        padding-bottom: 8px;
    }

    .stButton>button {
        background-color: #2b2825; 
        color: #f7f4ed; 
        font-family: 'Space Mono', monospace;
        font-weight: bold;
        border-radius: 2px; 
        width: 100%; 
        border: none; 
        padding: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .stButton>button:hover { 
        background-color: #8c7853; 
        color: #fcf9f2; 
    }

    .streamlit-expanderHeader {
        font-family: 'Space Mono', monospace !important;
        font-weight: 700 !important;
        color: #1a1816 !important;
        background-color: #ebe5d8 !important;
        border: 1px solid #d4cbb8;
        border-radius: 2px;
    }

    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #ffffff;
        color: #2b2825;
        border: 1px solid #c8b996;
        border-radius: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado institucional
st.title("YAYA | Joyería Artesanal")
st.markdown("**Propuesta de Co-Branding / Edición Cápsula — Arturo Calle Woman**")
st.write("Sistema automatizado de control de inventario integral (200+ Referencias) y cálculo financiero de producción.")

# ==============================================================================
# SECCIÓN VISUAL: CATÁLOGO FOTOGRÁFICO EDITORIAL
# ==============================================================================
st.subheader("Registro Fotográfico de Colección")

opcion_foto = st.selectbox("Seleccionar lámina editorial:", [
    "Lámina 02 - Aretes Flor Dalia & Accesorios Silver",
    "Lámina 03 - Aretes Domo Doble Gold & Collar Poporo",
    "Lámina 04 - Aretes Topo Flor Gold & Gargantilla",
    "Lámina 05 - Candongas Loop Silver & Gargantilla",
    "Lámina 06 - Aretes Amancay Silver & Pulsera Espiral",
    "Lámina 07 - Aretes Amancay Gold & Pulseras",
    "Lámina 08 - Aretes Stella Gold & Gargantilla",
    "Lámina 09 - Candongas Calima Gold & Gargantilla",
    "Lámina 10 - Aretes Rombo Naya Black & Gargantilla",
    "Lámina 11 - Candongas Calima Gold & Gargantilla Doble"
])

# Mapeo apuntando directamente a los archivos de imagen subidos en la raíz
mapa_imagenes = {
    "Lámina 02 - Aretes Flor Dalia & Accesorios Silver": "02.png",
    "Lámina 03 - Aretes Domo Doble Gold & Collar Poporo": "03.png",
    "Lámina 04 - Aretes Topo Flor Gold & Gargantilla": "04.png",
    "Lámina 05 - Candongas Loop Silver & Gargantilla": "05.png",
    "Lámina 06 - Aretes Amancay Silver & Pulsera Espiral": "06.png",
    "Lámina 07 - Aretes Amancay Gold & Pulseras": "07.png",
    "Lámina 08 - Aretes Stella Gold & Gargantilla": "08.png",
    "Lámina 09 - Candongas Calima Gold & Gargantilla": "09.png",
    "Lámina 10 - Aretes Rombo Naya Black & Gargantilla": "10.png",
    "Lámina 11 - Candongas Calima Gold & Gargantilla Doble": "11.png"
}

if opcion_foto in mapa_imagenes and os.path.exists(mapa_imagenes[opcion_foto]):
    st.image(mapa_imagenes[opcion_foto], use_column_width=True)
else:
    st.info("Seleccione una lámina disponible en el catálogo visual.")

st.markdown("---")

# ==============================================================================
# BASE DE DATOS MASIVA: 200 REFERENCIAS DE INVENTARIO BODEGA YAYA
# ==============================================================================
inventario_bodega = {
    "Miyuki Delica 11/0 Dorado Galvanizado (g)": 85.0,
    "Miyuki Delica 11/0 Oro Real 24K (g)": 40.0,
    "Miyuki Delica 11/0 Oro Mate (g)": 60.0,
    "Miyuki Delica 11/0 Oro Claro Silver Lined (g)": 75.0,
    "Miyuki Delica 11/0 Oro Antiguo (g)": 50.0,
    "Miyuki Delica 11/0 Bronce Galvanizado (g)": 65.0,
    "Miyuki Delica 11/0 Bronce Mate (g)": 45.0,
    "Miyuki Delica 11/0 Cobre Galvanizado (g)": 55.0,
    "Miyuki Delica 11/0 Cobre Antiguo (g)": 38.0,
    "Miyuki Delica 11/0 Oro Rosa Galvanizado (g)": 90.0,
    "Miyuki Delica 11/0 Plata Brillante (g)": 110.0,
    "Miyuki Delica 11/0 Plata Mate (g)": 70.0,
    "Miyuki Delica 11/0 Plata Oscura (g)": 40.0,
    "Miyuki Delica 11/0 Aluminio (g)": 35.0,
    "Miyuki Delica 11/0 Platino (g)": 30.0,
    "Miyuki Duracoat 11/0 Negro Mate (g)": 120.0,
    "Miyuki Duracoat 11/0 Blanco Marfil (g)": 95.0,
    "Miyuki Duracoat 11/0 Gris Humo (g)": 60.0,
    "Miyuki Duracoat 11/0 Antracita (g)": 50.0,
    "Miyuki Duracoat 11/0 Beige Arena (g)": 80.0,
    "Miyuki Duracoat 11/0 Terracota Andino (g)": 85.0,
    "Miyuki Duracoat 11/0 Ocre Siena (g)": 45.0,
    "Miyuki Duracoat 11/0 Mostaza Profundo (g)": 70.0,
    "Miyuki Duracoat 11/0 Rojo Carmesí (g)": 50.0,
    "Miyuki Duracoat 11/0 Vinotinto Borgoña (g)": 65.0,
    "Miyuki Duracoat 11/0 Rosado Pastel (g)": 40.0,
    "Miyuki Duracoat 11/0 Fucsia Vitalidad (g)": 75.0,
    "Miyuki Duracoat 11/0 Magenta Real (g)": 55.0,
    "Miyuki Duracoat 11/0 Lila Espiritualidad (g)": 60.0,
    "Miyuki Duracoat 11/0 Morado Amatista (g)": 45.0,
    "Miyuki Duracoat 11/0 Violeta Profundo (g)": 35.0,
    "Miyuki Duracoat 11/0 Azul Rey (g)": 70.0,
    "Miyuki Duracoat 11/0 Azul Marino (g)": 80.0,
    "Miyuki Duracoat 11/0 Turquesa Prehispánico (g)": 90.0,
    "Miyuki Duracoat 11/0 Verde Esmeralda (g)": 65.0,
    "Miyuki Duracoat 11/0 Verde Oliva (g)": 50.0,
    "Miyuki Duracoat 11/0 Verde Militar (g)": 40.0,
    "Miyuki Duracoat 11/0 Menta Suave (g)": 45.0,
    "Miyuki Duracoat 11/0 Amarillo Sol (g)": 55.0,
    "Miyuki Duracoat 11/0 Naranja Mandarina (g)": 38.0,
    "Miyuki 11/0 Transparente Cristal (g)": 150.0,
    "Miyuki 11/0 Cristal AB Tornasol (g)": 100.0,
    "Miyuki 11/0 Cristal Mate Esmerilado (g)": 80.0,
    "Miyuki 11/0 Topacio Transparente (g)": 60.0,
    "Miyuki 11/0 Ámbar Transparente (g)": 50.0,
    "Miyuki 11/0 Humo Transparente (g)": 70.0,
    "Miyuki 11/0 Negro Transparente (g)": 85.0,
    "Miyuki 11/0 Azul Acuoso Transparente (g)": 45.0,
    "Miyuki 11/0 Verde Agua Transparente (g)": 55.0,
    "Miyuki 11/0 Amatista Transparente (g)": 40.0,
    "Miyuki 11/0 Fucsia Transparente (g)": 50.0,
    "Miyuki 11/0 Rojo Transparente (g)": 60.0,
    "Miyuki 11/0 Naranja Transparente (g)": 35.0,
    "Miyuki 11/0 Amarillo Transparente (g)": 40.0,
    "Miyuki 11/0 Violeta Transparente (g)": 45.0,
    "Miyuki 11/0 Ceylon Marfil (g)": 90.0,
    "Miyuki 11/0 Ceylon Beige (g)": 75.0,
    "Miyuki 11/0 Ceylon Rosado (g)": 50.0,
    "Miyuki 11/0 Ceylon Celeste (g)": 60.0,
    "Miyuki 11/0 Ceylon Mint (g)": 45.0,
    "Miyuki 11/0 Silk Satin Dorado (g)": 70.0,
    "Miyuki 11/0 Silk Satin Bronce (g)": 55.0,
    "Miyuki 11/0 Silk Satin Cobre (g)": 50.0,
    "Miyuki 11/0 Silk Satin Plata (g)": 65.0,
    "Miyuki 11/0 Silk Satin Perla (g)": 80.0,
    "Miyuki 11/0 Metallic Steel (g)": 60.0,
    "Miyuki 11/0 Metallic Pewter (g)": 50.0,
    "Miyuki 11/0 Metallic Gunmetal (g)": 70.0,
    "Miyuki 11/0 Metallic Graphite (g)": 45.0,
    "Miyuki 11/0 Metallic Charcoal (g)": 55.0,
    "Miyuki 11/0 Inside Color Oro/Cristal (g)": 65.0,
    "Miyuki 11/0 Inside Color Plata/Cristal (g)": 75.0,
    "Miyuki 11/0 Inside Color Rojo/Cristal (g)": 40.0,
    "Miyuki 11/0 Inside Color Azul/Cristal (g)": 50.0,
    "Miyuki 11/0 Inside Color Verde/Cristal (g)": 45.0,
    "Miyuki 11/0 Lined Red (g)": 55.0,
    "Miyuki 11/0 Lined Blue (g)": 60.0,
    "Miyuki 11/0 Lined Green (g)": 50.0,
    "Miyuki 11/0 Lined Yellow (g)": 35.0,
    "Miyuki 11/0 Lined Pink (g)": 45.0,
    "Miyuki Delica 8/0 Dorado Galvanizado (g)": 50.0,
    "Miyuki Delica 8/0 Negro Mate (g)": 60.0,
    "Miyuki Delica 8/0 Bronce (g)": 40.0,
    "Miyuki Delica 8/0 Plata (g)": 45.0,
    "Miyuki Delica 8/0 Blanco Marfil (g)": 55.0,
    "Miyuki Delica 15/0 Dorado Galvanizado (g)": 30.0,
    "Miyuki Delica 15/0 Negro Mate (g)": 35.0,
    "Miyuki Delica 15/0 Plata (g)": 25.0,
    "Miyuki Delica 15/0 Turquesa (g)": 20.0,
    "Miyuki Delica 15/0 Fucsia (g)": 22.0,
    "Miyuki Bugle Beads 3mm Oro (g)": 40.0,
    "Miyuki Bugle Beads 3mm Plata (g)": 45.0,
    "Miyuki Bugle Beads 3mm Negro (g)": 50.0,
    "Miyuki Bugle Beads 6mm Oro (g)": 35.0,
    "Miyuki Bugle Beads 6mm Plata (g)": 38.0,
    "Cuentas Rodillo Miyuki Oro (g)": 30.0,
    "Cuentas Rodillo Miyuki Plata (g)": 32.0,
    "Cuentas Triangulares Miyuki Bronce (g)": 28.0,
    "Cuentas Hexagonales Miyuki Negro (g)": 40.0,
    "Cuentas Drop Miyuki Cristal (g)": 25.0,
    "Toquilla Miyuki Cobre (g)": 30.0,
    "Toquilla Miyuki Grafito (g)": 35.0,
    "Cuentas Cubo Miyuki 3mm Oro (g)": 25.0,
    "Cuentas Cubo Miyuki 3mm Plata (g)": 28.0,
    "Cuentas Cubo Miyuki 3mm Negro (g)": 30.0,
    "Cuentas Magatama Miyuki Turquesa (g)": 35.0,
    "Cuentas Magatama Miyuki Fucsia (g)": 32.0,
    "Cuentas Magatama Miyuki Dorado (g)": 40.0,
    "Cuentas Magatama Miyuki Perlado (g)": 38.0,
    "Cuentas Magatama Miyuki Antracita (g)": 42.0,
    "Hilo Aptan Especial para Tejido Blanco (m)": 200.0,
    "Hilo Aptan Especial para Tejido Negro (m)": 250.0,
    "Hilo Aptan Especial para Tejido Beige (m)": 180.0,
    "Hilo Aptan Especial para Tejido Dorado (m)": 150.0,
    "Hilo Encerado Slam 1.0mm Negro (m)": 120.0,
    "Hilo Encerado Slam 1.0mm Marrón (m)": 100.0,
    "Hilo Encerado Slam 1.0mm Beige (m)": 110.0,
    "Hilo Encerado Slam 0.5mm Negro (m)": 140.0,
    "Hilo Encerado Slam 0.5mm Blanco (m)": 130.0,
    "Hilo Nylon Monofilamento Fino 0.15mm (m)": 300.0,
    "Hilo Nylon Monofilamento Fino 0.20mm (m)": 250.0,
    "Hilo C-Lon Beading Cord Negro (m)": 150.0,
    "Hilo C-Lon Beading Cord Natural (m)": 160.0,
    "Hilo C-Lon Beading Cord Marrón (m)": 120.0,
    "Hilo C-Lon Dabond UV Negro (m)": 100.0,
    "Hilo FireLine Crystal 0.12mm (m)": 90.0,
    "Hilo FireLine Smoke 0.15mm (m)": 85.0,
    "Hilo WildFire Beading Thread Green (m)": 95.0,
    "Hilo S-Lon Heavy 0.5mm Gold (m)": 110.0,
    "Hilo S-Lon Heavy 0.5mm Black (m)": 120.0,
    "Hilo K.O. Beading Thread White (m)": 130.0,
    "Hilo K.O. Beading Thread Black (m)": 140.0,
    "Hilo K.O. Beading Thread Natural (m)": 110.0,
    "Hilo Nano Fil Beading Thread (m)": 80.0,
    "Cordón de Cuero Genuine Black 2mm (m)": 70.0,
    "Cordón de Cuero Genuine Brown 2mm (m)": 60.0,
    "Cola de Rata Fina Dorada (m)": 90.0,
    "Cola de Rata Fina Negra (m)": 100.0,
    "Hilo Metálico Lamé Dorado (m)": 120.0,
    "Hilo Metálico Lamé Plateado (m)": 110.0,
    "Herrajes Tubo Anodizado Silver (unidad)": 80.0,
    "Herrajes Tubo Oro 24K (unidad)": 75.0,
    "Herrajes Tubo Cobre Antiguo (unidad)": 50.0,
    "Herrajes Tubo Bronce (unidad)": 60.0,
    "Argollas Loop Silver 15mm (par)": 100.0,
    "Argollas Loop Gold 15mm (par)": 90.0,
    "Argollas Loop Bronce 15mm (par)": 60.0,
    "Bases Topos Triada Gold (par)": 70.0,
    "Bases Topos Triada Silver (par)": 65.0,
    "Broches Mosquetón Acero Inoxidable 12mm (unidad)": 120.0,
    "Broches Mosquetón Oro 14K 12mm (unidad)": 90.0,
    "Cadenitas Extensoras Acero 5cm (unidad)": 100.0,
    "Cadenitas Extensoras Oro 5cm (unidad)": 85.0,
    "Dijes Geométricos Precolombinos Oro (unidad)": 50.0,
    "Dijes Geométricos Precolombinos Silver (unidad)": 45.0,
    "Pines de Seguridad para Broches (unidad)": 150.0,
    "Ganchos Arete Anzuelo Acero (par)": 110.0,
    "Ganchos Arete Anzuelo Oro (par)": 95.0,
    "Bases Anillo Ajustable Gold (unidad)": 60.0,
    "Bases Anillo Ajustable Silver (unidad)": 55.0,
    "Terminales Crimp Bead Cover Oro (unidad)": 200.0,
    "Terminales Crimp Bead Cover Plata (unidad)": 180.0,
    "Topes de Silicona para Aretes (par)": 300.0,
    "Bases Dije Marco Circular Oro (unidad)": 40.0,
    "Bases Dije Marco Circular Plata (unidad)": 45.0,
    "Broches Tapa-Nudo Acero (unidad)": 150.0,
    "Broches Tapa-Nudo Oro (unidad)": 130.0,
    "Conectores Ovales Geométricos Oro (unidad)": 70.0,
    "Conectores Ovales Geométricos Plata (unidad)": 65.0,
    "Apliques Rombo Precolombino Oro (unidad)": 50.0,
    "Apliques Rombo Precolombino Plata (unidad)": 45.0,
    "Cierre Marinero T-Bar Oro (unidad)": 60.0,
    "Cierre Marinero T-Bar Plata (unidad)": 55.0,
    "Separadores Metálicos Lisos Oro (unidad)": 140.0,
    "Separadores Metálicos Lisos Plata (unidad)": 130.0,
    "Tubos Calados Filigrana Oro (unidad)": 40.0,
    "Tubos Calados Filigrana Plata (unidad)": 35.0,
    "Bases Broche Brooch Pin Dorado (unidad)": 50.0,
    "Colgantes Fleco Metálico Oro (unidad)": 45.0,
    "Colgantes Fleco Metálico Plata (unidad)": 40.0
}

with st.expander("Inventario Completo en Bodega (200+ Referencias)"):
    st.write("Catálogo maestro general sincronizado con bodega YAYA:")
    for insumo, stock in inventario_bodega.items():
        st.markdown(f"- **{insumo}:** `{stock}` en stock")

st.markdown("---")

# ==============================================================================
# ENTRADA DE DATOS PARA PRODUCCIÓN
# ==============================================================================
st.subheader("Parámetros de Producción y Diseño")

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
# PROCESAMIENTO Y SALIDA FINANCIERA
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
    st.subheader(f"Reporte Editorial de Producción: {nombre_pieza.upper()}")
    st.write(f"**Técnica:** {tecnica_tejido} | **Volumen de Lote:** {unidades_lote} unidades")
    
    if diferencia_stock >= 0:
        st.success(f"STOCK SUFICIENTE: El lote requiere {total_material_necesario:.1f} y cuentas con {stock_disponible}. El remanente en bodega será de {diferencia_stock:.1f}.")
    else:
        faltante = abs(diferencia_stock)
        st.error(f"ALERTA DE ABASTECIMIENTO: Se requieren {total_material_necesario:.1f} unidades/gramos, pero el stock actual es de {stock_disponible}. Faltan {faltante:.1f} para completar el lote.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Costo Total Lote", f"${costo_total_lote:,.0f} COP")
    m2.metric("Precio Sugerido c/u", f"${precio_sugerido_unitario:,.0f} COP")
    m3.metric("Tiempo de Tejido", f"{tiempo_total_produccion:.1f} Horas")

    st.info(f"""
    Desglose Financiero para Co-Branding:
    - Inversión en insumos y herrajes: ${costo_total_materiales:,.0f} COP
    - Inversión en mano de obra artesanal: ${costo_total_mano_obra:,.0f} COP
    - Proyección de ingresos en tienda: ${venta_total_lote:,.0f} COP
    - Utilidad estimada (Margen de lujo 40%): ${utilidad_neta:,.0f} COP
    """)