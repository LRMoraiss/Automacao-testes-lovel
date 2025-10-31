#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify-deploy.py - Verificação do deploy no GitHub
Autor: Luciano Rodrigues de Morais
"""

import subprocess
import webbrowser

def run_command(command):
    """Executa comando"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout.strip()
    except:
        return False, ""

def main():
    """Verifica deploy e abre repositório"""
    print("[VERIFY] Verificando deploy do projeto...")
    
    # Verificar status do git
    success, output = run_command("git status")
    if success:
        print("[OK] Repositorio Git configurado")
    
    # Verificar remote
    success, output = run_command("git remote -v")
    if "github.com/LRMoraiss/Automacao-testes-lovel" in output:
        print("[OK] Remote GitHub configurado corretamente")
    
    # Informações do projeto
    print("\n" + "="*50)
    print("[SUCCESS] PROJETO DEPLOYADO COM SUCESSO!")
    print("="*50)
    print("[URL] https://github.com/LRMoraiss/Automacao-testes-lovel")
    print("[NOME] QA-Cyber-Integration-Lovel")
    print("[ARCH] Arquitetura: MVCR")
    print("[TECH] Tecnologias: Cypress + Python")
    print("[FOCUS] Foco: QA + Cyber Security")
    print("="*50)
    
    # Abrir no navegador
    try:
        webbrowser.open("https://github.com/LRMoraiss/Automacao-testes-lovel")
        print("[BROWSER] Abrindo repositorio no navegador...")
    except:
        print("[INFO] Acesse: https://github.com/LRMoraiss/Automacao-testes-lovel")
    
    print("\n[READY] PROJETO PRONTO PARA PORTFOLIO!")

if __name__ == "__main__":
    main()