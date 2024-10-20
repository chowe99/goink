// src/App.js
import React from 'react';
import AirQualityChart from './components/AirQualityChart';
import './App.css'; // Optional: For styling


function App() {
  return (
    <div className="App">
      <h1>Goink Data Visualization</h1>
      <AirQualityChart />
    </div>
  );
}

export default App;

