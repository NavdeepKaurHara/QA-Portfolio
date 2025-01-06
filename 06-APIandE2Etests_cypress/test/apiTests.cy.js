import testData from '../fixtures/testData.json';
import locators from '../fixtures/locators.json';
import { formatInvoiceData, verifyResponseStatus, verifyResponseBody } from '../support/helper';

describe('API Tests for Invoicing Module', () => {
  before(() => {
    cy.login(testData.validLogin.username, testData.validLogin.password);
  });

  it('should successfully login with valid credentials', () => {
    cy.request({
      method: 'POST',
      url: '/api/login',
      body: testData.validLogin
    }).then((response) => {
      verifyResponseStatus(response, 200);
      expect(response.body).to.have.property('token');
    });
  });

  it('should fail login with invalid credentials', () => {
    cy.request({
      method: 'POST',
      url: '/api/login',
      body: testData.invalidLogin,
      failOnStatusCode: false // Prevent test failure on non-2xx responses
    }).then((response) => {
      verifyResponseStatus(response, 401);
      expect(response.body).to.have.property('error', 'Invalid username or password');
    });
  });

  it('should create an invoice successfully', () => {
    const invoiceData = formatInvoiceData(testData.invoice);

    cy.request({
      method: 'POST',
      url: '/api/invoices',
      headers: { Authorization: `Bearer ${Cypress.env('token')}` },
      body: invoiceData
    }).then((response) => {
      verifyResponseStatus(response, 201);
      verifyResponseBody(response, {
        message: 'Invoice created successfully',
        invoiceId: response.body.invoiceId
      });
    });
  });

  it('should handle missing fields in invoice creation', () => {
    const incompleteInvoiceData = { netPowerGenerated: 200 }; // Missing fields

    cy.request({
      method: 'POST',
      url: '/api/invoices',
      headers: { Authorization: `Bearer ${Cypress.env('token')}` },
      body: incompleteInvoiceData,
      failOnStatusCode: false
    }).then((response) => {
      verifyResponseStatus(response, 400);
      expect(response.body).to.have.property('error', 'Missing required fields');
    });
  });
});
