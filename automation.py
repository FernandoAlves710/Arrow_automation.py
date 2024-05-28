import streamlit as st
import PyPDF2

def extrair_texto(pdf_file):
    text = ""
    with pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def main():
    st.title("Extrator de Texto de PDF")

    pdf_file = st.file_uploader("Selecione o arquivo PDF", type="pdf")
    if pdf_file is not None:
        st.write(f"PDF selecionado: {pdf_file.name}")

        texto = extrair_texto(pdf_file)
        st.write("Texto extraído:")
        st.text(texto)

if __name__ == "__main__":
    main()
