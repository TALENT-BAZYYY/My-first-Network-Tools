# 🛠️ My First Network & AI Tools

Welcome to my repository featuring my first projects focused on network security, automation, and Artificial Intelligence! Designed as a prototype portfolio for the KAIST application evaluation.

---

## 🇺🇸 ENGLISH VERSION

## 🧠 Repository Overview:

### 1. 🛡️ FEATURED PROJECT: Aegis-Net (Autonomous AI-Driven IPS/IDS)
A high-performance Automated Intrusion Detection and Prevention System.
* **Concept:** Synergizing low-level system statistics monitoring with Local Large Language Models (LLM) orchestration.
* **Core Logic:** The script continuously audits system sockets via `psutil`. Upon detecting anomalous socket multiplexing or potential connection flooding (e.g., DDoS vectors), the telemetry is instantly dispatched to the **Gemma 2 (9B)** neural core running via **Ollama**.
* **Autonomous Mitigation:** The AI engine acts as a cyber-analyst: evaluates threat severity, establishes mitigation frameworks, and outputs targeted low-level Netfilter commands (`iptables`) for real-time kernel-level packet dropping.

### 2. 🧟 Cyber-Necromancer (AI Server Resuscitation Tool)
An autonomous script for automated server health diagnostics and self-healing.
* **Logic:** Pings servers and traps crashes. Extracts raw log outputs, submits them to the local LLM, and automatically pipe the generated recovery Bash scripts straight into the Linux terminal.

### 3. 🤖 Local AI Assistant (`kaist.ai`)
An advanced AI assistant featuring a fully functional RAG (Retrieval-Augmented Generation) system.
* **Features:** Scans local PDF textbooks via OCR (`easyocr`) and references text data along with custom DuckDuckGo internet searches to construct accurate responses.

### 4. 📊 Network Perimeter & Provider Auditor (`net_audit.py`)
A fast script that parses your public IP addresses, analyzes your ISP data, and audits open perimeter ports (SSH, HTTP, HTTPS, RDP).

---

## 💻 How to Run Locally:
```bash
# Install dependencies
pip install ollama pypdf easyocr numpy rank_bm25 duckduckgo_search psutil

# Run scripts
python aegis_ids.py
python necromancer.py
python net_audit.py
python kaist.ai/app.py
```

---

## 🇷🇺 РУССКАЯ ВЕРСИЯ

## 🧠 Содержание репозитория:

### 1. 🛡️ ГЛАВНЫЙ ПРОЕКТ: Aegis-Net (Автономная ИИ-система IPS/IDS)
Высокопроизводительная система автоматического обнаружения и предотвращения вторжений в реальном времени.
* **Логика:** Скрипт непрерывно сканирует сетевые сокеты через `psutil`. При фиксации аномалий (флуд подключений, DDoS), данные передаются нейроядру **Gemma 2 (9B)** через **Ollama**. ИИ выполняет роль аналитика и выдает низкоуровневые команды брандмауэра (`iptables`) для мгновенной блокировки угрозы на уровне ядра.

### 2. 🧟 Cyber-Necromancer (ИИ-Реаниматор Серверов)
Автономный скрипт для мониторинга «падения» сетевых узлов. Извлекает логи ошибок, отправляет локальному ИИ и автоматически исполняет сгенерированную Bash-команду для починки системы.

### 3. 🤖 Локальный ИИ-Ассистент (`kaist.ai`)
Продвинутый ИИ-помощник с RAG-системой. Умеет считывать текст с PDF-учебников с помощью оптического распознавания (OCR) и искать свежие данные в интернете через DuckDuckGo API.

### 4. 📊 Аудитор Сетевой Безопасности (`net_audit.py`)
Скрипт для проверки внешнего IP, анализа провайдера (Aknet) и аудита уязвимых внешних портов роутера.

---
**Developer:** Islambek (17 years old, Bishkek, Kyrgyzstan) 🇰🇬  
