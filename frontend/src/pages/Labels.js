import React, { useEffect, useState } from 'react';
import './Labels.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';

function Labels() {
  const [labels, setLabels] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API}/labels`)
      .then(r => r.json())
      .then(data => { setLabels(data.sort((a, b) => a.founded - b.founded)); setLoading(false); })
      .catch(() => { setError('Failed to load labels.'); setLoading(false); });
  }, []);

  return (
    <main className="labels-page page-wrapper">
      <div className="page-header">
        <div className="section-header">
          <span className="section-title">Record Labels</span>
          <div className="section-line"></div>
          <span className="section-count">{labels.length} ENTRIES</span>
        </div>
      </div>

      {loading ? (
        <div className="loading">LOADING...</div>
      ) : error ? (
        <div className="loading">{error}</div>
      ) : (
        <div className="labels-list">
          {labels.map(label => (
            <div className="label-row" key={label.label_id}>
              <div className="label-year">{label.founded}</div>
              <div className="label-info">
                <div className="label-name">{label.name}</div>
                <div className="label-founder">Founded by {label.founder}</div>
                <div className="label-profile">{label.description}</div>
                <div className="label-tags">
                  {label.genres?.slice(0, 3).map(g => <span className="tag" key={g}>{g}</span>)}
                </div>
              </div>
              <div className="label-meta">
                {label.image_url && (
                 <img src={label.image_url} alt={label.name} style={{ width: '100%', aspectRatio: '1', objectFit: 'cover', marginBottom: '12px' }} />
                )}
                <div className="label-origin">{label.origin}</div>
                <div className="label-dist">{label.distribution}</div>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}

export default Labels;