import log from './logger';

export function fillInvoiceForm({ netPowerGenerated, totalConsumption, marketPrice }) {
  log('Filling the invoice form with test data');
  cy.get('#netPowerGenerated').type(netPowerGenerated);
  cy.get('#totalConsumption').type(totalConsumption);
  cy.get('#marketPrice').type(marketPrice);
}

export function navigateTo(url) {
    cy.visit(url);
    cy.log(`Navigated to ${url}`);
  }
  