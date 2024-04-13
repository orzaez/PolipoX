import requests
import os

audio_file_path = 'audio.wav'

# Leer el archivo de audio
file = {'audio_file': open(audio_file_path, 'rb')}

# Enviar la petición HTTP al servidor
response = requests.post('http://ec2-3-90-230-145.compute-1.amazonaws.com:8080/transcribe', files=file)

# Procesar la respuesta
if response.status_code == 200:
    transcribed_text =  response.json()
    print(transcribed_text)
else:
    print(f'Error al transcribir el audio: {response.status_code}')
