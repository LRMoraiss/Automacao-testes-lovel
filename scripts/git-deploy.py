#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
git-deploy.py - Script para deploy automático no GitHub
Autor: Luciano Rodrigues de Morais
"""

import subprocess
import sys
import os

def run_command(command):
    """Executa comando e retorna resultado"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[ERROR] {result.stderr}")
            return False
        print(f"[OK] {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

def main():
    """Deploy automático para GitHub"""
    print("[DEPLOY] Iniciando deploy automatico para GitHub...")
    
    # Verificar se está em um repositório git
    if not os.path.exists('.git'):
        print("[GIT] Inicializando repositorio Git...")
        if not run_command("git init"):
            return
    
    # Adicionar remote se não existir
    print("[REMOTE] Configurando remote...")
    run_command("git remote remove origin")  # Remove se existir
    if not run_command("git remote add origin https://github.com/LRMoraiss/Automacao-testes-lovel.git"):
        return
    
    # Configurar usuário (opcional)
    run_command("git config user.name 'Luciano Rodrigues de Morais'")
    run_command("git config user.email 'luciano.morais@example.com'")
    
    # Adicionar todos os arquivos
    print("[ADD] Adicionando arquivos...")
    if not run_command("git add ."):
        return
    
    # Commit
    commit_message = "feat: projeto integrado QA + Cyber Security com arquitetura MVCR"
    print("[COMMIT] Fazendo commit...")
    if not run_command(f'git commit -m "{commit_message}"'):
        return
    
    # Push para GitHub
    print("[PUSH] Enviando para GitHub...")
    if not run_command("git push -u origin main"):
        # Tentar master se main falhar
        run_command("git branch -M main")
        if not run_command("git push -u origin main"):
            return
    
    print("\n[SUCCESS] Deploy concluido com sucesso!")
    print("[URL] Repositorio: https://github.com/LRMoraiss/Automacao-testes-lovel")

if __name__ == "__main__":
    main()