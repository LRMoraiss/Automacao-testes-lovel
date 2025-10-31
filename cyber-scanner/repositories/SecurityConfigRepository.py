#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SecurityConfigRepository.py - Repository para configurações de segurança
Autor: Luciano Rodrigues de Morais
"""

from typing import Dict, List

class SecurityConfigRepository:
    """Repository para configurações e dados de segurança"""
    
    @staticmethod
    def get_critical_headers() -> List[str]:
        """Retorna lista de cabeçalhos críticos de segurança"""
        return [
            "strict-transport-security",
            "x-frame-options",
            "x-content-type-options"
        ]
    
    @staticmethod
    def get_recommended_headers() -> List[str]:
        """Retorna lista de cabeçalhos recomendados"""
        return [
            "content-security-policy",
            "x-xss-protection",
            "referrer-policy",
            "permissions-policy"
        ]
    
    @staticmethod
    def get_header_descriptions() -> Dict[str, str]:
        """Retorna descrições dos cabeçalhos de segurança"""
        return {
            "strict-transport-security": "Força uso de HTTPS e previne SSL stripping",
            "x-frame-options": "Previne ataques de clickjacking",
            "x-content-type-options": "Previne MIME type sniffing",
            "content-security-policy": "Define política de segurança de conteúdo",
            "x-xss-protection": "Ativa proteção XSS do navegador",
            "referrer-policy": "Controla informações de referrer enviadas"
        }
    
    @staticmethod
    def get_severity_levels() -> Dict[str, int]:
        """Retorna níveis de severidade para scoring"""
        return {
            "critical": 40,
            "high": 25,
            "medium": 15,
            "low": 10,
            "info": 0
        }
    
    @staticmethod
    def get_test_urls() -> List[str]:
        """Retorna URLs para testes"""
        return [
            "https://app.lovel.dev/jobs",
            "https://github.com",
            "https://google.com",
            "https://stackoverflow.com"
        ]
    
    @staticmethod
    def get_vulnerability_categories() -> Dict[str, List[str]]:
        """Retorna categorias de vulnerabilidades"""
        return {
            "transport_security": ["strict-transport-security"],
            "clickjacking": ["x-frame-options"],
            "content_sniffing": ["x-content-type-options"],
            "xss_protection": ["x-xss-protection", "content-security-policy"],
            "information_disclosure": ["referrer-policy", "server"]
        }