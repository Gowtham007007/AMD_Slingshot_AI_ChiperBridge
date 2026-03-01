# 🛡️ AI CipherBridge: Secure Intranet Communication 🌉

**AI CipherBridge** is a privacy-first, decentralized security gateway designed to eliminate the "blind spots" in university intranets. It retrofits legacy lab equipment with **Triple-Lock Encryption** and **On-Premise AI Anomaly Detection** to protect sensitive research data.

## 🚀 The Problem

Traditional university networks focus on perimeter firewalls but leave **internal traffic** (Intranet) unmonitored.

- ⚠️ **Vulnerability:** Legacy lab devices send data in plain text.
- ⚠️ **Risk:** Internal threats can move laterally across the campus.
- ⚠️ **Privacy:** Cloud-based AI exposes sensitive student PII (Personally Identifiable Information).

## ✨ Key Features

- **🔒 Triple-Lock Security:** AES-256 payload encryption + HTTPS routing + Token-based Auth.
- **🧠 Dual AI Engine:** Localized **Isolation Forest** (Scikit-Learn) for anomaly detection and **Llama-3** for explainable security alerts.
- **📦 Isolated Smart Routing:** NGINX-powered containerized message flow to prevent lateral movement.
- **🔌 Retrofit Ready:** Low-cost ESP32 integration for existing university lab hardware.
- **💻 AMD Optimized:** Engineered for **AMD Ryzen™ AI** edge nodes and **AMD EPYC™** core infrastructure.

## 🛠️ System Architecture

The system operates in three distinct layers:

1. **The Edge Node (ESP32):** Collects data from lab equipment and encrypts the payload.
2. **The CipherBridge (Raspberry Pi/AMD Edge):** Acts as the secure gateway, decrypting and inspecting traffic using AI.
3. **The AI Command Center (AMD Ryzen Laptop):** Provides a dashboard for real-time threat monitoring and GenAI-driven reports.

## 🏗️ Tech Stack

- **Hardware:** Raspberry Pi 4 (Edge Gateway), ESP32 (Sensor Node), AMD Ryzen™ 7 (AI Inference).
- **Firmware:** Arduino C++ (ESP32), MicroPython.
- **Backend:** Python (Flask/FastAPI), NGINX (Reverse Proxy).
- **AI/ML:** Scikit-Learn (Isolation Forest), PyTorch (Autoencoders), Ollama (Local Llama-3).
- **DevOps:** Docker, Ubuntu 22.04 LTS.

## 📂 Repository Structure

Bash

`├── firmware/              # ESP32 C++/Arduino code for encryption
├── gateway/               # NGINX configs & Docker Compose files
├── ai-engine/             # Scikit-Learn & PyTorch models
├── backend-api/           # Flask API for secure data handling
├── dashboard/             # React/Streamlit UI for threat alerts
└── docs/                  # Project PPT and Architecture diagrams`

## 🛠️ Setup Instructions (Phase 1)

To get your own CipherBridge node running on a Raspberry Pi:

1. **Flash OS:** Use Raspberry Pi OS Legacy (64-bit) Lite.
2. **Configure SSH:** `touch ssh` in the boot partition.
3. **Connect to Intranet:**Bash
    
    `ssh admin@lab-gateway.local`
    
4. **Deploy Bridge:**Bash
    
    `sudo apt update && sudo apt install nginx docker.io -y`
    

## 🌟 Vision

Our goal is to provide a **cost-effective, cloud-independent** security layer for global educational institutions, ensuring that the next generation of research stays within the campus walls.

---

**Built by Team INVICTUS for AMD Slingshot 2026** 🚀
