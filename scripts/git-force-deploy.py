#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
git-force-deploy.py - Script para force push no GitHub
Autor: Luciano Rodrigues de Morais
"""

import subprocess
import sys

def run_command(command):
    """Executa comando"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"[CMD] {command}")
        if result.stdout:
            print(f"[OUT] {result.stdout.strip()}")
        if result.stderr:
            print(f"[ERR] {result.stderr.strip()}")
        return result.returncode == 0
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

def main():
    """Force deploy para GitHub"""
    print("[DEPLOY] Iniciando force deploy...")
    
    # Configurar branch main
    run_command("git branch -M main")
    
    # Force push
    print("[PUSH] Fazendo force push...")
    if run_command("git push -f origin main"):
        print("\n[SUCCESS] Deploy realizado com sucesso!")
        print("[URL] https://github.com/LRMoraiss/Automacao-testes-lovel")
    else:
        print("\n[MANUAL] Execute manualmente:")
        print("git branch -M main")
        print("git push -f origin main")

if __name__ == "__main__":
    main()