import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'; // Adjust the path if App.js is in a different location
import './index.css'; // Optional, if you have a CSS file to import

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
