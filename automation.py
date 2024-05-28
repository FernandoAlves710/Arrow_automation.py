import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
from io import BytesIO

def extrair_texto(pdf_file):
    text = ""
    filename = pdf_file.name
    with pdf_file:
        pdf_document = fitz.open(BytesIO(pdf_file.read()))
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
    return text, filename

def extrair_informacoes(texto, pagina):
    # Simulação de dados para demonstração
    if pagina == 1:
        data = {
            "Item": ["Ativos", "Passivos"],
            "Valor": ["100000", "50000"]
        }
    elif pagina == 2:
        data = {
            "Item": ["Receita", "Custos", "Despesas"],
            "Valor": ["80000", "30000", "20000"]
        }
    elif pagina == 3:
        data = {
            "Item": ["Entradas", "Saídas"],
            "Valor": ["60000", "40000"]
        }
    elif pagina == 4:
        data = {
            "Item": ["Custos Extras", "Despesas Extras"],
            "Valor": ["5000", "3000"]
        }
    else:
        st.error("Página inválida! Por favor, selecione uma página válida.")
        return None
    
    return pd.DataFrame(data)

def main():
    st.title("Extrator de Dados Financeiros")

    pdf_file = st.file_uploader("Selecione o arquivo PDF", type="pdf")
    if pdf_file is not None:
        texto, filename = extrair_texto(pdf_file)
        st.write(f"PDF selecionado: {filename}")

        st.write("1. Pagina do BP:")
        tabela_bp = extrair_informacoes(texto, 1)
        if tabela_bp is not None:
            st.table(tabela_bp)

        st.write("2. Pagina da DRE:")
        tabela_dre = extrair_informacoes(texto, 2)
        if tabela_dre is not None:
            st.table(tabela_dre)

        st.write("3. Pagina do FC:")
        tabela_fc = extrair_informacoes(texto, 3)
        if tabela_fc is not None:
            st.table(tabela_fc)

        st.write("4. Pagina da NECD:")
        tabela_necd = extrair_informacoes(texto, 4)
        if tabela_necd is not None:
            st.table(tabela_necd)

if __name__ == "__main__":
    main()
