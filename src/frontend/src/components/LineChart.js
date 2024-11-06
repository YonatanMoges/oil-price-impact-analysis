// src/frontend/src/components/LineChart.js
import React, { useEffect, useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend } from 'recharts';
import axios from 'axios';

const LineChartComponent = () => {
  const [oilData, setOilData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/oil_data")
      .then(response => setOilData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <LineChart width={800} height={400} data={oilData}>
      <Line type="monotone" dataKey="Price" stroke="#8884d8" />
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="Date" />
      <YAxis />
      <Tooltip />
      <Legend />
    </LineChart>
  );
};

export default LineChartComponent;
