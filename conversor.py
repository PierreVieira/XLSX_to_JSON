import json

import pandas as pd

objeto_jason = {
    'data': []
}


def formatar_porcentagem(dado):
    if type(dado) == str:
        return dado[:-1]
    else:
        return str(dado)


def escrever_json(objeto):
    with open('atomos_json.json', 'w', encoding='utf-8') as file_json:
        json.dump(objeto, file_json, ensure_ascii=False)


def criar_atomo(nome, descricao, classificacao, numero_atomico, simbolo_atomico, numero_de_massa, grupo, periodo,
                ano_da_descoberta, numero_cas, quem_descobriu, densidade, ponto_de_fusao, ponto_de_ebulicao, valencia,
                quadra, composicao_universo, composicao_sol, composicao_oceano, composicao_corpo_humano,
                composicao_crosta_terrestre, composicao_meteoritos):
    return {
        'visao geral': {
            'nome': nome,
            'descricao': descricao,
            'classificacao': classificacao,
            'numero atomico': numero_atomico,
            'simbolo atomico': simbolo_atomico,
            'numero de massa': numero_de_massa,
            'grupo': grupo,
            'periodo': periodo,
            'ano da descoberta': ano_da_descoberta,
            'numero cas': numero_cas,
            'quem descobriu': quem_descobriu
        },
        'propriedades físicas': {
            'densidade': densidade,
            'ponto de fusao': ponto_de_fusao,
            'ponto de ebulicao': ponto_de_ebulicao,
            'valencia': valencia,
            'quadra': quadra
        },
        'composicao': {
            'universo': formatar_porcentagem(composicao_universo),
            'sol': formatar_porcentagem(composicao_sol),
            'oceano': formatar_porcentagem(composicao_oceano),
            'corpo humano': formatar_porcentagem(composicao_corpo_humano),
            'crosta terrestre': formatar_porcentagem(composicao_crosta_terrestre),
            'meteoritos': formatar_porcentagem(composicao_meteoritos)
        }
    }


infos_excel = pd.read_excel('atomos_info_base.xlsx')
lista_atomos = [criar_atomo(linha[1]['Nome'], linha[1]['Descrição'], linha[1]['Classificação'], linha[1]['Número '
                                                                                                         'Atômico'],
                            linha[1]['Símbolo Atômico'], linha[1]['Número de Massa'], linha[1]['Grupo'],
                            linha[1]['Período'], linha[1]['Ano da descoberta'], linha[1]['Número CAS'],
                            linha[1]['Quem Descobriu'], linha[1]['Densidade'], linha[1]['Ponto de Fusão (°C)'],
                            linha[1]['Ponto de Ebulição (°C)'], linha[1]['Valência'], linha[1]['Quadra'],
                            linha[1]['Universo'], linha[1]['Sol'], linha[1]['Oceano'], linha[1]['Corpo Humano'],
                            linha[1]['Crosta Terrestre'], linha[1]['Meteoritos']) for linha in infos_excel.iterrows()]
objeto_jason['data'] = lista_atomos
escrever_json(objeto_jason)
