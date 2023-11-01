import requests

cidade = input('Digite o nome da cidade: ')
APIKey = 'Sua APIKey'

url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&appid={APIKey}'

response = requests.get(url)

if response.status_code == 200:
    
    data = response.json()

    nome_cidade = data['name']
    temperatura = data['main']['temp']
    tempo_descricao = data['weather'][0]['description']
    humidade = data['main']['humidity']
    vento = data['wind']['speed']*3.6

    if tempo_descricao == "clear sky":
        tempo_descricao = "Tempo Limpo"
    
    elif tempo_descricao == "scattered clouds":
        tempo_descricao = "Nuvens Dispersas"
    
    elif tempo_descricao == "overcast clouds":
        tempo_descricao = "Nublado"

    
    print(f'\nCidade: {nome_cidade}')
    print(f'Temperatura atual: {temperatura}°C')
    print(f'Descrição do Tempo: {tempo_descricao}')
    print(f'Humidade: {humidade}%')
    print(f'Velocidade do Vento: {round(vento,0)}Km/h')
    print('\n')

else:
    print("Infelizmente não conseguimos completar a sua solicitação :(")
