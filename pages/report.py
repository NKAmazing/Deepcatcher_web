import streamlit as st
import requests
from pages.utils.api_requests import get_user_id, get_prediction_history, get_user_reports
from streamlit_option_menu import option_menu
from pages.utils.auth import show_sidebar_auth

# Set the page configuration
st.set_page_config(page_title="Deepcatcher Demo - Home", page_icon=":clipboard:")

# Show the login sidebar
show_sidebar_auth()

def report_view():
    # Verify user authentication
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.warning('Please login to report a prediction.')
        return

    # Get the user ID
    user_id = get_user_id(st.session_state.token)

    # Get the prediction history for the user
    predictions = get_prediction_history(user_id, st.session_state.token)

    # Analize if there are predictions to show
    if not predictions:
        st.info("No predictions found. Please make a prediction first.")
        return

    # Show a select box to choose a prediction
    st.subheader("Select a Prediction to Report")
    prediction_options = {f"{p['predicted_class']} - {p['timestamp'].split('T')[0]} at {p['timestamp'].split('T')[1].split('.')[0]}": p['id'] for p in predictions}
    selected_prediction = st.selectbox("Choose a prediction", options=list(prediction_options.keys()))
    prediction_id = prediction_options[selected_prediction]

    # Show the selected prediction
    prediction = next((p for p in predictions if p['id'] == int(prediction_id)), None)
    if prediction:
        # Definir color y texto según la clase predicha
        if prediction['predicted_class'] == 'Real':
            value_color = 'green'
            value_text = 'REAL'
        else:
            value_color = 'red'
            value_text = 'FAKE'

        # --- Cuadro tipo blur-box para la predicción seleccionada ---
        st.markdown(
            """
            <style>
            .blur-box-report {
                margin: 30px auto 30px auto;
                padding: 28px 24px 24px 24px;
                max-width: 700px;
                width: 98%;
                border-radius: 18px;
                background: rgba(30, 34, 50, 0.45);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1.5px solid rgba(255,255,255,0.18);
                display: flex;
                flex-direction: row;
                align-items: center;
                gap: 28px;
            }
            .blur-report-img {
                flex: 1;
                max-width: 180px;
                min-width: 120px;
                border-radius: 16px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.12);
                background: #fff;
                margin-right: 18px;
            }
            .blur-report-content {
                flex: 2;
                text-align: left;
            }
            .blur-report-title {
                font-size: 1.3rem;
                font-weight: bold;
                color: #fff;
                margin-bottom: 8px;
                font-family: 'Comic Sans MS', 'Comic Sans', cursive;
            }
            .blur-report-pred {
                font-size: 1.1rem;
                font-weight: bold;
                margin-bottom: 6px;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .blur-report-value {
                font-size: 1.1rem;
                font-weight: bold;
            }
            .blur-report-desc {
                font-size: 1.05rem;
                color: #e0e0e0;
                margin-bottom: 8px;
            }
            @media (max-width: 700px) {
                .blur-box-report {
                    flex-direction: column;
                    text-align: center;
                    gap: 12px;
                }
                .blur-report-content {
                    text-align: center;
                }
                .blur-report-img {
                    margin: 0 auto 12px auto;
                }
            }
            </style>
            """, unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class="blur-box-report">
                <img src="{prediction['image']}" class="blur-report-img" width="140"/>
                <div class="blur-report-content">
                    <div class="blur-report-title">Prediction Details</div>
                    <div class="blur-report-pred">
                        <span style="color: #FFD600;">Prediction:&nbsp;</span>
                        <span class="blur-report-value" style="color: {value_color};">{value_text}</span>
                        <span style="color: #fff;">&mdash; {prediction['confidence']:.2f}%</span>
                    </div>
                    <div class="blur-report-desc">
                        Prediction made on {prediction['timestamp'].split('T')[0]} at {prediction['timestamp'].split('T')[1].split('.')[0]}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

    # Report form
    st.subheader("Report Prediction Form")
    title = st.text_input("Title")
    description = st.text_area("Description")

    # If the user submits the report
    if st.button("Submit Report"):
        # Enviar el reporte a la API
        data = {
            "title": title,
            "description": description,
            "prediction": prediction_id,
            "user": user_id
        }
        headers = {'Authorization': f'Token {st.session_state.token}'}
        response = requests.post('http://127.0.0.1:8000/user-service/reports/', headers=headers, data=data)
        if response.status_code == 201:
            st.success("Report successfully submitted.")
        else:
            st.error(f"Error submitting the report: {response.status_code} - {response.json()}")

def reports_history_view():
    # Verificar autenticación
    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.warning('Please login to view report history.')
        return

    # Obtener reportes del usuario
    user_id = get_user_id(st.session_state.token)
    reports = get_user_reports(user_id, st.session_state.token)
    # Obtener predicciones del usuario
    predictions = get_prediction_history(user_id, st.session_state.token)

    if reports:
        st.subheader("Reports History")
        # Agrega el CSS solo una vez
        st.markdown(
            """
            <style>
            .blur-box-report {
                margin: 18px auto 18px auto;
                padding: 18px 18px 18px 18px;
                max-width: 260px;
                width: 98%;
                border-radius: 18px;
                background: rgba(30, 34, 50, 0.45);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1.5px solid rgba(255,255,255,0.18);
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 12px;
            }
            .blur-report-img {
                max-width: 180px;
                min-width: 120px;
                border-radius: 16px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.12);
                background: #fff;
                margin-bottom: 8px;
            }
            </style>
            """, unsafe_allow_html=True
        )
        for report in reports:
            status_color = "yellow" if report['status'] == 'Pending' else "green"
            with st.expander(f"Report: {report['title']} - {report['timestamp'].split('T')[0]} at {report['timestamp'].split('T')[1].split('.')[0]}"):
                # Buscar la predicción correspondiente por ID
                pred_img = None
                if predictions:
                    pred = next((p for p in predictions if p['id'] == report['prediction']), None)
                    if pred and pred.get('image'):
                        pred_img = pred['image']
                if pred_img:
                    # Obtener la clase predicha y el color
                    pred_class = pred.get('predicted_class', '').upper()
                    if pred_class == 'REAL':
                        value_color = 'green'
                    else:
                        value_color = 'red'
                    st.markdown(
                        f"""
                        <div class="blur-box-report">
                            <img src="{pred_img}" class="blur-report-img" width="140"/>
                            <div style="margin-top:6px; font-size:1.05rem; font-weight:bold;">
                                <span style="color: #FFD600;">Predicted Class:&nbsp;</span>
                                <span style="color:{value_color};">{pred_class}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True
                    )
                st.write(f"**Title:** {report['title']}")
                st.write(f"**Description:** {report['description']}")
                st.write(f"**Reported on:** {report['timestamp'].split('T')[0]} at {report['timestamp'].split('T')[1].split('.')[0]}")
                st.markdown(f"**Status:** <span style='color:{status_color}'>**{report['status']}**</span>", unsafe_allow_html=True)
    else:
        st.info("No reports found.")

def main():
    '''
    Main function to display the report page
    '''
    selected_option = option_menu(
        menu_title="Reports and Application Support",
        options=["Report Prediction", "Reports History"],
        icons=["📝", "📄"],
        menu_icon="clipboard",
        default_index=0,
        orientation="horizontal"
    )
    if selected_option == "Report Prediction":
        report_view()
    else:
        reports_history_view()

if __name__ == "__main__":
    main()
