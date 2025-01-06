const log = (message) => {
    const timestamp = new Date().toLocaleTimeString();
    cy.log(`[${timestamp}] ${message}`);
    console.log(`[${timestamp}] ${message}`);
  };
  
  export default log;
  
