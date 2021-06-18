# Bot Google Calendar para Discord

Bot simples que obtem os reuniões agendadadas do dia envia uma notifiação em uma canal no discord, ou pode ser chamado, por comando, solicitando a agenda do dia.

## Requisitos

- Crie um BOT no [Portal de desenvolvimento doDiscord](https://discord.com/developers/applications)
- Crie uma credencial do google api, [Veja aqui como criar uma](https://karenapp.io/articles/how-to-automate-google-calendar-with-python-using-the-calendar-api/)

- Python >= 3.6 
- Pip3 >= 18.0

`sudo apt install -y python3-venv`
`python3 -m venv my_env`
`source my_env/bin/activate`
`pip3 install -r requirements.txt`

## Uso Basico

1. Edite o arquivo config.json.example e salve como confi.json

2. Baixe o arquivo credentials.json e coloque na pasta raiz - Veja no tutorial acima como criar uma credencial.

3. Rode python3 bot.py
