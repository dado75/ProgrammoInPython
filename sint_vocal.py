from gtts import gTTS
#import subprocess

text = """
Rilascio rotante

Garuda Linux è una distribuzione a rilascio progressivo basata su Arch Linux che garantisce di ricevere sempre gli ultimi aggiornamenti software.

Usiamo solo un repository aggiuntivo sopra i repository Arch Linux, posizionandoci molto vicini ad Arch Linux senza dover installare il sistema con la CLI.
"""
tts = gTTS(text=text, lang='it')
tts.save("tts_output_audio.mp3")
print("tutto fatto, file salvato!")
#subprocess.run(["tts_output_audio.mp3"])