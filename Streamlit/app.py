import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from scipy import stats
from PIL import Image


st.set_page_config(page_title="#panamsterdam", page_icon=":bike:", layout="wide")

#image = Image.open(r'C:\Users\Administrateur\Documents\GitHub\Final_Project\Streamlit\Panamsterdam.png')
#st.image(image, use_column_width=True, width=500)
st.markdown(
"<h1 style='text-align: center'>"
"<strong>The bike revolution in Paris (2018-2024):</strong>"
"<br><span style='font-size: smaller'>en route to #panamsterdam</span>"
"</h1>", unsafe_allow_html=True)


############### SIDEBAR ######################################################
st.sidebar.subheader("The bike revolution in Paris")
page1 = "Executive summary"
page2 = "Infrastructure overview"
page3 = "Traffic overview"
page4 = "Accident overview"
page5 = "Correlation between traffic & accidents"
page6 = "Users' perception"
page7 = "Is Paris municipality giving itself the means to achieve its ambitions?"

pages = [page1, page2, page3, page4, page5, page6, page7]
select_page = st.sidebar.radio("", pages)



#<iframe src="https://public.tableau.com/authoring/Bikeaccidentmap/Bikeaccidentsmap"
 #width="645" height="955"></iframe>


import streamlit.components.v1 as components
def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1650300467898' style='position: relative'><noscript><a href='#'><img alt='Bike accidents map - 2020 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Panamsterdam_accidents2017_2020&#47;Bikeaccidentsmap&#47;1_rss.png' style='border: none' /></a></noscript><object allowfullscreen="true" class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
    <param name='embed_code_version' value='3' /> 
    <param name='site_root' value='' />
    <param name='name' value='Panamsterdam_accidents2017_2020&#47;Bikeaccidentsmap' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Panamsterdam_accidents2017_2020&#47;Bikeaccidentsmap&#47;1.png' /> 
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='fr-FR' />
    <param name='filter' value='publish=yes' /></object></div>                
    <script type='text/javascript'>                    
    var divElement = document.getElementById('viz1650300467898');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1000, height=500)
if __name__ == "__main__":    
    main()


    
st.write("coucou")
st.write("changement à voir")


def main():
    html_temp = """<div class='tableauPlaceholder' id='viz1650302350918' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Panamsterdam_accidents2017_2020&#47;Bikeaccidentstrend&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Panamsterdam_accidents2017_2020&#47;Bikeaccidentstrend' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pa&#47;Panamsterdam_accidents2017_2020&#47;Bikeaccidentstrend&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='fr-FR' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650302350918');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp, width=1000, height=500)
if __name__ == "__main__":    
    main()