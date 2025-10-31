/**
 * @file JobSearchModel.js - Model para estrutura de dados de busca de vagas
 * @author Luciano Rodrigues de Morais
 */

class JobSearchModel {
  constructor(searchTerm, expectedResults = true) {
    this.searchTerm = searchTerm;
    this.expectedResults = expectedResults;
    this.timestamp = new Date().toISOString();
  }

  static createValidSearch(term = 'Analista') {
    return new JobSearchModel(term, true);
  }

  static createInvalidSearch() {
    return new JobSearchModel('VagaInexistenteComTermoAleatorio12345XYZ', false);
  }

  getSearchData() {
    return {
      term: this.searchTerm,
      hasResults: this.expectedResults,
      executedAt: this.timestamp
    };
  }
}

module.exports = JobSearchModel;