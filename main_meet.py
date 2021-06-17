import socket

from vidstream import *
import tkinter as tk

import threading


indirizzo_ip_privato= socket.gethostbyname(socket.gethostname())
server = StreamingServer(indirizzo_ip_privato, 7777)
reciever = AudioReceiver(indirizzo_ip_privato, 6666)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=reciever.start_server)
    t1.start()
    t2.start()


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), 9999)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'), 8888)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()
#GUI
window = tk.Tk()
window.title('programma inutile')
window.geometry('300x200')

label_target_ip = tk.Label(window, text='Indirizzo di connessione:')
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text='Ascolta', width=50, command=start_listening())
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text='Attiva la videocamera', width=50, command=start_camera_stream())
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text='Condividi lo schermo', width=50, command=start_screen_sharing())
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text='Attiva il microfono', width=50, command=start_audio_stream())
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()
