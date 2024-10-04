/**
 * index.tsx
 * 
 * The entry point for the React app. Renders the main App component into the DOM.
 * 
 * @example
 * // Renders the React app into the DOM
 * <App />
 * 
 */
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Create root and render the App component into the #root div in index.html
const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
