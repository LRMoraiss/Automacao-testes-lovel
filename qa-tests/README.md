# 🔍 QA Tests - Automação de Testes E2E

## 📋 Visão Geral

Módulo de automação de testes end-to-end desenvolvido com **Cypress** seguindo arquitetura **MVCR** (Model-View-Controller-Repository). Integra validações funcionais com verificações de segurança.

## 🏗️ Arquitetura MVCR

### 📊 Models (`/models`)
- **JobSearchModel.js**: Estrutura de dados para busca de vagas
- Encapsula lógica de negócio e validações

### 👁️ Views (`/views`) 
- **JobSearchPage.js**: Page Object Pattern
- Encapsula seletores e interações com elementos da UI

### 🎮 Controllers (`/controllers`)
- **JobSearchController.js**: Orquestra fluxos de teste
- Integra models, views e repositories

### 🗄️ Repositories (`/repositories`)
- **TestDataRepository.js**: Centraliza dados de teste
- Configurações e massa de dados

## 🧪 Cenários de Teste

### ✅ Cenário 1: Busca Válida
```javascript
// Busca por "Analista" com resultados esperados
controller.executeValidSearch();
```

### ❌ Cenário 2: Busca Inválida  
```javascript
// Busca por termo inexistente
controller.executeInvalidSearch();
```

### 🛡️ Cenário 3: Validação de Segurança
```javascript
// Verificação de cabeçalhos HTTP de segurança
controller.executeSecurityValidation(url);
```

## 🚀 Execução

### Pré-requisitos
```bash
npm install
```

### Modo Interativo
```bash
npm run test:qa:open
```

### Modo Headless
```bash
npm run test:qa
```

### Integração com Security Scanner
```bash
npm run test:integrated
```

## 📊 Relatórios

- **Videos**: `reports/videos/`
- **Screenshots**: `reports/screenshots/`
- **Logs**: Console do Cypress

## 🔧 Configurações

### cypress.config.js
- BaseURL: `https://app.lovel.dev`
- Timeouts: 10s
- Viewport: 1280x720
- Integração com scanner Python

### Comandos Customizados
- `cy.searchJobs(term, hasResults)`
- `cy.checkSecurityHeaders(url)`
- `cy.runSecurityScan(url)`

## 🎯 Boas Práticas Implementadas

- ✅ Page Object Pattern
- ✅ Arquitetura MVCR
- ✅ Comandos reutilizáveis
- ✅ Tratamento de erros
- ✅ Screenshots automáticos
- ✅ Integração QA + Security

## 🔍 Exemplo de Uso

```javascript
const JobSearchController = require('./controllers/JobSearchController');

describe('Testes Integrados', () => {
  let controller;

  beforeEach(() => {
    controller = new JobSearchController();
  });

  it('Deve executar busca com validação de segurança', () => {
    // Executa teste funcional
    const result = controller.executeValidSearch();
    
    // Valida dados
    expect(result.hasResults).to.be.true;
    
    // Executa scan de segurança
    controller.executeSecurityValidation('https://app.lovel.dev/jobs');
  });
});
```

---
**Desenvolvido por**: Luciano Rodrigues de Morais  
**Tecnologia**: Cypress + JavaScript  
**Padrão**: MVCR Architecture