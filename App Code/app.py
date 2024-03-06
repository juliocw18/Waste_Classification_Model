# ---------------- Librerías ----------------
import streamlit as st
from streamlit_back_camera_input import back_camera_input
from streamlit_js_eval import streamlit_js_eval
from tensorflow import keras
import numpy as np
from PIL import Image

def main():

# ---------------- General ----------------
    st.set_page_config(page_title='Clasificador de Desechos', page_icon='♻️')

# ---------------- Variables y funciones ----------------
    classifier_model = fr'Modelo_Optimizado.h5'
    banner = fr'TFM_Banner.png'
    class_names = ['orgánico', 'reciclable']
    target_size = (224, 224)
    image_file = None       # Inicio la variable vacía
    model = None

    @st.cache_resource
    def load_model():
        model = keras.models.load_model(classifier_model)
        return model

    # Carga el modelo
    model = load_model()

    def predict_plot(image_photo):
        # Carga de la imagen y preprocesado (resize, vectorizar, agregar batch)
        image_procesed = image_photo.convert('RGB')
        image_procesed = image_procesed.resize(target_size)
        image_procesed = keras.preprocessing.image.img_to_array(image_procesed)
        image_procesed = image_procesed.astype(np.uint8)
        prob = model.predict(np.expand_dims(image_procesed, 0), verbose=0)[0][0]
        pred_class = class_names[(1.0 * (prob >= 0.5)).astype(int)]
        prob = 1-prob if pred_class == class_names[0] else prob
        result = f'desecho clasificado como "{pred_class}" con probabilidad de {prob:.0%}.'
        return result

# ---------------- Banner ----------------
    with st.container():
        title_col_left, title_col_right = st.columns(spec=[1,.4],)
        title_col_left.image(banner)
        title_text = """
        <h1 style='text-align: left;
        padding: 50px 0;
        font-size: 25px'>
        Clasifica imágenes de desechos en <i>orgánico</i> o <i>reciclable</i>
        </h1>
            """
        title_col_right.markdown(title_text, unsafe_allow_html=True)
        st.divider()

# ---------------- Radio buttons ----------------
    label_options = ['Cargar una imagen', 'Cargar una foto']
    label_options_captions = ['ubicada dentro de tu dispositivo', 'tomada con tu cámara']
    
    with st.container():
        radio_col_left, radio_col_center, radio_col_right = st.columns(spec=[1, 3, 1], gap='small')
        selection = radio_col_center.radio('**Selecciona el origen de la imagen:**', options=label_options,
                            captions=label_options_captions, index=None, horizontal=True)
        if selection == label_options[0]:
            st.info('¡Haz click, toca o arrastra hasta aquí la imagen!', icon='🖼️')
            image_file = st.file_uploader(label='', type=['jpeg', 'jpg', 'png'],
                                          accept_multiple_files=False, label_visibility='hidden')
            if image_file != None:
                image_file = Image.open(image_file)
                st.image(image_file, caption=image_file.filename, use_column_width='auto')
        elif selection == label_options[1]:
            # image_camera = st.camera_input(label='', label_visibility='hidden')   # Cámara frontal
            st.info('¡Haz click o toca el visor para tomar la foto!', icon='📷')
            image_file = back_camera_input()  # Cámara trasera
            if image_file != None:
                image_file = Image.open(image_file)
                st.image(image_file, caption=image_file.filename, use_column_width='auto')

# ---------------- Botones clasificar y reiniciar ----------------
    with st.container():
        button_col_left, button_col_center, button_col_right = st.columns(spec=[.8, 1, 1], gap='small')
        button_class = button_col_center.button('Clasificar')
        if button_class == True:
            if image_file != None:    
                    st.success(f'¡Listo!, {predict_plot(image_file)}', icon='✅')
            elif image_file == None:
                st.error('¡Por favor carga una imagen para poder proceder!', icon='❌')
        button_restart = button_col_right.button('Reiniciar')
        if button_restart == True:
            streamlit_js_eval(js_expressions="parent.window.location.reload()")

# ---------------- Pie de Página ----------------
    st.divider()
    st.caption('Versión 1.0, Red Neuronal Convolucional desarrollada por Julio Chen. Universidad Complutense \
            de Madrid, Máster en Big Data y Data Science, curso 2022-2023. Trabajo de Fin de Máster.')
    
if __name__ == '__main__':
    main()