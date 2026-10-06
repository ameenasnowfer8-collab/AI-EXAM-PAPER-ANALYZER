import streamlit as st
from ocr import extract_text
from analyzer import analyze_questions

st.set_page_config(
    page_title="AI Exam Paper Analyzer",
    page_icon="📄"
)

st.title("📄 AI Exam Paper Analyzer")
st.write("Upload an exam paper and analyze it using OCR and AI.")

uploaded_file = st.file_uploader(
    "Upload your exam paper",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.success("Exam paper uploaded successfully!")

    # Display uploaded image
    st.image(
        uploaded_file,
        caption="Uploaded Exam Paper",
        use_container_width=True
    )

    if st.button("🔍 Analyze Exam Paper"):

        with st.spinner("Extracting text using OCR..."):

            text = extract_text(uploaded_file)

        if text.strip():

            st.subheader("📄 Extracted Text")

            st.text_area(
                "OCR Result",
                text,
                height=300
            )

            with st.spinner("Analyzing questions using AI..."):

                result = analyze_questions(text)

            st.subheader("🤖 AI Analysis")

            st.write(result)

        else:

            st.error(
                "No text could be extracted from the image."
            )