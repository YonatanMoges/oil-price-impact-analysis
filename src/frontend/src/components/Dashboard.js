// src/frontend/src/pages/Dashboard.js
import React from 'react';
import LineChartComponent from '../components/LineChart';
import EventHighlight from '../components/EventHighlight';

const Dashboard = () => {
  const events = [
    { name: 'Event A', date: '2020-01-01', description: 'Significant event affecting oil prices' },
    { name: 'Event B', date: '2021-06-15', description: 'Another significant event' },
  ];

  return (
    <div>
      <h1>Brent Oil Price Dashboard</h1>
      <LineChartComponent />
      <div className="event-highlights">
        {events.map((event, index) => (
          <EventHighlight key={index} event={event} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
