import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="QR Code Generator", page_icon="🔳")
st.title("🔳 QR Code Generator App")

text = st.text_input("Enter text or URL to convert into QR Code:")

if st.button("Generate"):
    if text.strip() == "":
        st.warning("Please enter something!")
    else:
        qr = qrcode.make(text).convert("RGB")  # Ensure compatibility
        buf = BytesIO()
        qr.save(buf, format="PNG")
        st.image(qr, caption="Here is your QR Code")

        st.download_button(
            label="Download QR Code",
            data=buf.getvalue(),
            file_name="qr_code.png",
            mime="image/png"
        )
