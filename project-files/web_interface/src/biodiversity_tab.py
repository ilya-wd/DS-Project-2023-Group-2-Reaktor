import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from func_import import open_file

sys.dont_write_bytecode = True


def render():
    st.header("Biodiversity in Finland")
    st.subheader("Biodiversity map")
    col1, col2 = st.columns([0.75, 0.25], gap="small")
    year = "2023"
    datatype = "Observations"
    with col2:
        st.subheader("Map controller")
        year = str(col2.slider("Year slider", 2000, 2023, 2023))
        col2.caption(f"Showing data from **2000** to **{year}**")
        stats = pd.read_csv(CURRENT_DIR + "/../precomp_data/statistics.csv")
        observations_stats = stats[stats["Year"] == int(year)]["Observations"].iloc[0]
        species_stats = stats[stats["Year"] == int(year)]["Species"].iloc[0]

        col21, col22 = st.columns([0.5, 0.5], gap="small")
        col21.markdown(
            f"<p style='text-align: center; font-size: 16px;'> Observations so far </p>",
            unsafe_allow_html=True,
        )
        col21.markdown(
            f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {str(observations_stats)} </p>",
            unsafe_allow_html=True,
        )
        col22.markdown(
            f"<p style='text-align: center; font-size: 16px;'> Observed species </p>",
            unsafe_allow_html=True,
        )
        col22.markdown(
            f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {str(species_stats)} </p>",
            unsafe_allow_html=True,
        )

        datatype = col2.selectbox(
            "Type of data",
            ["Simpson index", "Shannon entropy", "Richness", "Observations"],
        )

    with col1:
        if datatype == "Observations":
            col1._html(
                open_file(f"./precomp_data/grid_map/grid_map_2000-{year}.html")[1],
                height=700,
            )
        elif datatype == "Richness":
            col1._html(
                open_file(
                    f"./precomp_data/biodiversity_metrics/actual_dist/grid_richness_{year}.html"
                )[1],
                height=700,
            )
        elif datatype == "Simpson index":
            col1._html(
                open_file(
                    f"./precomp_data/biodiversity_metrics/actual_dist/grid_simpson_{year}.html"
                )[1],
                height=700,
            )
        else:
            col1._html(
                open_file(
                    f"./precomp_data/biodiversity_metrics/actual_dist/grid_shannon_{year}.html"
                )[1],
                height=700,
            )

    st.subheader("Keystone species")
    st.markdown(
        """
        Keystone species play a considerable role in maintaining the balance of the ecosystem. In Finland, there are several of them,
        but we focus on the yellow-breasted buntings in this webpage since this species has gone extinct in Finland, thus the effect
        of their disappearance can be studied. 

        Yellow-breasted buntings breed in Europe and migrate to Asia during winter. There, they are illegally hunted for a special dish
        and their number has decreased dramatically since 2004. Before that, they were listed as the 'Least Concerned', but, in just 10 years,
        their status became 'Critically Endangered'. In Finland, this birds has officially gone extinct, not only due to the extensive hunting
        but also because of the climate and habitat changes. Below, we study how the biodiversity changes according to the disappearance
        of yellow-breasted bunting, therefore giving an example of how keystone species might affect the whole ecosystem.

        We study areas that used to have recorded observations of yellow-breasted bunting. 
        In particular, we collect data of trees and birds in area with yellow-breasted bunting before, during, and after the time spans in which there were observations of yellow-breasted bunting.
        In the time periods before and after such time spans, data are collected in 3-years intervals. The average species richness of such areas during these time periods is calculated:
        """
    )
    components.html(
        open_file(f"./precomp_data/keystone/bird_average_timeseries_bunting.html")[1],
        height=400,
    )
    components.html(
        open_file(f"./precomp_data/keystone/tree_average_timeseries_bunting.html")[1],
        height=400,
    )
    
    st.markdown(
        """
        It is visible that there was an increase in average biodiversity richness from the period before to after recorded observations of yellow-breasted bunting, 
        peaking at the time span of 1 to 3 years after last recorded observations. 
        
        In fact, the most statistically significant difference for both trees and birds data is between the period 1 to 3 years before and 1 to 3 years after recorded observations of yellow-breasted bunting,
        with higher than 95% confidence interval. The specific effect for each area is visualized as:
        """
    )
    components.html(
        open_file(f"./precomp_data/keystone/bird_paired_bunting_effect.html")[1],
        height=400,
    )
    components.html(
        open_file(f"./precomp_data/keystone/tree_paired_bunting_effect.html")[1],
        height=400,
    )
    st.markdown(
        """
        On the other hand, the effect of the species' decline remains unclear for the inspected time period.
        However, such decline can be speculated to negatively affect species richness, as species richness reached a peak in time span of 1 to 3 years after last recorded observations despite the previous increasing trend.
        Noticeably, the species richness of trees even showed a downturn trend after reaching such peak.
        """
    )

    st.subheader("Environmental variables analysis")
    st.markdown(
        """
        In this section, we model biodiversity (species richness) as a function of 19 bioclimatic variables (BIO1 - BIO19) provided by WorldClim [[1]](https://www.worldclim.org/). It's worth noting that the environmental variables are not independent, but rather correlated with each other.

        The grids of these bioclimatic variables have a resolution of 5 minutes.

        ##### Methods

        MaxEnt [[2]](https://www.sciencedirect.com/science/article/abs/pii/S030438000500267X) is a software commonly used for species distribution modeling. The software takes as input the observation locations (presence locations) of a species and a set of environmental grids, which are then used to infer a model whose output can be interpreted as the probability that the species is present in each grid cell.

        For each species, we extracted the observation locations of that species and fed them into MaxEnt together with the 19 bioclimatic grids. A bias file [[3]](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ddi.12096) was also included to account for sampling bias. The result is the probability of presence of a species in each grid cell, to which we applied a threshold of 0.5 to infer the binary labels “present” (p > 0.5) or “not present” (p <= 0.5). We then counted the number of species present in each grid cell and obtained the species richness value. Finally, we calculated the Pearson’s correlation between each bioclimatic variable and species richness to identify the bioclimatic factors that are highly correlated with species richness.

        ##### Results

        **1. Birds results**
        """
    )

    _, left_co, last_co, _ = st.columns([0.1, 0.4, 0.4, 0.1])
    with left_co:
        image = Image.open(
            f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/birds_richness.png"
        )
        st.image(image)

    with last_co:
        image = Image.open(
            f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/birds_corr.png"
        )
        st.image(image)

    st.markdown(
        """
        We can see that birds richness is strongly positively correlated (corr > 0.7) with BIO11 (Mean Temperature of Coldest Quarter), 
        BIO6 (Min Temperature of Coldest Month), BIO9 (Mean Temperature of Driest Quarter), BIO1 (Annual Mean Temperature). Meanwhile, 
        birds richness is strongly negatively correlated (corr < -0.7) with BIO7 (Temperature Annual Range).
        """
    )

    _, left_co, mid_co, last_co, _ = st.columns([0.05, 0.3, 0.3, 0.3, 0.05])
    with left_co:
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio1.png"
            )
        )
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio11.png"
            )
        )
    with mid_co:
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio6.png"
            )
        )
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio7.png"
            )
        )
    with last_co:
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio9.png"
            )
        )

    st.markdown(
        """
        **2. Mammals results**
        """
    )

    _, left_co, last_co, _ = st.columns([0.1, 0.4, 0.4, 0.1])
    with left_co:
        image = Image.open(
            f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/mammals_richness.png"
        )
        st.image(image)

    with last_co:
        image = Image.open(
            f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/mammals_corr.png"
        )
        st.image(image)

    st.markdown(
        """
        We can see that birds richness is strongly positively correlated (corr > 0.7) with BIO11 
        (Mean Temperature of Coldest Quarter), BIO6 (Min Temperature of Coldest Month), BIO9 
        (Mean Temperature of Driest Quarter). Meanwhile, birds richness is strongly negatively correlated 
        (corr < -0.7) with BIO7 (Temperature Annual Range).
        """
    )

    _, left_co, mid_co, last_co, _ = st.columns([0.05, 0.3, 0.3, 0.3, 0.05])
    with left_co:
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio1.png"
            )
        )
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio7.png"
            )
        )
    with mid_co:
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio6.png"
            )
        )
    with last_co:
        st.image(
            Image.open(
                f"{CURRENT_DIR}/../precomp_data/species-distribution/plots/bio9.png"
            )
        )

    st.markdown(
        """
        ##### Conclusion

        - We can observe a clear north-south gradient in the species richness of both mammals and birds
        - Species richness seems to be positively correlated with temperature and negatively correlated with the variation in temperature
        """
    )


if __name__ == "__main__":
    render()
