import streamlit as st
import PyPDF2
import pandas as pd

def extrair_texto(pdf_file):
    text = ""
    with pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def extrair_informacoes(texto, pagina):
    if pagina == 1:
        # Extrair informações do Balanço Patrimonial
        inicio_ativo = texto.find("ATIVO")
        inicio_passivo = texto.find("PASSIVO E PATRIMÔNIO LÍQUIDO")

        if inicio_ativo != -1 and inicio_passivo != -1:
            texto_ativo = texto[inicio_ativo:inicio_passivo]
            texto_passivo = texto[inicio_passivo:]

            # Dividir o texto do Balanço Patrimonial em seções
            secoes_ativo = texto_ativo.split("\n")
            secoes_passivo = texto_passivo.split("\n")

            # Criar listas para armazenar os dados das seções do Balanço Patrimonial
            ativo_lista = []
            passivo_lista = []

            # Iterar sobre as seções do Ativo
            for linha in secoes_ativo:
                if linha.strip():
                    ativo_lista.append(linha.strip())

            # Iterar sobre as seções do Passivo
            for linha in secoes_passivo:
                if linha.strip():
                    passivo_lista.append(linha.strip())

            # Criar DataFrames para exibir as informações
            df_ativo = pd.DataFrame({"Ativo": ativo_lista})
            df_passivo = pd.DataFrame({"Passivo": passivo_lista})

            # Exibir os DataFrames na interface
            st.write("Ativo:")
            st.table(df_ativo)
            st.write("Passivo e Patrimônio Líquido:")
            st.table(df_passivo)
        else:
            st.error("Não foi possível encontrar todas as seções necessárias no Balanço Patrimonial.")
    elif pagina == 2:
        # Extrair informações da Demonstração do Resultado do Exercício
        inicio_receita = texto.find("Vendas/faturamento (líquido)")
        inicio_custo = texto.find("Custo de bens vendidos")
        inicio_despesas_gerais = texto.find("Vendas, despesas gerais e administrativas")
        inicio_depreciacao = texto.find("D&A")
        inicio_lucro_operacional = texto.find("Lucro operacional, relatado")
        inicio_despesa_juros = texto.find("Despesas de juros")
        inicio_imposto_renda = texto.find("Imposto de renda")
        inicio_resultado_liquido = texto.find("Resultado líquido")

        if all(
            inicio_receita != -1, inicio_custo != -1, inicio_despesas_gerais != -1,
            inicio_depreciacao != -1, inicio_lucro_operacional != -1, inicio_despesa_juros != -1,
            inicio_imposto_renda != -1, inicio_resultado_liquido != -1
        ):
            # Extrair as informações para cada seção
            receita = texto[inicio_receita:inicio_custo]
            custo = texto[inicio_custo:inicio_despesas_gerais]
            despesas_gerais = texto[inicio_despesas_gerais:inicio_depreciacao]
            depreciacao = texto[inicio_depreciacao:inicio_lucro_operacional]
            lucro_operacional = texto[inicio_lucro_operacional:inicio_despesa_juros]
            despesa_juros = texto[inicio_despesa_juros:inicio_imposto_renda]
            imposto_renda = texto[inicio_imposto_renda:inicio_resultado_liquido]
            resultado_liquido = texto[inicio_resultado_liquido:]

            # Criar DataFrames para exibir as informações
            df_receita = pd.DataFrame({"Receita": [receita]})
            df_custo = pd.DataFrame({"Custo": [custo]})
            df_despesas_gerais = pd.DataFrame({"Despesas Gerais": [despesas_gerais]})
            df_depreciacao = pd.DataFrame({"Depreciação": [depreciacao]})
            df_lucro_operacional = pd.DataFrame({"Lucro Operacional": [lucro_operacional]})
            df_despesa_juros = pd.DataFrame({"Despesa de Juros": [despesa_juros]})
            df_imposto_renda = pd.DataFrame({"Imposto de Renda": [imposto_renda]})
            df_resultado_liquido = pd.DataFrame({"Resultado Líquido": [resultado_liquido]})

            # Exibir os DataFrames na interface
            st.write("Receita:")
            st.table(df_receita)
            st.write("Custo:")
            st.table(df_custo)
            st.write("Despesas Gerais:")
            st.table(df_despesas_gerais)
            st.write("Depreciação:")
            st.table(df_depreciacao)
            st.write("Lucro Operacional:")
            st.table(df_lucro_operacional)
            st.write("Despesa de Juros:")
            st.table(df_despesa_juros)
            st.write("Imposto de Renda:")
            st.table(df_imposto_renda)
            st.write("Resultado Líquido:")
            st.table(df_resultado_liquido)
        else:
            st.error("Não foi possível encontrar todas as seções necessárias na Demonstração do Resultado do Exercício.")
    elif pagina == 3:
        inicio_operacoes_continuas = texto.find("Receita de operações contínuas")
        inicio_depreciacao = texto.find("D&A")
        inicio_impostos_diferidos = texto.find("Impostos diferidos")
        inicio_participacao_minoritaria = texto.find("Participação não controladora/Participação minoritária")
        inicio_ganho_perda_subsidiaria = texto.find("Patrimônio líquido (ganho)/perda da subsidiária")
        inicio_participacao_lucros_coligadas = texto.find("Participação societária nos lucros das empresas coligadas")
        inicio_disposicoes = texto.find("Disposições")
        inicio_responsabilidades_pensoes = texto.find("Responsabilidades com pensões - alteração")
        inicio_venda_epi_investimentos = texto.find("Venda de EPI e investimentos")
        inicio_tributacao_operacionais = texto.find("Tributação – atividades operacionais")
        inicio_ajustes_juros_dividendos_operacionais = texto.find("Ajustes de juros e dividendos – atividades operacionais")
        inicio_ganho_perda_cambial = texto.find("Ganho/(perda) cambial e monetário")
        inicio_ganho_perda_atualizacao_monetaria = texto.find("Ganho/(perda) com atualização monetária")
        inicio_afudceq = texto.find("AFUDCEQ (fluxo de caixa)")
        inicio_outros_capital_nao_circulante = texto.find("Outros (capital não circulante)")
        inicio_contas_receber_diminuicao_aumento = texto.find("Contas a receber - diminuição (aumento)")
        inicio_estoque_diminuir_aumentar = texto.find("Estoque - diminuir (aumentar)")
        inicio_contas_pagar_aumento_diminuicao = texto.find("Contas a pagar/credores - aumento (diminuição)")
        inicio_passivos_acumulados_diminuicao_aumento = texto.find("Passivos acumulados - aumento (diminuição)")
        inicio_contas_pagar_passivos_acumulados_diminuicao_aumento = texto.find("Contas a pagar e passivos acumulados - aumento (diminuição)")
        inicio_imposto_renda_acumulado_diminuicao_aumento = texto.find("Imposto de renda - acumulado - aumento (diminuição)")
        inicio_avancos_cliente_diminuicao_aumento = texto.find("Avanços do cliente - aumento (diminuição)")
        inicio_ativos_passivos_circulantes_outros_variacao = texto.find("Ativos e passivos circulantes - outros - variação líquida")
        inicio_mudancas_capital_giro_relatadas = texto.find("Mudanças no capital de giro, relatadas")
        inicio_fluxo_caixa_atividades_operacionais = texto.find("Fluxo de caixa das atividades operacionais")
        
        if all(
            inicio_operacoes_continuas != -1, inicio_depreciacao != -1, inicio_impostos_diferidos != -1,
            inicio_participacao_minoritaria != -1, inicio_ganho_perda_subsidiaria != -1, inicio_participacao_lucros_coligadas != -1,
            inicio_disposicoes != -1, inicio_responsabilidades_pensoes != -1, inicio_venda_epi_investimentos != -1,
            inicio_tributacao_operacionais != -1, inicio_ajustes_juros_dividendos_operacionais != -1, inicio_ganho_perda_cambial != -1,
            inicio_ganho_perda_atualizacao_monetaria != -1, inicio_afudceq != -1, inicio_outros_capital_nao_circulante != -1,
            inicio_contas_receber_diminuicao_aumento != -1, inicio_estoque_diminuir_aumentar != -1, inicio_contas_pagar_aumento_diminuicao != -1,
            inicio_passivos_acumulados_diminuicao_aumento != -1, inicio_contas_pagar_passivos_acumulados_diminuicao_aumento != -1,
            inicio_imposto_renda_acumulado_diminuicao_aumento != -1, inicio_avancos_cliente_diminuicao_aumento != -1,
            inicio_ativos_passivos_circulantes_outros_variacao != -1, inicio_mudancas_capital_giro_relatadas != -1,
            inicio_fluxo_caixa_atividades_operacionais != -1
        ):
            # Extrair as informações para cada seção
            receita_operacoes_continuas = texto[inicio_operacoes_continuas:inicio_depreciacao]
            depreciacao = texto[inicio_depreciacao:inicio_impostos_diferidos]
            impostos_diferidos = texto[inicio_impostos_diferidos:inicio_participacao_minoritaria]
            participacao_minoritaria = texto[inicio_participacao_minoritaria:inicio_ganho_perda_subsidiaria]
            ganho_perda_subsidiaria = texto[inicio_ganho_perda_subsidiaria:inicio_participacao_lucros_coligadas]
            participacao_lucros_coligadas = texto[inicio_participacao_lucros_coligadas:inicio_disposicoes]
            disposicoes = texto[inicio_disposicoes:inicio_responsabilidades_pensoes]
            responsabilidades_pensoes = texto[inicio_responsabilidades_pensoes:inicio_venda_epi_investimentos]
            venda_epi_investimentos = texto[inicio_venda_epi_investimentos:inicio_tributacao_operacionais]
            tributacao_operacionais = texto[inicio_tributacao_operacionais:inicio_ajustes_juros_dividendos_operacionais]
            ajustes_juros_dividendos_operacionais = texto[inicio_ajustes_juros_dividendos_operacionais:inicio_ganho_perda_cambial]
            ganho_perda_cambial = texto[inicio_ganho_perda_cambial:inicio_ganho_perda_atualizacao_monetaria]
            ganho_perda_atualizacao_monetaria = texto[inicio_ganho_perda_atualizacao_monetaria:inicio_afudceq]
            afudceq = texto[inicio_afudceq:inicio_outros_capital_nao_circulante]
            outros_capital_nao_circulante = texto[inicio_outros_capital_nao_circulante:inicio_contas_receber_diminuicao_aumento]
            contas_receber_diminuicao_aumento = texto[inicio_contas_receber_diminuicao_aumento:inicio_estoque_diminuir_aumentar]
            estoque_diminuir_aumentar = texto[inicio_estoque_diminuir_aumentar:inicio_contas_pagar_aumento_diminuicao]
            contas_pagar_aumento_diminuicao = texto[inicio_contas_pagar_aumento_diminuicao:inicio_passivos_acumulados_diminuicao_aumento]
            passivos_acumulados_diminuicao_aumento = texto[inicio_passivos_acumulados_diminuicao_aumento:inicio_contas_pagar_passivos_acumulados_diminuicao_aumento]
            contas_pagar_passivos_acumulados_diminuicao_aumento = texto[inicio_contas_pagar_passivos_acumulados_diminuicao_aumento:inicio_imposto_renda_acumulado_diminuicao_aumento]
            imposto_renda_acumulado_diminuicao_aumento = texto[inicio_imposto_renda_acumulado_diminuicao_aumento:inicio_avancos_cliente_diminuicao_aumento]
            avancos_cliente_diminuicao_aumento = texto[inicio_avancos_cliente_diminuicao_aumento:inicio_ativos_passivos_circulantes_outros_variacao]
            ativos_passivos_circulantes_outros_variacao = texto[inicio_ativos_passivos_circulantes_outros_variacao:inicio_mudancas_capital_giro_relatadas]
            mudancas_capital_giro_relatadas = texto[inicio_mudancas_capital_giro_relatadas:inicio_fluxo_caixa_atividades_operacionais]
            fluxo_caixa_atividades_operacionais = texto[inicio_fluxo_caixa_atividades_operacionais:]
            
            # Criar DataFrames para exibir as informações
            df_operacoes_continuas = pd.DataFrame({"Receita de Operações Contínuas": [receita_operacoes_continuas]})
            df_depreciacao = pd.DataFrame({"D&A": [depreciacao]})
            df_impostos_diferidos = pd.DataFrame({"Impostos Diferidos": [impostos_diferidos]})
            df_participacao_minoritaria = pd.DataFrame({"Participação Minoritária": [participacao_minoritaria]})
            df_ganho_perda_subsidiaria = pd.DataFrame({"Ganho/Perda da Subsidiária": [ganho_perda_subsidiaria]})
            df_participacao_lucros_coligadas = pd.DataFrame({"Participação nos Lucros das Empresas Coligadas": [participacao_lucros_coligadas]})
            df_disposicoes = pd.DataFrame({"Disposições": [disposicoes]})
            df_responsabilidades_pensoes = pd.DataFrame({"Responsabilidades com Pensões": [responsabilidades_pensoes]})
            df_venda_epi_investimentos = pd.DataFrame({"Venda de EPI e Investimentos": [venda_epi_investimentos]})
            df_tributacao_operacionais = pd.DataFrame({"Tributação - Atividades Operacionais": [tributacao_operacionais]})
            df_ajustes_juros_dividendos_operacionais = pd.DataFrame({"Ajustes de Juros e Dividendos - Atividades Operacionais": [ajustes_juros_dividendos_operacionais]})
            df_ganho_perda_cambial = pd.DataFrame({"Ganho/Perda Cambial": [ganho_perda_cambial]})
            df_ganho_perda_atualizacao_monetaria = pd.DataFrame({"Ganho/Perda com Atualização Monetária": [ganho_perda_atualizacao_monetaria]})
            df_afudceq = pd.DataFrame({"AFUDCEQ (Fluxo de Caixa)": [afudceq]})
            df_outros_capital_nao_circulante = pd.DataFrame({"Outros (Capital Não Circulante)": [outros_capital_nao_circulante]})
            df_contas_receber_diminuicao_aumento = pd.DataFrame({"Contas a Receber - Diminuição/Aumento": [contas_receber_diminuicao_aumento]})
            df_estoque_diminuir_aumentar = pd.DataFrame({"Estoque - Diminuir/Aumentar": [estoque_diminuir_aumentar]})
            df_contas_pagar_aumento_diminuicao = pd.DataFrame({"Contas a Pagar - Aumento/Diminuição": [contas_pagar_aumento_diminuicao]})
            df_passivos_acumulados_diminuicao_aumento = pd.DataFrame({"Passivos Acumulados - Diminuição/Aumento": [passivos_acumulados_diminuicao_aumento]})
            df_contas_pagar_passivos_acumulados_diminuicao_aumento = pd.DataFrame({"Contas a Pagar e Passivos Acumulados - Diminuição/Aumento": [contas_pagar_passivos_acumulados_diminuicao_aumento]})
            df_imposto_renda_acumulado_diminuicao_aumento = pd.DataFrame({"Imposto de Renda Acumulado - Diminuição/Aumento": [imposto_renda_acumulado_diminuicao_aumento]})
            df_avancos_cliente_diminuicao_aumento = pd.DataFrame({"Avanços do Cliente - Diminuição/Aumento": [avancos_cliente_diminuicao_aumento]})
            df_ativos_passivos_circulantes_outros_variacao = pd.DataFrame({"Ativos e Passivos Circulantes - Outros - Variação Líquida": [ativos_passivos_circulantes_outros_variacao]})
            df_mudancas_capital_giro_relatadas = pd.DataFrame({"Mudanças no Capital de Giro, Relatadas": [mudancas_capital_giro_relatadas]})
            df_fluxo_caixa_atividades_operacionais = pd.DataFrame({"Fluxo de Caixa das Atividades Operacionais": [fluxo_caixa_atividades_operacionais]})
            
            # Exibir os DataFrames na interface
            st.write("Receita de Operações Contínuas:")
            st.table(df_operacoes_continuas)
            st.write("D&A:")
            st.table(df_depreciacao)
            st.write("Impostos Diferidos:")
            st.table(df_impostos_diferidos)
            st.write("Participação Minoritária:")
            st.table(df_participacao_minoritaria)
            st.write("Ganho/Perda da Subsidiária:")
            st.table(df_ganho_perda_subsidiaria)
            st.write("Participação nos Lucros das Empresas Coligadas:")
            st.table(df_participacao_lucros_coligadas)
            st.write("Disposições:")
            st.table(df_disposicoes)
            st.write("Responsabilidades com Pensões:")
            st.table(df_responsabilidades_pensoes)
            st.write("Venda de EPI e Investimentos:")
            st.table(df_venda_epi_investimentos)
            st.write("Tributação - Atividades Operacionais:")
            st.table(df_tributacao_operacionais)
            st.write("Ajustes de Juros e Dividendos - Atividades Operacionais:")
            st.table(df_ajustes_juros_dividendos_operacionais)
            st.write("Ganho/Perda Cambial:")
            st.table(df_ganho_perda_cambial)
            st.write("Ganho/Perda com Atualização Monetária:")
            st.table(df_ganho_perda_atualizacao_monetaria)
            st.write("AFUDCEQ (Fluxo de Caixa):")
            st.table(df_afudceq)
            st.write("Outros (Capital Não Circulante):")
            st.table(df_outros_capital_nao_circulante)
            st.write("Contas a Receber - Diminuição/Aumento:")
            st.table(df_contas_receber_diminuicao_aumento)
            st.write("Estoque - Diminuir/Aumentar:")
            st.table(df_estoque_diminuir_aumentar)
            st.write("Contas a Pagar - Aumento/Diminuição:")
            st.table(df_contas_pagar_aumento_diminuicao)
            st.write("Passivos Acumulados - Diminuição/Aumento:")
            st.table(df_passivos_acumulados_diminuicao_aumento)
            st.write("Contas a Pagar e Passivos Acumulados - Diminuição/Aumento:")
            st.table(df_contas_pagar_passivos_acumulados_diminuicao_aumento)
            st.write("Imposto de Renda Acumulado - Diminuição/Aumento:")
            st.table(df_imposto_renda_acumulado_diminuicao_aumento)
            st.write("Avanços do Cliente - Diminuição/Aumento:")
            st.table(df_avancos_cliente_diminuicao_aumento)
            st.write("Ativos e Passivos Circulantes - Outros - Variação Líquida:")
            st.table(df_ativos_passivos_circulantes_outros_variacao)
            st.write("Mudanças no Capital de Giro, Relatadas:")
            st.table(df_mudancas_capital_giro_relatadas)
            st.write("Fluxo de Caixa das Atividades Operacionais:")
            st.table(df_fluxo_caixa_atividades_operacionais)
        else:
            st.error("Não foi possível encontrar todas as seções necessárias no Fluxo de Caixa.")

# Título da aplicação
st.title("Extrator de Informações de Relatórios Financeiros")

# Upload do arquivo PDF
arquivo = st.file_uploader("Selecione o arquivo PDF", type="pdf")

# Selecionar a página do PDF
pagina_selecionada = st.radio("Selecione a página:", [1, 2, 3])

# Extrair texto e informações da página selecionada
if arquivo is not None:
    texto_pdf = extrair_texto(arquivo)
    extrair_informacoes(texto_pdf, pagina_selecionada)
