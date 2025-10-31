const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://app.lovel.dev',
    specPattern: 'qa-tests/cypress/e2e/**/*.cy.js',
    supportFile: 'qa-tests/cypress/support/e2e.js',
    videosFolder: 'reports/videos',
    screenshotsFolder: 'reports/screenshots',
    video: true,
    screenshot: true,
    viewportWidth: 1280,
    viewportHeight: 720,
    defaultCommandTimeout: 10000,
    requestTimeout: 10000,
    responseTimeout: 10000,
    setupNodeEvents(on, config) {
      // Integração com scanner de segurança
      on('task', {
        runSecurityScan(url) {
          const { spawn } = require('child_process');
          
          return new Promise((resolve, reject) => {
            const scanner = spawn('python', ['cyber-scanner/scanner.py', url]);
            let output = '';
            
            scanner.stdout.on('data', (data) => {
              output += data.toString();
            });
            
            scanner.on('close', (code) => {
              if (code === 0) {
                resolve(output);
              } else {
                reject(new Error(`Scanner failed with code ${code}`));
              }
            });
          });
        }
      });
      
      return config;
    },
  },
  
  component: {
    devServer: {
      framework: 'create-react-app',
      bundler: 'webpack',
    },
  },
});