## 🛡️ FEATURED PROJECT: Aegis-Net (Autonomous AI-Driven IPS/IDS)
A high-performance Automated Intrusion Detection and Prevention System designed as a prototype for advanced network protection architectures. Evaluated as a core project for the KAIST RIRO Lab application.

* **Concept:** Synergizing low-level system statistics monitoring with Local Large Language Models (LLM) orchestration.
* **Core Logic:** The script continuously audits system sockets via `psutil`. Upon detecting anomalous socket multiplexing or potential connection flooding (e.g., DDoS vectors), the telemetry is instantly dispatched to the **Gemma 2 (9B)** neural core running via **Ollama**.
* **Autonomous Mitigation:** The AI engine acts as a cyber-analyst: evaluates threat severity, establishes mitigation frameworks, and outputs targeted low-level Netfilter commands (`iptables`) for real-time kernel-level packet dropping.

---
