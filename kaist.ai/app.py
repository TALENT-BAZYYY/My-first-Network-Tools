import os
import re
import json
import socket
import sys
from datetime import datetime
import numpy as np
import ollama
import easyocr
from pypdf import PdfReader
from rank_bm25 import BM25Okapi
from duckduckgo_search import DDGS

CACHE_FILE = "db_cache.txt"
EVOLVED_MEMORY_FILE = "evolved_memory.json"
DOCS_DIR = "./docs"

context = ""

print("--- System Initialization: Knowledge Base & RAG System ---")

# 1. Загрузка локальных знаний
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f: 
        context = f.read()
else:
    print("Log: Cache file not found. Initializing document parsing...")
    reader_ocr = easyocr.Reader(['ru', 'en'], gpu=True)
    if os.path.exists(DOCS_DIR):
        for filename in os.listdir(DOCS_DIR):
            file_path = os.path.join(DOCS_DIR, filename)
            if filename.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f: 
                    context += f.read() + "\n"
            elif filename.endswith(".pdf"):
                try:
                    pdf = PdfReader(file_path)
                    for page in pdf.pages:
                        text = page.extract_text()
                        if not text or len(text.strip()) < 10:
                            for img_info in page.images:
                                ocr_result = reader_ocr.readtext(img_info.data, detail=0)
                                if ocr_result: 
                                    context += " ".join(ocr_result) + "\n"
                        else: 
                            context += text + "\n"
                except Exception as e: 
                    print(f"Error processing PDF {filename}: {e}")
                    
    if context.strip():
        with open(CACHE_FILE, "w", encoding="utf-8") as f: 
            f.write(context)

if os.path.exists(EVOLVED_MEMORY_FILE):
    with open(EVOLVED_MEMORY_FILE, "r", encoding="utf-8") as f:
        for insight in json.load(f): 
            context += f"\n[Memory]: {insight}\n"

paragraphs = [p.strip() for p in re.split(r'\n{2,}|\. \n|\n(?=[A-ZА-Я])', context) if len(p.strip()) > 30]
bm25 = BM25Okapi([p.lower().split(" ") for p in paragraphs])


def search_internet_force(search_query):
    try:
        print(f"Log: Initializing web search query: '{search_query}'")
        
        if "требован" in search_query or "kaist" in search_query:
            search_query = "KAIST international students admission requirements 2026 2027"
            print(f"Log: Query optimization applied: '{search_query}'")

        ddgs = DDGS()
        results = ddgs.text(search_query, region="wt-wt", safesearch="off", timelimit="y")
        
        web_text = ""
        count = 0
        if results:
            print("Log: Web search data retrieved successfully.")
            for res in results:
                count += 1
                print(f"   -> Result [{count}]: {res['title']}")
                web_text += f"\nSource: {res['title']} ({res['href']})\nContent: {res['body']}\n"
                if count >= 3: 
                    break
            return web_text
        
        print("Warning: Secondary search query executed due to empty response.")
        results_backup = ddgs.text("KAIST undergraduate admission guide pdf", max_results=2)
        for res in results_backup:
            web_text += f"\nSource: {res['title']} ({res['href']})\nContent: {res['body']}\n"
        return web_text
    except Exception as e:
        return f"Network module error: {e}"


print(f"Log: System ready ({len(paragraphs)} chunks parsed). System loop initialized.")
print("Type 'exit' to terminate the session.")

chat_history = []

while True:
    query = input("\nUser: ")
    if query.lower() in ['выход', 'exit']: 
        break
    if not query.strip(): 
        continue
    
    need_internet = any(word in query.lower() for word in ["интернет", "сайт", "найди", "гугл", "новости", "узнай", "сеть"])
    
    web_context = ""
    if need_internet:
        web_context = search_internet_force(query.lower())

    tokenized_query = query.lower().split(" ")
    top_fragments = bm25.get_top_n(tokenized_query, paragraphs, n=3)
    local_context = "\n\n".join(top_fragments)
    
    system_instruction = f"""Ты — ИИ-ассистент KAIST RIRO Lab. Твой руководитель — профессор Дэхен Пак. 
Твой создатель — Исламбек (17 лет, Кыргызстан). Ты обязан отвечать строго на РУССКОМ ЯЗЫКЕ.

Ниже приведены данные, извлеченные из сети Интернет по текущему запросу пользователя. Проанализируй этот текст, структурируй информацию и выдай пользователю четкие факты и требования.

ДАННЫЕ ИЗ СЕТИ ИНТЕРНЕТ:
{web_context if web_context else "Используются только локальные файлы."}

ДАННЫЕ ЛОКАЛЬНЫХ ФАЙЛОВ:
{local_context}"""

    messages = [{"role": "system", "content": system_instruction}] + chat_history + [{"role": "user", "content": query}]
    
    try:
        response = ollama.chat(
            model="gemma2:9b", 
            messages=messages,
            options={"num_ctx": 8192, "temperature": 0.2, "num_predict": 500, "repeat_penalty": 1.4}
        )
        reply = response['message']['content']
        print(f"\nAssistant:\n{reply}")
        
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": reply})
        if len(chat_history) > 4: 
            chat_history = chat_history[-4:]
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
