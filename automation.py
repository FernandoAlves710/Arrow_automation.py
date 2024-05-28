import streamlit as st
import PyPDF2
import pandas as pd
from io import BytesIO

def extrair_texto(pdf_file):
    text = ""
    with pdf_file as f:
        reader = PyPDF2.PdfFileReader(f)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def extrair_informacoes(texto, pagina):
    if pagina == 1:
        # Simulação de dados do Balanço Patrimonial
        data = {
            "Item": ["Ativos", "Passivos"],
            "Valor": ["100000", "50000"]
        }
    elif pagina == 2:
        # Simulação de dados da Demonstração do Resultado do Exercício
        data = {
            "Item": ["Receita", "Custos", "Despesas"],
            "Valor": ["80000", "30000", "20000"]
        }
    elif pagina == 3:
        # Simulação de dados do Fluxo de Caixa
        data = {
            "Item": ["Entradas", "Saídas"],
            "Valor": ["60000", "40000"]
        }
    elif pagina == 4:
        # Simulação de dados da Nota Explicativa de Custos e Despesas
        data = {
            "Item": ["Custos Extras", "Despesas Extras"],
            "Valor": ["5000", "3000"]
        }
    else:
        st.error("Página inválida!")
        return None
    
    return pd.DataFrame(data)

def main():
    st.title("Extrator de Dados Financeiros")

    pdf_file = st.file_uploader("Selecione o arquivo PDF", type="pdf")
    if pdf_file is not None:
        st.write("1. Pagina do BP:")
        texto = extrair_texto(pdf_file)
        tabela_bp = extrair_informacoes(texto, 1)
        if tabela_bp is not None:
            st.table(tabela_bp)

        st.write("2. Pagina da DRE:")
        texto = extrair_texto(pdf_file)
        tabela_dre = extrair_informacoes(texto, 2)
        if tabela_dre is not None:
            st.table(tabela_dre)

        st.write("3. Pagina do FC:")
        texto = extrair_texto(pdf_file)
        tabela_fc = extrair_informacoes(texto, 3)
        if tabela_fc is not None:
            st.table(tabela_fc)

        st.write("4. Pagina da NECD:")
        texto = extrair_texto(pdf_file)
        tabela_necd = extrair_informacoes(texto, 4)
        if tabela_necd is not None:
            st.table(tabela_necd)

if __name__ == "__main__":
    main()
