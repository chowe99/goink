// src/components/DatasetChart.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';

const DatasetChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/scraper/api/datasets/')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching datasets:', error);
      });
  }, []);

  return (
    <LineChart width={800} height={400} data={data}>
      <Line type="monotone" dataKey="someNumericField" stroke="#8884d8" />
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="someCategoryField" />
      <YAxis />
      <Tooltip />
    </LineChart>
  );
};

export default DatasetChart;

