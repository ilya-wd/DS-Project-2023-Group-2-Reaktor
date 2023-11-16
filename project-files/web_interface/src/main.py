import streamlit as st
import sys
from PIL import Image

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import biodiversity_tab
import relationship_tab
import project_tab
import about_tab

st.set_page_config(
    page_title="Biodiversity dashboard",
    page_icon=Image.open(f"{CURRENT_DIR}/../tree.png"),
    layout="wide",
)

st.title("Biodiversity dashboard")

st.markdown(
    """
    <style>
    .st-bn {
        display: flex;
        justify-content: space-around;
    }

    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 20px !important; 
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

tab_biod, tab_rela, tab_proj, tab_ab = st.tabs(
    ["Biodiversity", "Relationships", "Project", "About"]
)

with tab_biod:
    biodiversity_tab.render()

with tab_rela:
    relationship_tab.render()

with tab_proj:
    project_tab.render()

with tab_ab:
    about_tab.render()
