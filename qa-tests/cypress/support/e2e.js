/**
 * @file e2e.js - Configurações e comandos customizados do Cypress
 * @author Luciano Rodrigues de Morais
 */

// Import commands.js using ES2015 syntax:
import './commands'

// Alternatively you can use CommonJS syntax:
// require('./commands')

// Configurações globais
Cypress.on('uncaught:exception', (err, runnable) => {
  // Previne que erros JS da aplicação quebrem os testes
  return false;
});

// Comando customizado para verificar cabeçalhos de segurança
Cypress.Commands.add('checkSecurityHeaders', (url) => {
  cy.request('GET', url).then((response) => {
    const headers = response.headers;
    
    // Verificar HSTS
    if (headers['strict-transport-security']) {
      cy.log('✅ HSTS: Presente');
    } else {
      cy.log('❌ HSTS: Ausente - Vulnerável a SSL stripping');
    }
    
    // Verificar X-Frame-Options
    if (headers['x-frame-options']) {
      cy.log('✅ X-Frame-Options: Presente');
    } else {
      cy.log('❌ X-Frame-Options: Ausente - Vulnerável a clickjacking');
    }
    
    // Verificar X-Content-Type-Options
    if (headers['x-content-type-options'] === 'nosniff') {
      cy.log('✅ X-Content-Type-Options: Configurado corretamente');
    } else {
      cy.log('❌ X-Content-Type-Options: Ausente ou mal configurado');
    }
    
    return cy.wrap(headers);
  });
});

// Comando para integração com scanner Python
Cypress.Commands.add('runSecurityScan', (url) => {
  cy.task('runSecurityScan', url).then((result) => {
    cy.log('Security Scan Results:', result);
    return cy.wrap(result);
  });
});