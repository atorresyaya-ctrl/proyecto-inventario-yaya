# ==============================================================================
# PROGRAMA: Sistema Integral de Inventario y Cotización - YAYA x ARTURO CALLE
# AUTORA: Anjie Torres Yaya
# ==============================================================================

import streamlit as st

# Configuración estética de la página web
st.set_page_config(
    page_title="YAYA | Joyería Artesanal & Dirección Creativa", 
    page_icon="✒️", 
    layout="centered"
)

# Estilos visuales: Fondo papel marfil con textura sutil, tipografía de máquina de escribir y estética editorial
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Inter:wght@300;400;500&display=swap');

    .stApp { 
        background-color: #fcf9f2; 
        background-image: radial-gradient(#e3decb 0.75px, transparent 0.75px), radial-gradient(#e3decb 0.75px, #fcf9f2 0.75px);
        background-size: 30px 30px;
        background-position: 0 0, 15px 15px;
        color: #2b2825; 
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 { 
        font-family: 'Special Elite', monospace !important;
        color: #1a1816 !important; 
        font-weight: 400;
        letter-spacing: 1px;
        border-bottom: 1px solid #c8b996;
        padding-bottom: 6px;
    }

    .stButton>button {
        background-color: #2b2825; 
        color: #fcf9f2; 
        font-family: 'Special Elite', monospace;
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
        font-family: 'Special Elite', monospace !important;
        color: #1a1816 !important;
        background-color: #f0ebe1 !important;
        border: 1px solid #d4cbb8;
        border-radius: 2px;
        font-weight: bold;
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
# BASE DE DATOS MASIVA: 200 REFERENCIAS DE INVENTARIO BODEGA YAYA
# ==============================================================================
inventario_bodega = {
    # Cuentas Miyuki Delica 11/0 (Gramos) - Tonos Dorados y Metálicos (001 - 025)
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
    
    # Cuentas Miyuki Duracoat y Opacas (026 - 060)
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

    # Cuentas Miyuki Transparentes y Lustradas (061 - 100)
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
    "Miyuki 1