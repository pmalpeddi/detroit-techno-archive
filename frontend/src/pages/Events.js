import React, { useEffect, useState } from 'react';
import './Events.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';

function Events() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/events`)
      .then(r => r.json())
      .then(data => {
        setEvents(data.sort((a, b) => b.year - a.year));
        setLoading(false);
      });
  }, []);

  return (
    <main className="events-page page-wrapper">
      <div className="page-header">
        <div className="section-header">
          <span className="section-title">Events</span>
          <div className="section-line"></div>
          <span className="section-count">{events.length} ENTRIES</span>
        </div>
      </div>

      {loading ? (
        <div className="loading">LOADING...</div>
      ) : (
        <div className="events-list">
          {events.map(event => (
            <div className="event-row" key={event.event_id}>
              <div className="event-img">
                {event.image_url
                  ? <img src={event.image_url} alt={event.name} />
                  : <div className="event-img-placeholder">{event.year}</div>
                }
              </div>
              <div className="event-info">
                <div className="event-meta-row">
                  <span className={`event-status ${event.status}`}>{event.status}</span>
                  <span className="event-type">{event.type}</span>
                  <span className="event-date">{event.date}</span>
                </div>
                <div className="event-name">{event.name}</div>
                <p className="event-description">{event.description}</p>
                {event.historical_significance && (
                  <p className="event-significance">{event.historical_significance}</p>
                )}
                {event.lineup && event.lineup.length > 0 && (
                  <div className="event-lineup">
                    <span className="lineup-label">LINEUP</span>
                    <div className="lineup-tags">
                      {event.lineup.map((artist, i) => (
                        <span className="lineup-tag" key={i}>{artist}</span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}

export default Events;