#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scanner.py - Script principal do Scanner de Segurança
Autor: Luciano Rodrigues de Morais
"""

import sys
import json
from controllers.SecurityScanController import SecurityScanController

def main():
    """Função principal do scanner"""
    controller = SecurityScanController()
    
    # Executar scan via CLI
    result = controller.scan_from_cli()
    
    if result:
        # Salvar resultado em JSON para integração
        output_file = f"scan_result_{result.scan_timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result.to_dict(), f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Relatório salvo em: {output_file}")

if __name__ == "__main__":
    main()