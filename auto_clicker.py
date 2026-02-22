import time
from pynput import keyboard, mouse

def auto_clicker(interval):
    running = False  # Variável para controlar o estado do Auto Clicker

    def on_press(key):
        nonlocal running
        if key == keyboard.Key.f2:
            running = not running  # Alterna o estado do Auto Clicker

    def click_thread():
        while True:
            if running:
                mouse.Controller().click(mouse.Button.left)
                time.sleep(interval)

    # Cria o listener para a tecla pressionada
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Inicia a thread para emitir os cliques
    click_thread()

interval = 0.001  # Intervalo de clique em segundos
auto_clicker(interval)