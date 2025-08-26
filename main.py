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
    st.title("🏠 Home - Deepcatcher Demo") 

    # --- Navbar con scroll interno y borde blanco ---
    st.markdown(
        """
        <style>
        .navbar {
            background: rgba(30, 34, 50, 0.45);
            overflow: hidden;
            border-radius: 24px;
            margin-bottom: 20px;
            border: 2px solid rgba(255,255,255,0.18);
            box-shadow: 0 2px 8px rgba(31, 38, 135, 0.18);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
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

    # # Adjust the size of the image and center it
    # st.markdown(
    #     """
    #     <style>
    #     .center {
    #         display: block;
    #         margin-left: auto;
    #         margin-right: auto;
    #         width: 50%;
    #     }
    #     </style>
    #     """, unsafe_allow_html=True
    # )

    # # Create columns to center the image
    # left_co, cent_co, last_co = st.columns(3)

    main_img = get_base64_image("static/Deepcatcher.png")

    st.markdown(
        f"""
        <style>
        .blur-box {{
            margin: 40px auto 40px auto;
            padding: 36px 32px 32px 32px;
            max-width: 1700px;
            width: 95%;
            border-radius: 18px;
            background: rgba(30, 34, 50, 0.45);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1.5px solid rgba(255,255,255,0.18);
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-between;
            gap: 32px;
        }}
        .blur-content {{
            flex: 2;
            text-align: left;
        }}
        .blur-title {{
            font-size: 2.2rem;
            font-weight: bold;
            letter-spacing: 2px;
            margin-bottom: 18px;
            color: #fff;
            font-family: 'Comic Sans MS', 'Comic Sans', cursive;
        }}
        .blur-desc {{
            font-size: 1.1rem;
            color: #e0e0e0;
            margin-bottom: 22px;
        }}
        .blur-btn {{
            display: inline-block;
            margin: 8px 12px 0 0;
            padding: 10px 28px;
            font-size: 1.1rem;
            border-radius: 6px;
            border: 2px solid #222;
            color: #222;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0px 0px 0px 0px #bbb;
            transition: background 0.2s;
            text-decoration: none;
        }}
        .blur-btn.signup {{
            background: #d6f5d6; /* Verde claro */
            color: #222;
            border: 2px solid #d6f5d6; /* Borde igual al fondo */
        }}
        .blur-btn.getstarted {{
            background: #218838; /* Verde oscuro */
            color: #fff;
            border: 2px solid #218838; /* Borde igual al fondo */
        }}
        .blur-btn.signup:hover {{
            background: #b6f7c1;
        }}
        .blur-btn.getstarted:hover {{
            background: #17692b;
        }}
        .blur-img {{
            flex: 1;
            margin-left: 24px;
            max-width: 260px;
            min-width: 180px;
            border-radius: 50%;
            box-shadow: 0 2px 12px rgba(0,0,0,0.12);
            display: block;
            background: #fff;
        }}
        @media (max-width: 900px) {{
            .blur-box {{
                flex-direction: column;
                text-align: center;
                gap: 18px;
            }}
            .blur-content {{
                text-align: center;
            }}
            .blur-img {{
                margin-left: 0;
                margin: 0 auto;
            }}
        }}
        </style>
        <div class="blur-box">
            <div class="blur-content">
                <div class="blur-title">WELCOME TO DEEPCATCHER</div>
                <div class="blur-desc">
                    A new Deepfake detection app solution using a machine learning model designed to classify images as real or fake. 
                    This application leverages advanced deep learning techniques to identify deepfakes with high accuracy.
                </div>
                <a href="#signup" class="blur-btn signup">Sign Up for Free</a>
                <a href="#get-started" class="blur-btn getstarted">Get Started</a>
            </div>
            <img src="{main_img}" class="blur-img" width="220"/>
        </div>
        """, unsafe_allow_html=True
    )

    # # Display the Deepcatcher image centered
    # with cent_co:
    #     st.image("static/Deepcatcher.png", width=500, caption="Deepcatcher - Deepfake Detection App")

    # --- Sección Our Insight estilo masonry ---
    st.markdown(
        """
        <hr style="border-top: 3px solid #bbb;">
        <div id="our-insight"></div>
        <div style="text-align: left;">
            <h3>Our Insight</h3>
            <p style="font-size:16px;">
                Our solution emerges as a necessary and accessible response to the growing threat of deepfakes. To this end, we have developed Deepcatcher, a practical and effective tool designed to reduce the spread of fake content and empower users with accessible means to verify the authenticity of visual content.
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
        <hr style="border-top: 1px solid #bbb;">
        <div id="features"></div>
        <div style="text-align: left;">
            <h3>Features</h3>
            <p>Our platform combines technological power with an accessible and reliable experience. Each feature is designed to deliver optimal performance, adapt to different scenarios, and always maintain a high level of quality.</p>
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
        {"title": "Adaptable Performance", "desc": "Designed to adapt to different workloads and environments, ensuring optimal results regardless of the complexity of the challenge."},
        {"title": "Great user experience", "desc": "Each interaction is designed to be clear, fast, and efficient, ensuring the user can focus on what's important without distractions."},
        {"title": "Innovative functionality", "desc": "We incorporate unique tools that boost productivity and open up new usage possibilities that go beyond the conventional."},
        {"title": "Precision in the AI Model development", "desc": "Our artificial intelligence models prioritize accuracy and reliability, delivering trustworthy predictions for decision-making in a 73% of accuracy."},
        {"title": "Built to last", "desc": "The system architecture is based on principles of scalability and robustness, ensuring its continuity and long-term evolution."},
        {"title": "Comfortable and Intuitive UI", "desc": "A user-friendly and minimalist interface that allows anyone, regardless of their technical level, to take advantage of all the platform's capabilities."},
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

    with st.expander("How do I contact support for an erroneous prediction?"):
        st.write("To create a report and send it to support, go to the page selection in the navigation bar (left sidebar), select the erroneous prediction, and fill out the form.")

    with st.expander("How do I permanently delete an account registered in the app?"):
        st.write("To delete your account, please contact support using the contact form in the reports section.")

    with st.expander("Can Deepcatcher detect any type of deepfake?"):
        st.write("Deepcatcher is trained to detect the most common types of deepfake (face images), but it does not guarantee the detection of all possible cases.")

    with st.expander("Is it safe to upload and store my images on Deepcatcher?"):
        st.write("Yes, Deepcatcher uses security measures to protect your data and images.")

    with st.expander("Do I need technical knowledge to use the app?"):
        st.write("No, the application is designed to be intuitive and easy to use for anyone.")

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
