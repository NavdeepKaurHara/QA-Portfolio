import locators from '../fixtures/locators.json';
import testData from '../fixtures/testData.json';
import { fillInvoiceForm } from '../support/helper';
import log from '../support/logger';

describe('Enhanced UI Tests for Invoicing Module', () => {
  beforeEach(() => {
    cy.visit('/');
    log('Opened the application');
  });

  it('should successfully log in and navigate to dashboard', () => {
    cy.loginUI(testData.validLogin.username, testData.validLogin.password);

    cy.assertVisible(locators.dashboardPage.welcomeMessage, 'Welcome Message');
    log('Login successful. Dashboard loaded.');
  });

  it('should display error message for invalid login', () => {
    cy.loginUI(testData.invalidLogin.username, testData.invalidLogin.password);

    cy.assertContainsText(
      locators.loginPage.errorMessage,
      'Invalid username or password'
    );
    log('Error message displayed for invalid login');
  });

  it('should navigate to invoices tab and verify page load', () => {
    cy.loginUI(testData.validLogin.username, testData.validLogin.password);
    cy.navigateToInvoices();

    cy.url().should('include', '/invoices');
    log('Successfully navigated to the invoices page');
  });

  it('should create a new invoice successfully', () => {
    cy.loginUI(testData.validLogin.username, testData.validLogin.password);
    cy.navigateToInvoices();

    fillInvoiceForm(testData.invoice.valid);
    cy.get(locators.invoicePage.submitButton).click();

    cy.assertContainsText(
      locators.invoicePage.successMessage,
      'Invoice created successfully'
    );
    log('Invoice creation successful');
  });

  it('should display validation errors for incomplete invoice data', () => {
    cy.loginUI(testData.validLogin.username, testData.validLogin.password);
    cy.navigateToInvoices();

    fillInvoiceForm(testData.invoice.invalid); // Missing fields
    cy.get(locators.invoicePage.submitButton).click();

    cy.assertContainsText(
      locators.invoicePage.formErrors,
      'All fields are required'
    );
    log('Validation errors displayed as expected');
  });
});
