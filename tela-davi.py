# Tela do Davi - Modelo 1 (Terminal)
import time
from datetime import datetime, timedelta
import os

# -------- CONFIGURAÇÃO INICIAL --------
TOTAL_REFEICOES = 5
HORA_INICIAL_REFEICAO = datetime.combine(datetime.today(), datetime.strptime("07:00", "%H:%M").time())

# -------- VARIÁVEIS DE CONTROLE --------
refeicoes_realizadas = 0
proxima_refeicao = HORA_INICIAL_REFEICAO
fim_ultima_refeicao = None
hora_agua = None
hora_abaixar_cama = None

# -------- FUNÇÕES AUXILIARES --------
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatar(horario):
    return horario.strftime("%H:%M") if horario else "--:--"

def alerta(msg):
    print(f"\033[91m🔔 {msg}\033[0m")

# -------- LOOP PRINCIPAL --------
while refeicoes_realizadas < TOTAL_REFEICOES:
    limpa_tela()
    agora = datetime.now()

    print("📆 Data:", agora.strftime("%d/%m/%Y"), "  ⏰ Hora atual:", agora.strftime("%H:%M:%S"))
    print(f"🍽️  Refeição atual: {refeicoes_realizadas + 1} de {TOTAL_REFEICOES}\n")

    print("✅ Início da refeição:", formatar(proxima_refeicao))
    print("🛑 Fim da refeição:", formatar(fim_ultima_refeicao))
    print("💧 Água liberada em:", formatar(hora_agua))
    print("⬇️  Baixar cama após:", formatar(hora_abaixar_cama))
    print("🍽️  Próxima refeição:", formatar(proxima_refeicao if refeicoes_realizadas < TOTAL_REFEICOES else None))

    print("\n🔔 ALERTAS:")
    if fim_ultima_refeicao:
        if agora >= hora_agua and agora < hora_abaixar_cama:
            alerta("Hora de oferecer 200ml de água!")
        if agora >= hora_abaixar_cama and agora < proxima_refeicao:
            alerta("Pode abaixar a cama!")
        if agora >= proxima_refeicao:
            alerta("Hora da próxima refeição!")

    print("\n[ENTER] para informar fim da refeição | [Ctrl+C] para sair")
    try:
        entrada = input("→ Aguardando...")
        fim_ultima_refeicao = datetime.now()
        hora_agua = fim_ultima_refeicao + timedelta(hours=1)
        hora_abaixar_cama = hora_agua + timedelta(minutes=40)
        proxima_refeicao = fim_ultima_refeicao + timedelta(hours=3)
        refeicoes_realizadas += 1
    except KeyboardInterrupt:
        print("\nEncerrando sistema...")
        break
