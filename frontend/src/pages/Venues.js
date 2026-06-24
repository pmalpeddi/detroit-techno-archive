import React, { useEffect, useState } from 'react';
import './Venues.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';

function Venues() {
  const [venues, setVenues] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/venues`)
      .then(r => r.json())
      .then(data => { setVenues(data.sort((a, b) => a.opened - b.opened)); setLoading(false); });
  }, []);

  return (
    <main className="venues-page page-wrapper">
      <div className="page-header">
        <div className="section-header">
          <span className="section-title">Venues</span>
          <div className="section-line"></div>
          <span className="section-count">{venues.length} ENTRIES</span>
        </div>
      </div>

      {loading ? (
        <div className="loading">LOADING...</div>
      ) : (
        <div className="venues-list">
          {venues.map(venue => (
            <div className="venue-row" key={venue.venue_id}>
              <div className="venue-img">
                {venue.image_url
                  ? <img src={venue.image_url} alt={venue.name} />
                  : <div className="venue-img-placeholder">{venue.opened}</div>
                }
              </div>
              <div className="venue-info">
                <div className="venue-status-row">
                  <span className={`venue-status ${venue.status}`}>{venue.status}</span>
                  <span className="venue-type">{venue.type}</span>
                </div>
                <div className="venue-name">{venue.name}</div>
                <div className="venue-address">{venue.address}</div>
                <div className="venue-years">
                  {venue.opened}{venue.closed ? ` — ${venue.closed}` : ' — present'}
                </div>
                <p className="venue-significance">{venue.historical_significance}</p>
                <div className="venue-tags">
                  {venue.genres?.slice(0, 3).map(g => <span className="tag" key={g}>{g}</span>)}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}

export default Venues;