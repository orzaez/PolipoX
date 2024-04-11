import pyaudio
import wave
import pyttsx3
from faster_whisper import WhisperModel

def grabar_audio(address, filename, duration):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=96000,
                    input=True,
                    frames_per_buffer=1024)

    wf = wave.open(filename, "wb")
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(96000)

    for i in range(int(duration * 96000 / 1024)):
        data = stream.read(1024)
        wf.writeframes(data)

    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

    print(f"Grabación de audio de {address} finalizada. Guardada como {filename}")



def reproducir_texto(address, text):
    # Configurar pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Ajustar la velocidad de habla
    engine.setProperty("volume", 0.75)  # Ajustar el volumen

    voice = engine.getProperty('voices')[0]
    # Seleccionar el dispositivo de salida Bluetooth por MAC
    engine.setProperty("voice", voice.id)

    # Reproducir el texto
    engine.say(text)
    engine.runAndWait()

    print(f"Texto reproducido en {address}")


def transcode_audio(filename):
    model_size = "base"

    # Run on GPU with FP16
    # model = WhisperModel(model_size, device="cuda", compute_type="float16")

    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(filename, beam_size=1, language="es")

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

address = "C8:9B:D7:DD:B0:E8"  
filename = "./temp/grabacion.wav"
duration = 3

grabar_audio(address, filename, duration)
transcode_audio(filename)