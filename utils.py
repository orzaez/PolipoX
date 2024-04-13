import pyaudio
import wave
import pyttsx3
import datetime
from faster_whisper import WhisperModel
import requests


def iniciar_grabadora():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=96000,
                    input=True,
                    frames_per_buffer=1024)
    return p, stream

def grabar_audio(address, filename, duration, p, stream):
    wf = wave.open(filename, "wb")
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(96000)

    for i in range(int(duration * 96000 / 1024)):
        data = stream.read(1024)
        wf.writeframes(data)

    wf.close()

def cerrar_grabadora(p, stream):
    stream.stop_stream()
    stream.close()
    p.terminate()


def generar_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp

def reproducir_texto(address, text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150) 
    engine.setProperty("volume", 0.75)  

    voice = engine.getProperty('voices')[0]
    engine.setProperty("voice", voice.id)

    engine.say(text)
    engine.runAndWait()

    print(f"Texto reproducido en {address}")

def transcode_audio(filename):
    # model_size = "base"

    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # segments, info = model.transcribe(filename, beam_size=1, language="es", vad_filter=True,vad_parameters=dict(min_silence_duration_ms=500))

    # for segment in segments:
    #      return segment.text

    # return "" 
    file = {'audio_file': open(filename, 'rb')}

    # Enviar la petición HTTP al servidor
    response = requests.post('http://ec2-3-90-230-145.compute-1.amazonaws.com:8080/transcribe', files=file)

    # Procesar la respuesta
    if response.status_code == 200:
        transcribed_text =  response.json()["text"]
        print(transcribed_text)
        return transcribed_text
    else:
        print(f'Error al transcribir el audio: {response.status_code}')

def decode_transcription(transcription):  
  cadena_mayusculas = transcription.upper()
  
  return cadena_mayusculas

def check_there_is_command(command, decoded_transcription):
    return command in decoded_transcription

