#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SecurityHeaderModel.py - Model para estrutura de dados de cabeçalhos de segurança
Autor: Luciano Rodrigues de Morais
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class SecurityHeader:
    """Modelo para um cabeçalho de segurança individual"""
    name: str
    value: Optional[str]
    present: bool
    severity: str  # 'critical', 'high', 'medium', 'low', 'info'
    description: str
    recommendation: str

@dataclass
class SecurityScanResult:
    """Modelo para resultado completo do scan de segurança"""
    url: str
    status_code: int
    scan_timestamp: datetime
    headers_found: Dict[str, str]
    security_headers: List[SecurityHeader]
    overall_score: int
    vulnerabilities_count: int

    def to_dict(self) -> Dict:
        """Converte o resultado para dicionário"""
        return {
            'url': self.url,
            'status_code': self.status_code,
            'scan_timestamp': self.scan_timestamp.isoformat(),
            'headers_found': self.headers_found,
            'security_headers': [
                {
                    'name': header.name,
                    'value': header.value,
                    'present': header.present,
                    'severity': header.severity,
                    'description': header.description,
                    'recommendation': header.recommendation
                }
                for header in self.security_headers
            ],
            'overall_score': self.overall_score,
            'vulnerabilities_count': self.vulnerabilities_count
        }

class SecurityHeaderFactory:
    """Factory para criar objetos SecurityHeader"""
    
    @staticmethod
    def create_hsts_header(value: Optional[str] = None) -> SecurityHeader:
        return SecurityHeader(
            name="Strict-Transport-Security",
            value=value,
            present=value is not None,
            severity="critical" if value is None else "info",
            description="Força conexões HTTPS e previne ataques SSL stripping",
            recommendation="Adicionar: Strict-Transport-Security: max-age=31536000; includeSubDomains"
        )
    
    @staticmethod
    def create_xframe_header(value: Optional[str] = None) -> SecurityHeader:
        return SecurityHeader(
            name="X-Frame-Options",
            value=value,
            present=value is not None,
            severity="high" if value is None else "info",
            description="Previne ataques de clickjacking",
            recommendation="Adicionar: X-Frame-Options: DENY ou SAMEORIGIN"
        )
    
    @staticmethod
    def create_xcontent_header(value: Optional[str] = None) -> SecurityHeader:
        return SecurityHeader(
            name="X-Content-Type-Options",
            value=value,
            present=value is not None and value.lower() == "nosniff",
            severity="medium" if value != "nosniff" else "info",
            description="Previne MIME type sniffing",
            recommendation="Adicionar: X-Content-Type-Options: nosniff"
        )