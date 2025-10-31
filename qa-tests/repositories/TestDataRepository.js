/**
 * @file TestDataRepository.js - Repository para dados de teste
 * @author Luciano Rodrigues de Morais
 */

class TestDataRepository {
  static getValidSearchTerms() {
    return [
      'Analista',
      'Desenvolvedor',
      'QA',
      'Tester',
      'Engenheiro'
    ];
  }

  static getInvalidSearchTerms() {
    return [
      'VagaInexistenteComTermoAleatorio12345XYZ',
      'TermoQueNaoExiste999',
      'InvalidJobSearch2024'
    ];
  }

  static getSecurityHeaders() {
    return {
      required: [
        'strict-transport-security',
        'x-frame-options',
        'x-content-type-options'
      ],
      optional: [
        'content-security-policy',
        'x-xss-protection',
        'referrer-policy'
      ]
    };
  }

  static getTestEnvironments() {
    return {
      production: 'https://app.lovel.dev',
      staging: 'https://staging.lovel.dev',
      development: 'https://dev.lovel.dev'
    };
  }
}

module.exports = TestDataRepository;