import React, { useEffect, useState } from 'react';
import './Gear.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';

function Gear() {
  const [gear, setGear] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    fetch(`${API}/gear`)
      .then(r => r.json())
      .then(data => { setGear(data); setLoading(false); });
  }, []);

  const types = ['all', ...new Set(gear.map(g => g.type))];
  const filtered = filter === 'all' ? gear : gear.filter(g => g.type === filter);

  return (
    <main className="gear-page page-wrapper">
      <div className="page-header">
        <div className="section-header">
          <span className="section-title">Gear</span>
          <div className="section-line"></div>
          <span className="section-count">{filtered.length} ENTRIES</span>
        </div>
        <div className="gear-filters">
          {types.map(t => (
            <button
              key={t}
              className={`filter-btn ${filter === t ? 'active' : ''}`}
              onClick={() => setFilter(t)}
            >
              {t}
            </button>
          ))}
        </div>
      </div>

      {loading ? (
        <div className="loading">LOADING...</div>
      ) : (
        <div className="gear-grid">
          {filtered.map(item => (
            <div className="gear-card" key={item.gear_id}>
              {item.image_url && (
                <img src={item.image_url} alt={item.name} style={{ width: '100%', aspectRatio: '16/9', objectFit: 'cover', marginBottom: '16px' }} />
              )}
              <div className="gear-type">{item.type}</div>
              <div className="gear-name">{item.name}</div>
              <div className="gear-mfr">{item.manufacturer} · {item.released_year}</div>
              <div className="gear-desc">{item.description}</div>
              <div className="gear-role">{item.role_in_detroit_techno}</div>
              <div className="gear-artists">
                {item.associated_artists?.map(a => <span className="tag" key={a}>{a}</span>)}
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}

export default Gear;