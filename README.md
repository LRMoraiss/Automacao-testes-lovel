# QA-Cyber-Integration-Lovel

[![Quality Assurance](https://img.shields.io/badge/QA-Cypress-green)](https://cypress.io/)
[![Security](https://img.shields.io/badge/Security-Scanner-red)](https://owasp.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🎯 Propósito

Projeto integrado de **Quality Assurance** e **Cyber Security** que demonstra habilidades em automação de testes E2E e análise de segurança web. Desenvolvido para validar funcionalidades da plataforma Lovel enquanto verifica cabeçalhos de segurança HTTP.

## 🏗️ Arquitetura MVCR (Model-View-Controller-Repository)

```
qa-cyber-integration-lovel/
├── qa-tests/                 # Módulo de Automação QA
│   ├── models/              # Models - Estruturas de dados
│   ├── views/               # Views - Page Objects
│   ├── controllers/         # Controllers - Lógica de testes
│   └── repositories/        # Repositories - Dados de teste
├── cyber-scanner/           # Módulo de Security Scanner
│   ├── models/              # Models - Estruturas de segurança
│   ├── controllers/         # Controllers - Lógica de scanning
│   └── repositories/        # Repositories - Configurações
├── docs/                    # Documentação
└── reports/                 # Relatórios de execução
```

## 🚀 Tecnologias

- **QA Testing**: Cypress (JavaScript)
- **Security Scanner**: Python 3.x + Requests
- **Integração**: Node.js scripts
- **Documentação**: Markdown

## ⚡ Execução Rápida

```bash
# Clone o repositório
git clone https://github.com/LRMoraiss/QA-Cyber-Integration-Lovel.git
cd QA-Cyber-Integration-Lovel

# Instalar dependências
npm install
pip install -r requirements.txt

# Executar testes integrados
npm run test:integrated
```

## 📋 Funcionalidades

### 🔍 QA Tests
- ✅ Busca de vagas com resultados
- ✅ Busca sem resultados (edge case)
- ✅ Validação de cabeçalhos de segurança via Cypress

### 🛡️ Security Scanner
- ✅ Análise de cabeçalhos HSTS
- ✅ Verificação X-Frame-Options
- ✅ Validação X-Content-Type-Options
- ✅ Relatório colorido no terminal

### 🔗 Integração Híbrida
- ✅ Testes QA que chamam scanner de segurança
- ✅ Relatórios unificados
- ✅ Pipeline de validação completa

## 📖 Documentação Detalhada

- [📋 QA Tests Documentation](./qa-tests/README.md)
- [🛡️ Cyber Scanner Documentation](./cyber-scanner/README.md)
- [🔧 Setup Guide](./docs/SETUP.md)
- [📊 Reports Guide](./docs/REPORTS.md)

## 🏃‍♂️ Como Executar

### Pré-requisitos
- Node.js 16+
- Python 3.8+
- Chrome/Chromium browser

### Instalação
```bash
npm install
pip install -r requirements.txt
```

### Execução Individual
```bash
# Apenas testes QA
npm run test:qa

# Apenas scanner de segurança
npm run scan:security

# Integração completa
npm run test:integrated
```

## 📊 Provas de Execução

### QA Tests Results
![QA Tests](./docs/screenshots/qa-tests-results.png)

### Security Scanner Results
![Security Scanner](./docs/screenshots/security-scan-results.png)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Luciano Rodrigues de Morais**
- LinkedIn: [linkedin.com/in/luciano-morais](https://linkedin.com/in/luciano-morais)
- GitHub: [@LRMoraiss](https://github.com/LRMoraiss)

---
⭐ **Fixe este repositório se foi útil para você!**