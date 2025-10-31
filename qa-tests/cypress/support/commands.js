/**
 * @file commands.js - Comandos customizados do Cypress
 * @author Luciano Rodrigues de Morais
 */

// Comando para busca de vagas com validação
Cypress.Commands.add('searchJobs', (searchTerm, shouldHaveResults = true) => {
  cy.get('input[placeholder="Procure por vagas"]')
    .should('be.visible')
    .clear()
    .type(searchTerm);
  
  cy.get('button[type="submit"]').click();
  
  if (shouldHaveResults) {
    cy.contains('Vagas encontradas').should('be.visible');
    cy.get('[data-testid="job-card"]').should('have.length.greaterThan', 0);
  } else {
    cy.contains('Nenhuma vaga encontrada').should('be.visible');
  }
});

// Comando para capturar screenshot com timestamp
Cypress.Commands.add('screenshotWithTimestamp', (name) => {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  cy.screenshot(`${name}_${timestamp}`);
});

// Comando para aguardar carregamento da página
Cypress.Commands.add('waitForPageLoad', () => {
  cy.window().should('have.property', 'document');
  cy.document().should('have.property', 'readyState', 'complete');
});