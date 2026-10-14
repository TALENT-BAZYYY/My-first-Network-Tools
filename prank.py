import ctypes
import os
import platform
import random
import sys
import threading
import time
from colorama import Fore, Style, init
import psutil
import pygame
import pyautogui
import pyperclip

init(convert=True)


class DoomsdayEngine:

    def __init__(self):
        self.running = True
        self.screen_w = 0
        self.screen_h = 0
        self.log_lines = []
        self.hex_chars = [
            "0",
            "1",
            "X",
            "@",
            "%",
            "&",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "!",
            "$",
            "?",
        ]

    @staticmethod
    def trigger_system_alert(text, title):
        ctypes.windll.user32.MessageBoxW(0, text, title, 0x10)

    def spawn_cascading_alerts(self, count):
        for i in range(count):
            if not self.running and i > 15:
                break
                
            wave = i % 4
            offset_x = 30 + wave * 120 + (i * 12) % (self.screen_w - 400)
            offset_y = 30 + wave * 90 + (i * 10) % (self.screen_h - 200)
            
            alert_text = f"NUCLEAR_KERNEL_CORE_MELTDOWN: Memory leak at block 0x{random.randint(0x100000, 0xFFFFFF):X}"
            alert_title = f"CRITICAL SYSTEM DESTRICTION LOG #{i+1:03d}"
            
            t = threading.Thread(
                target=ctypes.windll.user32.MessageBoxW, 
                args=(0, alert_text, alert_title, 0x10)
            )
            t.daemon = True
            t.start()
            time.sleep(0.015)

    @staticmethod
    def dispatch_vocal_payload(phrase):
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak(phrase)
        except:
            pass

    def run_infinite_console_storm(self):
        start_time = time.time()
        while time.time() - start_time < 8.0:
            addr1 = f"0x{random.randint(0x10000000, 0x7FFFFFFF):08X}"
            addr2 = f"0x{random.randint(0x80000000, 0xFFFFFFFF):08X}"
            raw_bytes = " ".join(f"{random.randint(0, 255):02X}" for _ in range(16))
            binary = "".join(random.choice(["0", "1", "X", " "]) for _ in range(32))
            
            color = random.choice([Fore.RED, Fore.YELLOW, Fore.WHITE])
            print(color + Style.BRIGHT + f"[CRIT_DUMP] | {addr1} -> {addr2} | MEM_MATRIX: {raw_bytes} | STREAM: {binary}")
            time.sleep(0.0005)

    def render_matrix_overlay(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_w, self.screen_h = info.current_w, info.current_h
        surface = pygame.display.set_mode(
            (self.screen_w, self.screen_h), pygame.FULLSCREEN | pygame.NOFRAME
        )

        black = (0, 0, 0)
        matrix_green = (0, 255, 70)
        alert_red = (255, 10, 10)
        telemetry_cyan = (0, 230, 255)

        try:
            font = pygame.font.SysFont("courier", 22, bold=True)
        except:
            font = pygame.font.Font(None, 24)

        cols = self.screen_w // 20
        matrix_columns = [random.randint(-50, 0) for _ in range(cols)]
        start_time = time.time()
        clock = pygame.time.Clock()

        while self.running:
            if time.time() - start_time > 12.0:
                self.running = False

            fade_surface = pygame.Surface((self.screen_w, self.screen_h))
            fade_surface.set_alpha(25)
            fade_surface.fill(black)
            surface.blit(fade_surface, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            if random.random() > 0.95:
                pygame.draw.line(
                    surface,
                    alert_red,
                    (0, random.randint(0, self.screen_h)),
                    (self.screen_w, random.randint(0, self.screen_h)),
                    3,
                )

            for i in range(len(matrix_columns)):
                if matrix_columns[i] >= 0:
                    char = random.choice(self.hex_chars)
                    char_color = (255, 255, 255) if random.random() > 0.98 else matrix_green
                    char_text = font.render(char, True, char_color)
                    surface.blit(char_text, (i * 20, matrix_columns[i] * 20))

                if matrix_columns[i] * 20 > self.screen_h or (matrix_columns[i] >= 0 and random.random() > 0.975):
                    matrix_columns[i] = random.randint(-10, 0)
                else:
                    matrix_columns[i] += 1

            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            surface.blit(font.render(f"[CPU_COMPROMISED]: {cpu}% OVERLOAD", True, telemetry_cyan), (self.screen_w - 480, 40))
            surface.blit(font.render(f"[RAM_MEM_DESTROY]: {ram}% CORRUPTED", True, telemetry_cyan), (self.screen_w - 480, 75))

            progress_w = int((time.time() - start_time) / 12.0 * 300)
            pygame.draw.rect(surface, alert_red, (self.screen_w - 480, 120, 300, 15), 2)
            pygame.draw.rect(surface, matrix_green, (self.screen_w - 478, 122, max(0, progress_w - 4), 11))

            if random.random() > 0.25:
                addr = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
                vector = random.choice([
                    "OVERRIDING_HARDWARE_KERNEL_BUS",
                    "FLOODING_LOCAL_BUFFER_SOCKETS",
                    "REREUTING_SYSTEM_DATA_PACKETS",
                    "EXTRACTING_CRYPTOGRAPHIC_PAYLOAD",
                    "FORCING_DISTRIBUTED_CPU_MELTDOWN"
                ])
                self.log_lines.append(f"[{addr}] -> SYSTEM_DESTROY: {vector}")

            if len(self.log_lines) * 28 > self.screen_h - 160:
                self.log_lines.pop(0)

            for idx, line in enumerate(self.log_lines):
                surface.blit(font.render(line, True, alert_red), (50, 60 + idx * 28))

            surface.blit(
                font.render("⚠️ EMERGENCY WARNING: NUCLEAR FALLOUT INITIALIZED // PRESS ESC TO ABORT ⚠️", True, alert_red),
                (self.screen_w // 2 - 450, self.screen_h - 60)
            )

            pygame.display.flip()
            clock.tick(45)

        pygame.quit()

    def run_clipboard_flood(self, count):
        for i in range(count):
            hex_junk = "".join(random.choice(["A", "F", "0", "9", "X", "!"]) for _ in range(8))
            payload = f"[NUCLEAR_SYS_OVERFLOW_{hex_junk}] // TERMINATION_LAYER_{i+1:03d} // EXPORT_COMPLETE"
            pyperclip.copy(payload)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(random.uniform(0.01, 0.05))

    def initialize_orchestrator(self):
        print(Fore.RED + Style.BRIGHT + "=== [NUCLEAR FALLOUT DOOMSDAY ORCHESTRATOR v7.0] ===")
        print("ALERT: Unlocking quantum synchronization layers...")
        time.sleep(1)

        self.trigger_system_alert("CRITICAL CORRUPTION: ACCESS_VIOLATION_0x000F", "SYSTEM KERNEL")
        self.trigger_system_alert("NETWORK LOGS EXPORTED TO OUTSIDE TERMINAL", "SECURITY AUDIT")

        for i in range(5, 0, -1):
            print(Fore.YELLOW + f"  [!] CRITICAL QUANTUM OVERLOAD IN: {i}...")
            time.sleep(1)

        print(Fore.RED + Style.BRIGHT + f"\n[!!!] DEPLOYING ALL MULTI-THREADED ATTACK THREADS...\n")
        time.sleep(0.5)

        phrase_data = "Warning. Tactical emergency override activated. 300 fatal system dump windows launched. Total network blackout is imminent."
        voice_thread = threading.Thread(target=self.dispatch_vocal_payload, args=(phrase_data,))
        voice_thread.start()

        self.render_matrix_overlay()

        print(Fore.RED + Style.BRIGHT + "\n[🔥] WARNING: LAUNCHING THE 300 WINDOWS CASCADING HURRICANE...\n")
        
        # Запуск ядерного каскада из 300 окон ошибок
        self.spawn_cascading_alerts(300)
        time.sleep(4)

        print(Fore.YELLOW + Style.BRIGHT + "\n[☠️] ENGAGING UNSTOPPABLE CONSOLE MATRIX STORM...\n")
        time.sleep(0.5)
        
        # Бесконечный Матричный Шторм кодов прямо в терминал
        self.run_infinite_console_storm()

        print(Fore.YELLOW + Style.BRIGHT + "\n[!] EXECUTING FAST SPEED TELEMETRY FLODDING...\n")
        time.sleep(0.5)

        self.run_clipboard_flood(70)

        print(Fore.GREEN + Style.BRIGHT + "\n=== SYSTEM PURGE EXECUTED: ALL TARGETS NEUTRALIZED ===")
        print(Fore.GREEN + f"Handshake link destroyed. Core security status: COMPROMISED.\n" + Style.RESET_ALL)


if __name__ == "__main__":
    orchestrator = DoomsdayEngine()
    orchestrator.initialize_orchestrator()
