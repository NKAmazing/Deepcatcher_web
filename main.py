import streamlit as st
from st_pages import Page, show_pages
from pages.utils.auth import show_sidebar_auth
import base64

# Set the page configuration
st.set_page_config(page_title="Deepcatcher Demo - Home", page_icon=":globe_with_meridians:", initial_sidebar_state="expanded", layout="wide")

# Set the pages in the sidebar of the app
show_pages(
    [
        Page("main.py", "Home", "🏠"),
        Page("pages/predict.py", "Prediction", "💻"),
        # Page("pages/authenticate.py", "User Authentication", "🔒"),
        Page("pages/report.py", "Report", "📝"),
        Page("pages/information.py", "About", "📄"),
        # Page("pages/login.py", "Login", "❓")
    ]
)

# Show the login sidebar
show_sidebar_auth()

def get_base64_image(path):
    with open(path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpeg;base64,{b64}"

def main():
    st.title("Deepcatcher Demo - Home") 

    # --- Navbar con scroll interno y borde blanco ---
    st.markdown(
        """
        <style>
        .navbar {
            background-color: #222;
            overflow: hidden;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 2px solid #fff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }
        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 12px 24px;
            text-decoration: none;
            font-size: 17px;
            transition: background 0.2s, color 0.2s;
            border-right: 1px solid #444;
        }
        .navbar a:last-child {
            border-right: none;
        }
        .navbar a:hover {
            background-color: #575757;
            color: #fff;
        }
        </style>
        <div class="navbar">
            <a href="#welcome-to-deepcatcher-demo">Home</a>
            <a href="#our-insight">Our Insight</a>
            <a href="#features">Features</a>
            <a href="#get-started">Get Started</a>
            <a href="#faqs">FAQs</a>
        </div>
        """, unsafe_allow_html=True
    )

    # Adjust the size of the image and center it
    st.markdown(
        """
        <style>
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Create columns to center the image
    left_co, cent_co, last_co = st.columns(3)

    # Display the Deepcatcher image centered
    with cent_co:
        st.image("static/Deepcatcher.png", width=500, caption="Deepcatcher - Deepfake Detection App")

    # --- Sección Our Insight estilo masonry ---
    st.markdown(
        """
        <hr style="border-top: 3px solid #bbb;">
        <div id="our-insight"></div>
        <div style="text-align: left;">
            <h3>Our insight</h3>
            <p style="font-size:16px;">
                Nuestra solución surge como una respuesta necesaria y accesible frente a la amenaza creciente de los Deepfakes. Para ello, hemos desarrollado Deepcatcher, una herramienta práctica y efectiva diseñada para reducir la propagación de contenido falso y empoderar a los usuarios con medios accesibles para verificar la autenticidad del contenido visual.
            </p>
        </div>
        <style>
        .insight-masonry {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            grid-auto-rows: 180px;
            gap: 14px;
            margin: 24px 4% 8px 4%;
            padding: 18px 0;
            border: 2px dashed #888;
            border-radius: 12px;
            background: transparent;
        }
        .insight-masonry-card {
            position: relative;
            width: 100%;
            height: 100%;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            background: transparent;
        }
        .insight-masonry-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .insight-check, .insight-cross {
            position: absolute;
            top: 10px;
            right: 10px;
            width: 32px;
            z-index: 2;
        }
        .insight-label {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(30,30,30,0.55);
            color: #fff;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            padding: 4px 0;
            z-index: 2;
            letter-spacing: 1px;
        }
        .insight-caption {
            text-align: center;
            font-size: 15px;
            color: #aaa;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    fake_imgs = [
        get_base64_image("static/fake/1.jpg"),
        get_base64_image("static/fake/2.jpg"),
        get_base64_image("static/fake/3.jpg"),
        get_base64_image("static/fake/4.jpg"),
        get_base64_image("static/fake/5.jpg"),
    ]

    st.markdown(
        f"""
        <div class="insight-masonry">
            <div class="insight-masonry-card" style="grid-row: span 2;">
                <img src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&w=400" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/ok--v1.png" class="insight-check"/>
                <div class="insight-label">Real</div>
            </div>
            <div class="insight-masonry-card">
                <img src="{fake_imgs[0]}" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/cancel--v1.png" class="insight-cross"/>
                <div class="insight-label">Fake</div>
            </div>
            <div class="insight-masonry-card" style="grid-row: span 2;">
                <img src="https://images.pexels.com/photos/1130626/pexels-photo-1130626.jpeg?auto=compress&w=400" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/ok--v1.png" class="insight-check"/>
                <div class="insight-label">Real</div>
            </div>
            <div class="insight-masonry-card">
                <img src="{fake_imgs[1]}" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/cancel--v1.png" class="insight-cross"/>
                <div class="insight-label">Fake</div>
            </div>
            <div class="insight-masonry-card">
                <img src="https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&w=400" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/ok--v1.png" class="insight-check"/>
                <div class="insight-label">Real</div>
            </div>
            <div class="insight-masonry-card" style="grid-row: span 2;">
                <img src="{fake_imgs[2]}" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/cancel--v1.png" class="insight-cross"/>
                <div class="insight-label">Fake</div>
            </div>
            <div class="insight-masonry-card">
                <img src="https://images.pexels.com/photos/774909/pexels-photo-774909.jpeg?auto=compress&w=400" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/ok--v1.png" class="insight-check"/>
                <div class="insight-label">Real</div>
            </div>
            <div class="insight-masonry-card">
                <img src="{fake_imgs[3]}" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/cancel--v1.png" class="insight-cross"/>
                <div class="insight-label">Fake</div>
            </div>
            <div class="insight-masonry-card">
                <img src="https://images.pexels.com/photos/2379005/pexels-photo-2379005.jpeg?auto=compress&w=400" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/ok--v1.png" class="insight-check"/>
                <div class="insight-label">Real</div>
            </div>
            <div class="insight-masonry-card">
                <img src="{fake_imgs[4]}" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/cancel--v1.png" class="insight-cross"/>
                <div class="insight-label">Fake</div>
            </div>
            <div class="insight-masonry-card">
                <img src="https://images.pexels.com/photos/1707828/pexels-photo-1707828.jpeg?auto=compress&w=400" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/ok--v1.png" class="insight-check"/>
                <div class="insight-label">Real</div>
            </div>
            <div class="insight-masonry-card">
                <img src="{fake_imgs[0]}" class="insight-masonry-img"/>
                <img src="https://img.icons8.com/color/48/000000/cancel--v1.png" class="insight-cross"/>
                <div class="insight-label">Fake</div>
            </div>
        </div>
        <div class="insight-caption">Example Images</div>
        """, unsafe_allow_html=True
    )

    # --- Sección Features estilo highlights ---
    st.markdown(
        """
        <hr style="border-top: 3px solid #bbb;">
        <div id="features"></div>
        <div style="text-align: left; margin-right:8%;">
            <h3>Features</h3>
            <p>Descripción breve de las features de la aplicación, resaltadas al estilo de highlights, en un lenguaje no tan técnico.</p>
        </div>
        <style>
        .feature-card {
            background: #fff;
            border: 2px solid #b5c9d6;
            border-radius: 10px;
            padding: 18px 12px 12px 12px;
            margin: 8px;
            min-height: 80px;
            box-shadow: 1px 2px 6px rgba(0,0,0,0.04);
            font-family: 'Comic Sans MS', 'Comic Sans', cursive;
        }
        .feature-title {
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 6px;
            color: #222831;
        }
        .feature-desc {
            font-size: 15px;
            color: #393e46;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Cuadrícula de features (2 filas x 3 columnas)
    features = [
        {"title": "Adaptable Performance", "desc": "Descripcion del Highlight"},
        {"title": "Great user experience", "desc": "Descripcion del Highlight"},
        {"title": "Innovative functionality", "desc": "Descripcion del Highlight"},
        {"title": "Precision in the AI Model development", "desc": "Descripcion del Highlight"},
        {"title": "Built to last", "desc": "Descripcion del Highlight"},
        {"title": "Comfortable and Intuitive UI", "desc": "Descripcion del Highlight"},
    ]

    for i in range(0, len(features), 3):
        cols = st.columns(3)
        for idx, feature in enumerate(features[i:i+3]):
            with cols[idx]:
                st.markdown(
                    f"""
                    <div class="feature-card">
                        <div class="feature-title">{feature['title']}</div>
                        <div class="feature-desc">{feature['desc']}</div>
                    </div>
                    """, unsafe_allow_html=True
                )

    # --- Sección Get Started ---
    st.markdown(
        """
        <div id="get-started"></div>
        <hr style="border-top: 1px solid #bbb;">
        <div style="text-align: left;">
            <h3>Get Started</h3>
            <p>Use the sidebar to navigate through the different sections of the app:</p>
            <ul>
                <li><strong>Prediction:</strong> Upload an image and get a prediction.</li>
                <li><strong>User Authentication:</strong> Log in or sign up to save your prediction history.</li>
                <li><strong>Report:</strong> View and manage reports on the predictions you have made.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

    # --- Sección FAQs ---
    st.markdown('<div id="faqs"></div>'
                '<hr style="border-top: 1px solid #bbb;">'
                , unsafe_allow_html=True)
    st.markdown("### Frequently asked questions (FAQs)")

    with st.expander("¿Cómo contactar a soporte por una predicción errónea?"):
        st.write("Para crear un reporte y enviarlo a soporte debe ir al menú en la barra de navegación, seleccionar la predicción errónea y llenar el formulario.")

    with st.expander("¿Cómo eliminar una cuenta registrada en la aplicación de manera permanente?"):
        st.write("Para eliminar su cuenta, por favor contacte a soporte desde el formulario de contacto en la sección de reportes.")

    with st.expander("¿Puede Deepcatcher detectar cualquier tipo de deepfake?"):
        st.write("Deepcatcher está entrenado para detectar los tipos de deepfake más comunes, pero no garantiza la detección de todos los casos posibles.")

    with st.expander("¿Es seguro cargar y almacenar mis imágenes en Deepcatcher?"):
        st.write("Sí, Deepcatcher utiliza medidas de seguridad para proteger sus datos e imágenes.")

    with st.expander("¿Necesito conocimientos técnicos para poder usar la aplicación?"):
        st.write("No, la aplicación está diseñada para ser intuitiva y fácil de usar para cualquier persona.")

    # --- Pie de página ---
    st.markdown(
        """
        <hr style="border-top: 3px solid #bbb;">
        <div style="text-align: center;">
            <p>We hope you find Deepcatcher useful for your needs. If you have any feedback or questions, feel free to reach out!</p>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
