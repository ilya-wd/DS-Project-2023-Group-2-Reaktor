import streamlit as st
import sys
sys.dont_write_bytecode = True

import biodiversity_tab
import relationship_tab
import project_tab
import about_tab

st.set_page_config(layout="wide")
st.title("Biology dashboard")

st.markdown(
    """
    <style>
    .st-bn {
        display: flex;
        justify-content: space-around;
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
