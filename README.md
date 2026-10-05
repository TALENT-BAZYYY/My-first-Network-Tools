# 🛠️ My First Network & AI Tools

Welcome to my repository featuring my first projects focused on network security, automation, and Artificial Intelligence!

---

## 🇺🇸 ENGLISH VERSION

## 🧠 Repository Overview:

### 1. 🤖 Local AI Assistant (`kaist.ai`)
An advanced AI assistant powered by the **Ollama** framework and the **Gemma 2 (9B)** language model.
* **Tech Stack:** Python, Ollama, EasyOCR, PyPDF, BM25Okapi, DuckDuckGo Search API.
* **Features:** A fully functional RAG (Retrieval-Augmented Generation) system. The AI scans local PDF textbooks using Optical Character Recognition (OCR) and leverages this knowledge for responses. It also includes a web search module for live data retrieval via DuckDuckGo.

### 2. 🛡️ Network Security Audit Tool (`net_audit.py`)
A script designed for quick analysis of home internet parameters and external perimeter security.
* **Features:** Automatically detects public IP address, location, and the Internet Service Provider (ISP). Scans critical router ports (SSH, HTTP, HTTPS, RDP) most vulnerable to cyber attacks, verifying their status (`OPEN/CLOSED`).

---

## 💻 How to Run Locally:

1. Install dependencies:
   ```bash
   pip install ollama pypdf easyocr numpy rank_bm25 duckduckgo_search
   ```
2. Run Network Audit:
   ```bash
   python net_audit.py
   ```
3. Run AI Assistant:
   ```bash
   python kaist.ai/app.py
   ```

---
**Developer:** Islambek (17 years old, Bishkek, Kyrgyzstan) 🇰🇬  
*Studying Linux system administration, network cybersecurity, and local LLM integration.*

---

## 🇷🇺 РУССКАЯ ВЕРСИЯ

## 🧠 Содержание репозитория:

### 1. 🤖 Локальный ИИ-Ассистент (`kaist.ai`)
Продвинутый ИИ-помощник, разработанный на базе фреймворка **Ollama** и языковой модели **Gemma 2 (9B)**. 
* **Технологии:** Python, Ollama, EasyOCR, PyPDF, BM25Okapi, DuckDuckGo Search API.
* **Фишка:** Реализована полноценная RAG-система. ИИ умеет сканировать локальные PDF-книги с помощью оптического распознавания текста (OCR) и использовать эти знания при ответах. Также встроен модуль экстренного поиска актуальной информации в интернете через пул DuckDuckGo.

### 2. 🛡️ Аудитор Сетевой Безопасности (`net_audit.py`)
Инженерный скрипт для быстрого анализа параметров домашнего интернета и сетевого периметра.
* **Функционал:** Автоматически определяет внешний IP-адрес, страну подключения и текущего интернет-провайдера (ISP). Выполняет сканирование критических внешних портов роутера (SSH, HTTP, HTTPS, RDP), уязвимых для хакерских атак, проверяя их на статус `OPEN/CLOSED`.
