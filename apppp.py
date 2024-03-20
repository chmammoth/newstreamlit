import streamlit as st
import qrcode


def creat_qrcode(tex):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(tex)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")





text = st.text_area("enter text")
submitbtn = st.button("Enter")

if submitbtn:
    creat_qrcode(text)
    st.image("qrcode.png")
    st.success(text)
