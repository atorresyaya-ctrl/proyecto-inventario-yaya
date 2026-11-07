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

# =================