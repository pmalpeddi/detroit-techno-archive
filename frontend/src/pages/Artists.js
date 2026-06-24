import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './Artists.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';

function Artists() {
  const [artists, setArtists] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/artists`)
      .then(r => r.json())
      .then(data => { setArtists(data); setLoading(false); });
  }, []);

  const initials = (name) => name.split(' ').map(w => w[0]).join('').slice(0, 2);

  return (
    <main className="artists-page page-wrapper">
      <div className="page-header">
        <div className="section-header">
          <span className="section-title">Artists</span>
          <div className="section-line"></div>
          <span className="section-count">{artists.length} ENTRIES</span>
        </div>
      </div>

      {loading ? (
        <div className="loading">LOADING...</div>
      ) : (
        <div className="artists-grid">
          {artists.map(artist => (
            <Link to={`/artists/${artist.artist_id}`} key={artist.artist_id} style={{ textDecoration: 'none' }}>
            <div className="artist-card">
              <div className="artist-img">
                {artist.image_url
                ? <img src={artist.image_url} alt={artist.name} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                : initials(artist.name)
                }
              </div>
              <div className="artist-name">{artist.name}</div>
              {artist.aliases?.[0] && <div className="artist-alias">{artist.aliases[0]}</div>}
              <div className="artist-origin">{artist.origin} · {artist.active_years}</div>
              <div className="artist-bio">{artist.biography}</div>
              <div className="artist-tags">
                {artist.genres?.slice(0, 2).map(g => <span className="tag" key={g}>{g}</span>)}
              </div>
            </div>
            </Link>
          ))}
        </div>
      )}
    </main>
  );
}

export default Artists;