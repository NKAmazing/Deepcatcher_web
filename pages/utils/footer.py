import streamlit as st
import base64
from pathlib import Path

def footer():
    # --- Pie de página tipo sketch/doodle ---
    # Footer logo base64
    logo_path = Path("static/Deepcatcher.png")
    logo_base64 = ""
    if logo_path.exists():
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <hr style="border-top: 3px solid #bbb; margin-top: 40px;">
        <div style="
            font-family: 'Comic Sans MS', 'Comic Sans', 'Handwritten', cursive;
            max-width: 1400px;
            margin: 32px 0 0 0;
            padding: 0 32px 16px 32px;
        ">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <img src='data:image/png;base64,{logo_base64}' alt='Deepcatcher Logo' width='56' height='56' style='border-radius: 50px; border: 2px solid #222; background: #8ee7f1; display: inline-block;'>
                <span style="font-size: 1.2rem; font-weight: bold;">Deepcatcher</span>
            </div>
            <div style="margin-bottom: 10px;">Subscribe for weekly updates. No spams ever!</div>
            <form style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;" onsubmit="return false;">
                <input type="email" placeholder="Placeholder: Your email address" style="padding: 6px 12px; border-radius: 6px; border: 2px solid #222; font-family: inherit; font-size: 1rem; outline: none; background: #f7f7f7;" disabled>
                <button style="background: #222; color: #fff; border: 2px solid #222; border-radius: 6px; padding: 6px 18px; font-family: inherit; font-size: 1rem; font-weight: bold; cursor: not-allowed;">Subscribe</button>
            </form>
            <div style="margin-bottom: 10px; font-size: 0.95rem;">Terms of Service</div>
            <div style="font-size: 0.95rem; margin-bottom: 10px;">Copyright © Deepcatcher 2025</div>
            <div style="font-size: 0.95rem; margin-bottom: 10px;">All rights reserved.</div>
            <div style="display: flex; gap: 16px; margin-top: 8px; justify-content: flex-end; align-items: center;">
                <span style="margin-right: 18px; font-size: 1rem; font-style: italic; color: #fff;">Made by Nicolas Mayoral.</span>
                <div style="display: flex; gap: 16px;">
                    <div style="text-align: center;">
                        <a href="https://github.com/NKAmazing" target="_blank" style="text-decoration: none;">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="38" height="38" style="border: 2px solid #222; border-radius: 6px; background: #f7f7f7; margin-bottom: 2px;">
                            <div style="font-size: 0.9rem; color: #00B8D4;">GitHub</div>
                        </a>
                    </div>
                    <div style="text-align: center;">
                        <a href="mailto:deepcatcher@contact.com" target="_blank" style="text-decoration: none;">
                            <img src="https://img.icons8.com/ios-filled/50/000000/new-post.png" alt="Email" width="38" height="38" style="border: 2px solid #222; border-radius: 6px; background: #f7f7f7; margin-bottom: 2px;">
                            <div style="font-size: 0.9rem; color: #00B8D4;">Email</div>
                        </a>
                    </div>
                    <div style="text-align: center;">
                        <a href="https://www.linkedin.com/in/nico-kamienny/" target="_blank" style="text-decoration: none;">
                            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="38" height="38" style="border: 2px solid #222; border-radius: 6px; background: #e6f2fb; margin-bottom: 2px;">
                            <div style="font-size: 0.9rem; color: #00B8D4;">Linkedin</div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )