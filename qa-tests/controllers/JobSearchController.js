/**
 * @file JobSearchController.js - Controller para lógica de testes de busca
 * @author Luciano Rodrigues de Morais
 */

const JobSearchModel = require('../models/JobSearchModel');
const JobSearchPage = require('../views/JobSearchPage');

class JobSearchController {
  constructor() {
    this.page = new JobSearchPage();
  }

  executeValidSearch() {
    const searchModel = JobSearchModel.createValidSearch();
    const searchData = searchModel.getSearchData();
    
    this.page
      .visit()
      .searchFor(searchData.term)
      .submitSearch()
      .verifyResultsVisible()
      .checkSecurityHeaders();
    
    return searchData;
  }

  executeInvalidSearch() {
    const searchModel = JobSearchModel.createInvalidSearch();
    const searchData = searchModel.getSearchData();
    
    this.page
      .visit()
      .searchFor(searchData.term)
      .submitSearch()
      .verifyNoResults();
    
    return searchData;
  }

  executeSecurityValidation(url) {
    cy.task('runSecurityScan', url).then((result) => {
      cy.log('Security Scan Results:', result);
    });
  }
}

module.exports = JobSearchController;