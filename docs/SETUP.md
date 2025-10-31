# 🚀 Guia de Instalação - QA-Cyber-Integration-Lovel

## 📋 Pré-requisitos

### Sistema Operacional
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux Ubuntu 18.04+

### Software Necessário
- **Node.js** 16.0+ ([Download](https://nodejs.org/))
- **Python** 3.8+ ([Download](https://python.org/))
- **Git** ([Download](https://git-scm.com/))
- **Chrome/Chromium** (para Cypress)

## 🔧 Instalação Passo a Passo

### 1. Clone o Repositório
```bash
git clone https://github.com/LRMoraiss/QA-Cyber-Integration-Lovel.git
cd QA-Cyber-Integration-Lovel
```

### 2. Instalar Dependências Node.js
```bash
npm install
```

### 3. Instalar Dependências Python
```bash
# Windows
pip install -r requirements.txt

# macOS/Linux
pip3 install -r requirements.txt
```

### 4. Verificar Instalação
```bash
# Verificar Node.js
node --version

# Verificar Python
python --version

# Verificar Cypress
npx cypress --version
```

## ⚡ Execução Rápida

### Setup Automático
```bash
npm run setup
```

### Testes QA
```bash
# Modo interativo
npm run test:qa:open

# Modo headless
npm run test:qa
```

### Scanner de Segurança
```bash
npm run scan:security
```

### Pipeline Integrado
```bash
npm run test:integrated
```

## 🔧 Configurações Avançadas

### Variáveis de Ambiente
Crie arquivo `.env` na raiz:
```env
# URLs de teste
BASE_URL=https://app.lovel.dev
STAGING_URL=https://staging.lovel.dev

# Configurações Cypress
CYPRESS_TIMEOUT=10000
CYPRESS_VIEWPORT_WIDTH=1280
CYPRESS_VIEWPORT_HEIGHT=720

# Scanner de Segurança
SECURITY_TIMEOUT=30
REPORT_FORMAT=json
```

### Cypress Personalizado
Edite `cypress.config.js`:
```javascript
module.exports = defineConfig({
  e2e: {
    baseUrl: process.env.BASE_URL || 'https://app.lovel.dev',
    defaultCommandTimeout: process.env.CYPRESS_TIMEOUT || 10000,
    // ... outras configurações
  }
});
```

## 🐛 Solução de Problemas

### Erro: "Cypress não encontrado"
```bash
# Reinstalar Cypress
npm uninstall cypress
npm install cypress --save-dev
```

### Erro: "Python não reconhecido"
```bash
# Windows - Adicionar ao PATH
# Ou usar py ao invés de python
py cyber-scanner/scanner.py https://example.com
```

### Erro: "Módulo requests não encontrado"
```bash
pip install requests
# ou
pip install -r requirements.txt --force-reinstall
```

### Erro: "Permissão negada"
```bash
# Linux/macOS
sudo chmod +x cyber-scanner/scanner.py
```

## 📊 Estrutura de Pastas Após Instalação

```
qa-cyber-integration-lovel/
├── 📁 node_modules/          # Dependências Node.js
├── 📁 qa-tests/             # Módulo QA
│   ├── 📁 cypress/          # Testes Cypress
│   ├── 📁 models/           # Models MVCR
│   ├── 📁 views/            # Views MVCR
│   ├── 📁 controllers/      # Controllers MVCR
│   └── 📁 repositories/     # Repositories MVCR
├── 📁 cyber-scanner/        # Módulo Security
│   ├── 📁 models/           # Models Python
│   ├── 📁 controllers/      # Controllers Python
│   ├── 📁 repositories/     # Repositories Python
│   └── 📁 utils/            # Utilitários
├── 📁 reports/              # Relatórios gerados
├── 📁 docs/                 # Documentação
├── 📄 package.json          # Configuração Node.js
├── 📄 requirements.txt      # Dependências Python
├── 📄 cypress.config.js     # Configuração Cypress
└── 📄 README.md             # Documentação principal
```

## ✅ Validação da Instalação

### Teste Rápido QA
```bash
npx cypress run --spec "qa-tests/cypress/e2e/integrated-job-search.cy.js"
```

### Teste Rápido Security
```bash
python cyber-scanner/scanner.py https://github.com
```

### Verificar Integração
```bash
npm run test:integrated
```

## 🆘 Suporte

### Problemas Comuns
- [Issues no GitHub](https://github.com/LRMoraiss/QA-Cyber-Integration-Lovel/issues)
- [Documentação Cypress](https://docs.cypress.io/)
- [Documentação Python](https://docs.python.org/)

### Contato
- **Email**: luciano.morais@example.com
- **LinkedIn**: [linkedin.com/in/luciano-morais](https://linkedin.com/in/luciano-morais)
- **GitHub**: [@LRMoraiss](https://github.com/LRMoraiss)

---
**Última atualização**: Janeiro 2024  
**Versão**: 2.0.0