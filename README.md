# weather.py

Este código permite que o usuário insira o nome de uma cidade e, em seguida, consulta a API OpenWeatherMap para obter informações meteorológicas dessa cidade. O usuário deve fornecer sua própria chave de API, armazenada na variável APIKey. O código faz o seguinte:

1-Solicita que o usuário insira o nome da cidade.
<br>
2-Constrói uma URL de consulta para a API OpenWeatherMap, incluindo o nome da cidade e a chave de API fornecida.
<br>
3-Realiza uma solicitação GET à URL.
<br>
4-Verifica se a resposta HTTP tem um status de 200 (OK). Se sim, significa que a solicitação foi bem-sucedida.
<br>
5-Se a resposta for bem-sucedida, analisa os dados JSON recebidos, extraindo informações como o nome da cidade, temperatura, descrição do tempo, umidade e velocidade do vento.
<br>
6-Realiza algumas traduções simples das descrições do tempo, como "clear sky" para "Tempo Limpo", "scattered clouds" para "Nuvens Dispersas" e "overcast clouds" para "Nublado".
<br>
7-Exibe as informações meteorológicas na tela, incluindo o nome da cidade, temperatura, descrição do tempo, umidade e velocidade do vento.
