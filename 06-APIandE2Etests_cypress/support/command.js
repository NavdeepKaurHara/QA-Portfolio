import log from './logger';

Cypress.Commands.add('loginUI', (username, password) => {
  log('Navigating to login page');
  cy.get('input[name="username"]').type(username);
  cy.get('input[name="password"]').type(password);
  cy.get('button[type="submit"]').click();
  log(`Logging in with username: ${username}`);
});

Cypress.Commands.add('navigateToInvoices', () => {
  log('Navigating to the invoices page');
  cy.get('a[href="/invoices"]').click();
});

Cypress.Commands.add('assertVisible', (locator, message) => {
  log(`Asserting visibility of: ${message}`);
  cy.get(locator).should('be.visible');
});

Cypress.Commands.add('assertContainsText', (locator, text) => {
  log(`Asserting text: "${text}" for locator: ${locator}`);
  cy.get(locator).should('contain.text', text);
});
