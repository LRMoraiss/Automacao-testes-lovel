#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SecurityScanController.py - Controller para lógica de scanning de segurança
Autor: Luciano Rodrigues de Morais
"""

import requests
import sys
from datetime import datetime
from typing import Dict, List
from urllib.parse import urlparse

from models.SecurityHeaderModel import SecurityScanResult, SecurityHeader, SecurityHeaderFactory
from repositories.SecurityConfigRepository import SecurityConfigRepository
from utils.ColorUtils import ColorUtils

class SecurityScanController:
    """Controller principal para execução de scans de segurança"""
    
    def __init__(self):
        self.config_repo = SecurityConfigRepository()
        self.colors = ColorUtils()
        self._disable_ssl_warnings()
    
    def _disable_ssl_warnings(self):
        """Desabilita avisos de SSL para testes"""
        try:
            requests.packages.urllib3.disable_warnings(
                requests.packages.urllib3.exceptions.InsecureRequestWarning
            )
        except AttributeError:
            pass
    
    def scan_url(self, url: str) -> SecurityScanResult:
        """
        Executa scan completo de segurança em uma URL
        
        Args:
            url: URL para fazer o scan
            
        Returns:
            SecurityScanResult: Resultado completo do scan
        """
        print(f"\n{self.colors.info}[*] Iniciando scan de segurança: {url}{self.colors.reset}\n")
        
        try:
            response = requests.get(url, timeout=10, verify=False)
            headers = {k.lower(): v for k, v in response.headers.items()}
            
            print(f"{self.colors.info}[+] Conexão bem-sucedida (Status: {response.status_code}){self.colors.reset}")
            
            # Analisar cabeçalhos de segurança
            security_headers = self._analyze_security_headers(headers)
            
            # Calcular score geral
            overall_score = self._calculate_security_score(security_headers)
            vulnerabilities = sum(1 for h in security_headers if not h.present)
            
            # Criar resultado
            result = SecurityScanResult(
                url=url,
                status_code=response.status_code,
                scan_timestamp=datetime.now(),
                headers_found=dict(response.headers),
                security_headers=security_headers,
                overall_score=overall_score,
                vulnerabilities_count=vulnerabilities
            )
            
            # Exibir resultados
            self._display_results(security_headers, overall_score)
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"{self.colors.error}[X] ERRO: Não foi possível conectar à URL. Detalhes: {e}{self.colors.reset}")
            raise
    
    def _analyze_security_headers(self, headers: Dict[str, str]) -> List[SecurityHeader]:
        """Analisa cabeçalhos de segurança encontrados"""
        security_headers = []
        
        # HSTS
        hsts_value = headers.get("strict-transport-security")
        hsts_header = SecurityHeaderFactory.create_hsts_header(hsts_value)
        security_headers.append(hsts_header)
        
        # X-Frame-Options
        xframe_value = headers.get("x-frame-options")
        xframe_header = SecurityHeaderFactory.create_xframe_header(xframe_value)
        security_headers.append(xframe_header)
        
        # X-Content-Type-Options
        xcontent_value = headers.get("x-content-type-options")
        xcontent_header = SecurityHeaderFactory.create_xcontent_header(xcontent_value)
        security_headers.append(xcontent_header)
        
        return security_headers
    
    def _calculate_security_score(self, headers: List[SecurityHeader]) -> int:
        """Calcula score de segurança baseado nos cabeçalhos"""
        total_score = 100
        
        for header in headers:
            if not header.present:
                if header.severity == "critical":
                    total_score -= 40
                elif header.severity == "high":
                    total_score -= 25
                elif header.severity == "medium":
                    total_score -= 15
        
        return max(0, total_score)
    
    def _display_results(self, headers: List[SecurityHeader], score: int):
        """Exibe resultados formatados no terminal"""
        print(f"\n{self.colors.header}=== RESULTADOS DO SCAN DE SEGURANÇA ==={self.colors.reset}\n")
        
        for header in headers:
            if header.present:
                print(f"{self.colors.success}[✓] BOM: {header.name} encontrado{self.colors.reset}")
                if header.value:
                    print(f"    Valor: {header.value}")
            else:
                print(f"{self.colors.error}[!] VULNERABILIDADE: {header.name} ausente{self.colors.reset}")
                print(f"    {header.description}")
                print(f"    Recomendação: {header.recommendation}")
        
        # Score final
        color = self.colors.success if score >= 80 else self.colors.warning if score >= 60 else self.colors.error
        print(f"\n{color}Score de Segurança: {score}/100{self.colors.reset}")
        
        if score < 80:
            print(f"{self.colors.warning}⚠ Atenção: Score baixo indica vulnerabilidades de segurança{self.colors.reset}")
    
    def scan_from_cli(self):
        """Executa scan a partir da linha de comando"""
        if len(sys.argv) != 2 or not sys.argv[1].startswith(('http://', 'https://')):
            self._show_usage()
            return
        
        self.colors.print_banner()
        target_url = sys.argv[1]
        
        try:
            result = self.scan_url(target_url)
            return result
        except Exception as e:
            print(f"{self.colors.error}Erro durante o scan: {e}{self.colors.reset}")
            sys.exit(1)
    
    def _show_usage(self):
        """Mostra instruções de uso"""
        self.colors.print_banner()
        print("\nUso incorreto.")
        print(f"  {self.colors.info}Uso: python scanner.py <URL_COMPLETA>{self.colors.reset}")
        print(f"  {self.colors.info}Exemplo: python scanner.py https://github.com{self.colors.reset}\n")