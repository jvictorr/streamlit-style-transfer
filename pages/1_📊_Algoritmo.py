import streamlit as st
from PIL import Image

st.set_page_config(page_title="Tutorial: Transferência de Estilo de Gatys", layout="wide")

st.title("📚 Tutorial Simples: Transferência de Estilo de Gatys")

st.write(
    """
    A **Transferência de Estilo Neural (Neural Style Transfer)** é uma técnica criada por
    *Gatys, Ecker e Bethge* que combina **o conteúdo de uma imagem** com **o estilo de outra**.
    
    Ela usa redes neurais convolucionais (CNNs), especialmente a VGG19, para extrair padrões
    de conteúdo e estilo e gerar uma imagem nova.
    
    Neste mini tutorial interativo, você verá como o processo funciona de forma visual e simples.
    """
)

st.subheader("1️⃣ Imagem de Conteúdo")
st.write("É a imagem base, cuja estrutura (formato, objetos, posições) queremos manter.")
content_img = Image.open("content.jpg")

col1, col2, col3 = st.columns([2,3,2])
with col2:
    st.image(content_img, caption="Imagem de Conteúdo", width='stretch')

st.subheader("2️⃣ Imagem de Estilo")
st.write("É a imagem que fornece as características de estilo: cores, texturas e padrões usados na composição final.")
style_img = Image.open("style.jpg")
col1, col2, col3 = st.columns([2,3,2])
with col2:
    st.image(style_img, caption="Imagem de Estilo", width='stretch')

st.markdown("---")

st.subheader("🧠 Como a Técnica Funciona")
st.write(
    """
    A rede neural pré-treinada (normalmente a **VGG19**) extrai diferentes tipos de informações:

    - **Camadas profundas** → capturam *conteúdo* (formas principais da imagem)
    - **Camadas rasas** → capturam *estilo* (texturas, padrões e cores)

    O algoritmo cria uma imagem inicial (geralmente ruído ou a própria imagem de conteúdo)
    e tenta ajustá-la até:

    - Manter o **conteúdo** parecido com a imagem de conteúdo
    - Manter o **estilo** parecido com a imagem de estilo
    """
)

col1, col2 = st.columns(2)
with col1:
    st.image("feature_maps_example.png", caption="Exemplo de Mapas de Características da VGG", width='stretch')
with col2:
    st.write(
        """
        A VGG divide a imagem em camadas, cada uma respondendo a elementos diferentes,
        como bordas, formas, cores e texturas.
        """
    )

st.markdown("---")

st.subheader("📉 Funções de Custo")
st.write(
    """
    O processo usa duas funções principais:

    - **Custo de conteúdo**: mede o quanto a imagem gerada se parece com a imagem de conteúdo.
    - **Custo de estilo**: mede o quanto a imagem gerada segue o estilo desejado.

    A imagem final minimiza a soma dessas funções.
    """
)

#st.image("loss_function_diagram.jpg", caption="Esquema da Função de Custo", width='stretch')

st.markdown("---")

st.subheader("🎨 Resultado Final")
st.write("A combinação de conteúdo + estilo gera uma imagem única:")

col1, col2, col3 = st.columns([2,3,2])
with col2:
    st.image("result.jpg", caption="Imagem Gerada Pela Transferência de Estilo", width='stretch')

st.markdown("---")

st.subheader("📌 Conclusão")
st.write(
    """
    A transferência de estilo de Gatys mostra como redes neurais podem compreender e recriar
    padrões visuais complexos. Apesar de simples conceitualmente, o processo envolve cálculos
    intensos e depende da força das CNNs.
    
    Esse método foi base para muitas técnicas modernas de geração de imagens!
    """
)
