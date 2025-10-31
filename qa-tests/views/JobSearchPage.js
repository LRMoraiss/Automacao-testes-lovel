/**
 * @file JobSearchPage.js - Page Object para página de busca de vagas
 * @author Luciano Rodrigues de Morais
 */

class JobSearchPage {
  constructor() {
    this.url = 'https://app.lovel.dev/jobs';
    this.selectors = {
      searchInput: 'input[placeholder="Procure por vagas"]',
      submitButton: 'button[type="submit"]',
      resultsText: 'Vagas encontradas',
      noResultsText: 'Nenhuma vaga encontrada',
      jobCard: '[data-testid="job-card"]'
    };
  }

  visit() {
    cy.visit(this.url);
    return this;
  }

  searchFor(term) {
    cy.get(this.selectors.searchInput)
      .should('be.visible')
      .clear()
      .type(term);
    return this;
  }

  submitSearch() {
    cy.get(this.selectors.submitButton).click();
    return this;
  }

  verifyResultsVisible() {
    cy.contains(this.selectors.resultsText).should('be.visible');
    cy.get(this.selectors.jobCard).should('have.length.greaterThan', 0);
    return this;
  }

  verifyNoResults() {
    cy.contains(this.selectors.noResultsText).should('be.visible');
    return this;
  }

  checkSecurityHeaders() {
    cy.window().then((win) => {
      cy.request('GET', this.url).then((response) => {
        const headers = response.headers;
        
        // Verificar HSTS
        if (headers['strict-transport-security']) {
          cy.log('✓ HSTS header presente');
        } else {
          cy.log('⚠ HSTS header ausente');
        }

        // Verificar X-Frame-Options
        if (headers['x-frame-options']) {
          cy.log('✓ X-Frame-Options presente');
        } else {
          cy.log('⚠ X-Frame-Options ausente');
        }
      });
    });
    return this;
  }
}

module.exports = JobSearchPage;