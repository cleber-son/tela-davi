# Tela do Davi - Modelo 1 (Terminal Gráfico)
import time
from datetime import datetime, timedelta
import os
import sys

# -------- CONFIGURAÇÃO INICIAL --------
TOTAL_REFEICOES = 5
HORA_INICIAL_REFEICAO = datetime.combine(datetime.today(), datetime.strptime("07:00", "%H:%M").time())
EMERGENCIA = "+55 11 98414-8756"

# -------- VARIÁVEIS DE CONTROLE --------
refeicoes_realizadas = 0
proxima_refeicao = HORA_INICIAL_REFEICAO
fim_ultima_refeicao = None
hora_agua = None
hora_abaixar_cama = None
modo_alerta = False

# -------- FUNÇÕES AUXILIARES --------
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar(horario):
    return horario.strftime("%H:%M") if horario else "--:--"

def alerta(msg):
    return f"\033[91m🔔 {msg}\033[0m"

def desenha_tela():
    agora = datetime.now()
    limpa_tela()
    print("\033[96m" + "="*50)
    print("🖥️  TELA DO DAVI".center(50))
    print("\033[93m📞 Em caso de emergência, ligar para", EMERGENCIA.center(50))
    print("\033[96m" + "="*50 + "\033[0m")
    print(f"📆 Data: {agora.strftime('%d/%m/%Y')}    ⏰ Hora atual: {agora.strftime('%H:%M:%S')}")
    print(f"🍽️  Refeição atual: {refeicoes_realizadas + 1} de {TOTAL_REFEICOES}\n")
    print("✅ Início da refeição:", formatar(proxima_refeicao))
    print("🛑 Fim da refeição:", formatar(fim_ultima_refeicao))
    print("💧 Água liberada em:", formatar(hora_agua))
    print("⬇️  Baixar cama após:", formatar(hora_abaixar_cama))
    print("🍽️  Próxima refeição:", formatar(proxima_refeicao if refeicoes_realizadas < TOTAL_REFEICOES else None))
    print("\n🔔 ALERTAS:")

    alertas = []
    if fim_ultima_refeicao:
        agora = datetime.now()
        if agora >= hora_agua and agora < hora_abaixar_cama:
            alertas.append(alerta("Hora de oferecer 200ml de água!"))
        if agora >= hora_abaixar_cama and agora < proxima_refeicao:
            alertas.append(alerta("Pode abaixar a cama!"))
        if agora >= proxima_refeicao:
            alertas.append(alerta("Hora da próxima refeição!"))
    if alertas:
        for msg in alertas:
            print(msg)
        return True  # Modo alerta ligado
    return False

# -------- LOOP PRINCIPAL --------
try:
    while refeicoes_realizadas < TOTAL_REFEICOES:
        modo_alerta = desenha_tela()

        if modo_alerta:
            for i in range(5):
                print("\a", end='')  # Beep (se suportado)
                time.sleep(0.5)
                limpa_tela()
                time.sleep(0.3)
                desenha_tela()
        else:
            time.sleep(1)

        print("\n[ENTER] para informar fim da refeição | [Ctrl+C] para sair")
        entrada = input("→ Aguardando...")
        fim_ultima_refeicao = datetime.now()
        hora_agua = fim_ultima_refeicao + timedelta(hours=1)
        hora_abaixar_cama = hora_agua + timedelta(minutes=40)
        proxima_refeicao = fim_ultima_refeicao + timedelta(hours=3)
        refeicoes_realizadas += 1

except KeyboardInterrupt:
    print("\nEncerrando sistema...")
