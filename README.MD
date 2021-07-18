# Bot Calendly para Discord

Bot simples que obtem os reuniões agendadadas dos dia envia uma notifiação em uma canal no discord, ou pode ser chamado, por comando, solicitando a agenda do dia.

## Requisitos

- Crie um BOT no[Portal de desenvolvimento doDiscord](https://discord.com/developers/applications)

- Python >= 3.6 
- Pip3 >= 18.0

`sudo apt install -y python3-venv`
`python3 -m venv my_env`
`source my_env/bin/activate`
`pip3 install -r requirements.txt`

## Basic Usage

1. Edit the ``src/welcome-message.md`` as you please.

2. Set the API_TOKEN env var from the Discord Application bot

3. Then run the project with local Python or as a Docker container (recommended).

### Local

``make local`` installs dependencies and run the application.

### Docker

Execute ``make`` or ``make run`` command to build and run the docker container. When you are done, ``make clean`` will remove the docker container and image.