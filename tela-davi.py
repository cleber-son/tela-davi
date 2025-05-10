import time
import os

def limpa_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def exibir_tela():
    limpa_tela()
    
    # Cores ANSI
    cor_amarela = '\033[93m'
    cor_azul = '\033[94m'
    cor_verde = '\033[92m'
    cor_reset = '\033[0m'
    
    boneco = f"""{cor_azul}
       [◉_◉]
      /|\\   {cor_amarela}<-- Davi
      / \\ 
    {cor_reset}"""
    
    print(f"{cor_verde}\n" + "="*40)
    print(" " * 10 + "T E L A  D O  D A V I")
    print("="*40 + "\n")
    print(boneco)
    print(f"{cor_amarela}Pressione Ctrl + C para sair.{cor_reset}")

try:
    while True:
        exibir_tela()
        time.sleep(5)
except KeyboardInterrupt:
    print("\nEncerrando...")
