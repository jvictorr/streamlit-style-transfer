import streamlit as st
from PIL import Image
import stylization_script as stylize
import training_script as train
from css import css

css.define_css()
st.set_page_config(page_title="Ferramenta de estilização de imagem", page_icon="🎨")


st.write("## Ferramenta de transferência de estilo")


estilos = {
    "-- Selecione uma opção --": None,
    "Greatwave": {"path":"arts/greatwave.jpg","name":"greatwave.pth"},
    "Starry": {"path":"arts/starry.jpg","name":"starry.pth"},
    "Vassily": {"path":"arts/vassily.jpg","name":"vassily.pth"},
    "Monacat": {"path":"arts/monacat.jpg","name":"monacat.pth"},
    "Candy": {"path":"arts/candy.jpg","name":"candy.pth"},
    "Edtaonisl": {"path":"arts/edtaonisl.jpg","name":"edtaonisl.pth"},
    "Mosaic": {"path":"arts/mosaic.jpg","name":"mosaic.pth"},
    "Importar Estilo":None,
}


with st.sidebar.expander("ℹ️ Image Guidelines"):
    st.write("""
    - Tamanho máximo do arquivo: 10MB
    - Formatos suportados: PNG, JPG, JPEG
    """)


content_valid, style_valid = False, False
col1, col2 = st.columns(2, vertical_alignment="top", border=True)


with col1:
    my_upload = st.file_uploader("Adicione uma imagem de conteúdo", type=["png", "jpg", "jpeg"])
    if my_upload is not None:
        content_image = Image.open(my_upload).convert("RGB")
        st.image(content_image, caption="Conteúdo", width='stretch')
        content_valid = True

with col2:
    style_option = st.selectbox("Escolha o estilo:", list(estilos.keys()))
    if style_option != "-- Selecione uma opção --":
        if style_option == "Importar Estilo":
            my_style = st.file_uploader("Adicione uma imagem de estilo", type=["png", "jpg", "jpeg"])
            if my_style is not None:
                soon = st.button("Em breve...", disabled=True)
                # style_training = Image.open(my_style).convert("RGB")
                # style_training.save('data/style-images/stile.jpg')
                # style_path = train.run('stile.jpg')
        else:
            style_image = estilos[style_option]
            st.image(style_image["path"], caption="Estilo", width='stretch')
            style_valid = True


if content_valid and style_valid:
    output_image = None
    
    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("Estilizar Imagem", use_container_width=True):

            content_image.save('data/content-images/content.jpg')

            output = stylize.run('content.jpg', style_image["name"])
            output_image = output+'\stylized.jpg'

    if output_image is not None:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image(output_image, caption="Imagem estilizada",width='stretch')
        

