from utils import cerrar_grabadora, iniciar_grabadora, grabar_audio, generar_timestamp, transcode_audio, decode_transcription, check_there_is_command
from ui import window, state, update_ui
import multiprocessing
import threading
import os
import time

cola = multiprocessing.Queue()
ui_queue = multiprocessing.Queue()
signal_event = multiprocessing.Event()

def producer():
  p, stream = iniciar_grabadora()
  try:
    while True:
      timestamp = generar_timestamp()
      not_empty = grabar_audio(address, "./temp/" + timestamp + ".wav", duration, p, stream)
      if not_empty:
        cola.put("./temp/" + timestamp + ".wav")
      else:
        os.remove("./temp/" + timestamp + ".wav")

      if not signal_event.is_set():
        signal_event.set()

  except KeyboardInterrupt:
     cerrar_grabadora(p, stream)



def consumer():
  pid = os.getpid()
  os.system("sudo renice -n -19 -p " + str(pid))
  while True:
    if not cola.empty():
      filename = cola.get()
      transcription = transcode_audio(filename)
      os.remove(filename)
      decoded_transcription = decode_transcription(transcription)
      if(check_there_is_command("REGISTRAR", decoded_transcription)):
        while not cola.empty():
          filename = cola.get()
          os.remove(filename)
        ui_queue.put("NEXT_STATE")

    else:
       signal_event.wait()
       signal_event.clear()

def producer_consumer():
    hilo_consumidor = multiprocessing.Process(target=consumer)
    hilo_productor = multiprocessing.Process(target=producer)
  
    hilo_consumidor.start()
    hilo_productor.start()

    while True:
        if not ui_queue.empty():
          ui_command = ui_queue.get()
          if(ui_command == "NEXT_STATE"):
            state.set(state.get() + 1)
            update_ui(state.get())
             



if __name__ == "__main__":
    address = "C8:9B:D7:DD:B0:E8"  
    filename = "./temp/grabacion.wav"
    duration = 2

    producer_consumer_thread = threading.Thread(target=producer_consumer)
    
    producer_consumer_thread.start()

    update_ui(state.get())
    window.mainloop()

    exit(0)
