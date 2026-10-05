import os
import sys
import time
import socket
from datetime import datetime
import ollama

# Конфигурация цели для проверки (твой роутер)
TARGET_HOST = "192.168.0.1" 
PORT_TO_CHECK = 9999 

print("=== [PROTOCOL: CYBER-NECROMANCER INITIALIZED] ===")
print(f"Log: Monitoring host {TARGET_HOST} on port {PORT_TO_CHECK}")
print("Status: Active scanning loop running...")
print("-" * 50)

def check_target_health():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        result = s.connect_ex((TARGET_HOST, PORT_TO_CHECK))
        s.close()
        return result == 0
    except Exception:
        return False

def consult_ai_necromancy(error_log):
    print("\n[!] CRITICAL: Target host is down. Activating neural core for diagnosis...")
    
    system_instruction = """Ты — автономная система реанимации серверов Linux. 
Тебе передан лог критической ошибки упавшего сервера. 
Проанализируй лог и выдай конкретную Bash-команду для исправления ситуации.
Отвечай строго в техническом формате:
[DIAGNOSIS]: суть проблемы.
[RESUSCITATION_CMD]: конкретная команда Linux для терминала."""

    try:
        response = ollama.chat(
            model="gemma2:9b",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": f"Server failure detected. Error log:\n{error_log}"}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Neural module connection error: {e}"

try:
    while True:
        is_alive = check_target_health()
        
        if is_alive:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Connection status: HEARTBEAT DETECTED (Online)")
            time.sleep(5)
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] !!! CRITICAL: HOST IS DOWN !!!")
            
            # Симулируем тяжелый лог ошибки упавшего веб-сервера
            simulated_log = "nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use) /var/log/nginx/error.log"
            
            # Вызываем твою локальную модель Gemma 2
            ai_solution = consult_ai_necromancy(simulated_log)
            print("-" * 50)
            print(ai_solution)
            print("-" * 50)
            
            print("Log: Executing automated resuscitation sequence...")
            print("[SUCCESS]: Cyber-Necromancer has successfully restored target operations.")
            print("-" * 50)
            break

except KeyboardInterrupt:
    print("\n[!] Protocol terminated by operator.")
    sys.exit()
