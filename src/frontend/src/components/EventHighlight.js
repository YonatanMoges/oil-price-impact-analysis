// src/frontend/src/components/EventHighlight.js
import React from 'react';

const EventHighlight = ({ event }) => {
  return (
    <div className="event-highlight">
      <h4>{event.name}</h4>
      <p>{event.date}</p>
      <p>{event.description}</p>
    </div>
  );
};

export default EventHighlight;
