import socket
import sys
import json
import urllib.request
from datetime import datetime

print("=== Network Security & Provider Audit Tool ===")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# 1. Анализ внешнего подключения и провайдера
print("[*] Analyzing external network parameters...")
try:
    # Запрос к доверенному API для определения внешнего IP и провайдера
    with urllib.request.urlopen("https://ipapi.co", timeout=5) as response:
        ip_data = json.loads(response.read().decode())
        
        public_ip = ip_data.get("ip", "Unknown")
        org = ip_data.get("org", "Unknown") # Здесь отобразится твой провайдер (например, Aknet)
        city = ip_data.get("city", "Unknown")
        country = ip_data.get("country_name", "Unknown")
        
        print(f" -> Public IP Address: {public_ip}")
        print(f" -> Internet Provider: {org}")
        print(f" -> Location: {city}, {country}\n")
except Exception as e:
    print(f" [!] Unable to retrieve public IP data: {e}\n")
    public_ip = "127.0.0.1"

# 2. Сканирование критических внешних портов роутера
print("[*] Scanning external perimeter ports for vulnerabilities...")
# Список портов, которые чаще всего атакуют хакеры, если они открыты в интернет
critical_ports = {
    21: "FTP (File Transfer)",
    22: "SSH (Secure Shell)",
    23: "Telnet (Unsecure)",
    80: "HTTP (Web Interface)",
    443: "HTTPS (Secure Web)",
    3389: "RDP (Remote Desktop)"
}

for port, description in critical_ports.items():
    try:
        # Создаем сокет для проверки
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        
        # Пробуем подключиться к твоему внешнему IP
        result = s.connect_ex((public_ip, port))
        
        if result == 0:
            print(f" -> Port {port} [{description}]: OPEN !! (Security Risk)")
        else:
            print(f" -> Port {port} [{description}]: CLOSED (Secure)")
            
        s.close()
    except KeyboardInterrupt:
        print("\n[!] Scan terminated by user.")
        sys.exit()
    except Exception as e:
        print(f" [!] Error scanning port {port}: {e}")

print("\n=== Audit Completed Successfully ===") 
