from utils import grabar_audio, generar_timestamp, transcode_audio, decode_transcription, check_there_is_command
from ui import window, state, update_ui
import multiprocessing
import threading
import os

cola = multiprocessing.Queue()
cola2 = multiprocessing.Queue()

def producer():
  while True:
    timestamp = generar_timestamp()
    grabar_audio(address, "./temp/" + timestamp + ".wav", duration)

    cola.put("./temp/" + timestamp + ".wav")

def consumer():
  while True:
    if not cola.empty():
        filename = cola.get()
        transcription = transcode_audio(filename)
        os.remove(filename)
        print("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        decoded_transcription = decode_transcription(transcription)
        cola2.put(decoded_transcription)
        


def producer_consumer():
    hilo_productor = multiprocessing.Process(target=producer)
    hilo_consumidor = multiprocessing.Process(target=consumer)

    hilo_productor.start()
    hilo_consumidor.start()

    while True:
        if not cola2.empty():
            decoded_transcription = cola2.get()
            if(check_there_is_command("REGISTRAR", decoded_transcription)):
                    state.set(state.get() + 1)
                    update_ui(state.get())


if __name__ == "__main__":
    address = "C8:9B:D7:DD:B0:E8"  
    filename = "./temp/grabacion.wav"
    duration = 5

    producer_consumer_thread = threading.Thread(target=producer_consumer)
    
    producer_consumer_thread.daemon = True
    producer_consumer_thread.start()

    update_ui(state.get())
    window.mainloop()

    exit(0)
