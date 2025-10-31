# 🛡️ Cyber Scanner - Análise de Segurança Web

## 📋 Visão Geral

Scanner de segurança web desenvolvido em **Python** seguindo arquitetura **MVCR**. Analisa cabeçalhos HTTP de segurança e identifica vulnerabilidades baseadas nas diretrizes **OWASP**.

## 🏗️ Arquitetura MVCR

### 📊 Models (`/models`)
- **SecurityHeaderModel.py**: Estruturas de dados para cabeçalhos
- **SecurityScanResult**: Resultado completo do scan
- **SecurityHeaderFactory**: Factory para criação de objetos

### 🎮 Controllers (`/controllers`)
- **SecurityScanController.py**: Lógica principal de scanning
- Orquestra análise e exibição de resultados

### 🗄️ Repositories (`/repositories`)
- **SecurityConfigRepository.py**: Configurações de segurança
- Dados de cabeçalhos, severidades e categorias

### 🛠️ Utils (`/utils`)
- **ColorUtils.py**: Formatação colorida para terminal
- Banner e mensagens formatadas

## 🔍 Cabeçalhos Analisados

### 🚨 Críticos
- **Strict-Transport-Security (HSTS)**
  - Previne SSL stripping
  - Força conexões HTTPS

- **X-Frame-Options**
  - Previne clickjacking
  - Controla embedding em frames

- **X-Content-Type-Options**
  - Previne MIME sniffing
  - Valor esperado: `nosniff`

## 🎯 Sistema de Scoring

```python
Score Base: 100 pontos

Penalizações:
- Critical ausente: -40 pontos
- High ausente: -25 pontos  
- Medium ausente: -15 pontos

Classificação:
- 80-100: Excelente 🟢
- 60-79: Bom 🟡
- 0-59: Crítico 🔴
```

## 🚀 Execução

### Instalação
```bash
pip install -r requirements.txt
```

### Uso Básico
```bash
python scanner.py https://app.lovel.dev/jobs
```

### Uso Programático
```python
from controllers.SecurityScanController import SecurityScanController

controller = SecurityScanController()
result = controller.scan_url('https://example.com')
print(f"Score: {result.overall_score}/100")
```

## 📊 Saída do Scanner

### Terminal Colorido
```
============================================
    QA-Cyber Security Scanner v2.0
    Análise Integrada de Segurança Web
============================================

[*] Iniciando scan de segurança: https://app.lovel.dev/jobs

[+] Conexão bem-sucedida (Status: 200)

=== RESULTADOS DO SCAN DE SEGURANÇA ===

[✓] BOM: Strict-Transport-Security encontrado
    Valor: max-age=31536000; includeSubDomains

[!] VULNERABILIDADE: X-Frame-Options ausente
    Previne ataques de clickjacking
    Recomendação: Adicionar: X-Frame-Options: DENY ou SAMEORIGIN

Score de Segurança: 75/100
```

### Relatório JSON
```json
{
  "url": "https://app.lovel.dev/jobs",
  "status_code": 200,
  "scan_timestamp": "2024-01-15T10:30:00",
  "overall_score": 75,
  "vulnerabilities_count": 1,
  "security_headers": [
    {
      "name": "Strict-Transport-Security",
      "present": true,
      "severity": "info",
      "value": "max-age=31536000"
    }
  ]
}
```

## 🔧 Configurações

### Cabeçalhos Suportados
```python
CRITICAL_HEADERS = [
    "strict-transport-security",
    "x-frame-options", 
    "x-content-type-options"
]

RECOMMENDED_HEADERS = [
    "content-security-policy",
    "x-xss-protection",
    "referrer-policy"
]
```

### Personalização
```python
# Adicionar novos cabeçalhos
SecurityConfigRepository.get_critical_headers()

# Modificar scoring
SecurityConfigRepository.get_severity_levels()
```

## 🔗 Integração com QA

### Via Cypress Task
```javascript
cy.task('runSecurityScan', url).then((result) => {
  cy.log('Security Results:', result);
});
```

### Via Node.js
```javascript
const { spawn } = require('child_process');
const scanner = spawn('python', ['cyber-scanner/scanner.py', url]);
```

## 📈 Casos de Uso

### 1. Validação Contínua
```bash
# Integrar no CI/CD
python scanner.py $TARGET_URL
```

### 2. Auditoria de Segurança
```bash
# Scan múltiplas URLs
for url in urls.txt; do
  python scanner.py $url >> audit_report.txt
done
```

### 3. Monitoramento
```bash
# Cron job diário
0 9 * * * /usr/bin/python /path/scanner.py https://app.lovel.dev
```

## 🎯 Roadmap

- [ ] Suporte a mais cabeçalhos (CSP, HPKP)
- [ ] Análise de certificados SSL
- [ ] Integração com APIs de threat intelligence
- [ ] Dashboard web para resultados
- [ ] Alertas automáticos

---
**Desenvolvido por**: Luciano Rodrigues de Morais  
**Tecnologia**: Python 3.8+  
**Padrão**: OWASP Security Guidelines