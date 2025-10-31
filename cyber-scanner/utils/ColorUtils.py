#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ColorUtils.py - Utilitário para cores no terminal
Autor: Luciano Rodrigues de Morais
"""

class ColorUtils:
    """Utilitário para formatação colorida no terminal"""
    
    def __init__(self):
        self.header = "\033[95m"
        self.success = "\033[92m"
        self.warning = "\033[93m"
        self.error = "\033[91m"
        self.info = "\033[94m"
        self.bold = "\033[1m"
        self.underline = "\033[4m"
        self.reset = "\033[0m"
    
    def print_banner(self):
        """Exibe banner inicial colorido"""
        print(f"{self.header}{'='*50}{self.reset}")
        print(f"{self.header}{self.bold}    QA-Cyber Security Scanner v2.0{self.reset}")
        print(f"{self.header}    Análise Integrada de Segurança Web{self.reset}")
        print(f"{self.header}{'='*50}{self.reset}")
    
    def format_success(self, message: str) -> str:
        """Formata mensagem de sucesso"""
        return f"{self.success}[✓] {message}{self.reset}"
    
    def format_error(self, message: str) -> str:
        """Formata mensagem de erro"""
        return f"{self.error}[✗] {message}{self.reset}"
    
    def format_warning(self, message: str) -> str:
        """Formata mensagem de aviso"""
        return f"{self.warning}[⚠] {message}{self.reset}"
    
    def format_info(self, message: str) -> str:
        """Formata mensagem informativa"""
        return f"{self.info}[ℹ] {message}{self.reset}"
    
    def format_header(self, message: str) -> str:
        """Formata cabeçalho"""
        return f"{self.header}{self.bold}{message}{self.reset}"