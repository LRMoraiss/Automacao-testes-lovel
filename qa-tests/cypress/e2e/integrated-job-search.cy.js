/**
 * @file integrated-job-search.cy.js - Testes integrados QA + Security
 * @author Luciano Rodrigues de Morais
 */

const JobSearchController = require('../../controllers/JobSearchController');

describe('QA + Security: Busca de Vagas Integrada', () => {
  let controller;

  beforeEach(() => {
    controller = new JobSearchController();
  });

  it('Cenário 1: Busca válida com verificação de segurança', () => {
    const searchResult = controller.executeValidSearch();
    
    // Validar dados do teste
    expect(searchResult.term).to.equal('Analista');
    expect(searchResult.hasResults).to.be.true;
    
    // Executar scan de segurança
    controller.executeSecurityValidation('https://app.lovel.dev/jobs');
  });

  it('Cenário 2: Busca inválida com verificação de segurança', () => {
    const searchResult = controller.executeInvalidSearch();
    
    // Validar dados do teste
    expect(searchResult.hasResults).to.be.false;
    
    // Executar scan de segurança mesmo em cenário de falha
    controller.executeSecurityValidation('https://app.lovel.dev/jobs');
  });

  it('Cenário 3: Validação exclusiva de cabeçalhos de segurança', () => {
    cy.visit('https://app.lovel.dev/jobs');
    
    cy.request('GET', 'https://app.lovel.dev/jobs').then((response) => {
      const headers = response.headers;
      
      // Verificações de segurança críticas
      cy.wrap(headers).should('have.property', 'strict-transport-security');
      cy.wrap(headers).should('have.property', 'x-frame-options');
      
      // Log dos resultados
      cy.log('Security Headers Analysis:', JSON.stringify(headers, null, 2));
    });
  });
});