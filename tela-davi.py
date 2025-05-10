import time
import os

def limpa_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def exibir_tela():
    limpa_tela()
    print("\n" + "="*40)
    print(" " * 10 + "T E L A  D O  D A V I")
    print("="*40 + "\n")
    print("Pressione Ctrl + C para sair.")

try:
    while True:
        exibir_tela()
        time.sleep(5)
except KeyboardInterrupt:
    print("\nEncerrando...")
