import requests
from django.shortcuts import render


def cep(request):
    dados_endereco = None
    erro = None

    if request.method == 'POST':
        # Remove traços ou espaços do CEP digitado
        cep = request.POST.get('cep', '').replace('-', '').strip()

        # Valida se o CEP tem 8 dígitos numéricos
        if len(cep) == 8 and cep.isdigit():

            url = f'https://viacep.com.br/ws/{cep}/json/'

            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                dados = response.json()

                # O ViaCEP retorna status 200 mesmo se o CEP não existir,
                # mas envia a chave {'erro': True} no JSON.
                if 'erro' in dados:
                    erro = 'CEP não encontrado.'
                else:
                    dados_endereco = dados

            except requests.RequestException:
                erro = (
                    'Erro ao conectar com o serviço do ViaCEP. Tente novamente.'
                )
        else:
            erro = 'CEP inválido. Digite 8 números.'

        
 



    contexto = {'endereco': dados_endereco, 'erro': erro}

    return render(request, 'cep.html', contexto)
