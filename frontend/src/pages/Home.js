import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';
const BELLEVILLE_THREE_IMG = 'https://detroit-techno-archive-media.s3.us-east-1.amazonaws.com/artists/The_Belleville_Three.jpg';

function Home() {
  const [artists, setArtists] = useState([]);
  const [counts, setCounts] = useState({ artists: 0, labels: 0, releases: 0, venues: 0, gear: 0 });

  useEffect(() => {
    fetch(`${API}/artists`).then(r => r.json()).then(data => {
      setArtists(data.slice(0, 3));
      setCounts(c => ({ ...c, artists: data.length }));
    });
    fetch(`${API}/labels`).then(r => r.json()).then(data => setCounts(c => ({ ...c, labels: data.length })));
    fetch(`${API}/releases`).then(r => r.json()).then(data => setCounts(c => ({ ...c, releases: data.length })));
    fetch(`${API}/venues`).then(r => r.json()).then(data => setCounts(c => ({ ...c, venues: data.length })));
    fetch(`${API}/gear`).then(r => r.json()).then(data => setCounts(c => ({ ...c, gear: data.length })));
  }, []);

  const initials = (name) => name.split(' ').map(w => w[0]).join('').slice(0, 2);

  return (
    <main className="home">
      <section className="hero page-wrapper">
        <div className="hero-content">
          <div className="hero-label">Est. Detroit, MI — 1980</div>
          <h1 className="hero-title">
            DETROIT<br /><span className="hero-title-accent">TECHNO</span><br />ARCHIVE
          </h1>
          <p className="hero-sub">
            A living archive of the artists, labels, venues, releases,
            and machines that built Detroit Techno and House music.
          </p>
          <div className="hero-stats">
            <div className="stat"><div className="stat-num">{counts.artists}</div><div className="stat-label">Artists</div></div>
            <div className="stat"><div className="stat-num">{counts.labels}</div><div className="stat-label">Labels</div></div>
            <div className="stat"><div className="stat-num">{counts.releases}</div><div className="stat-label">Releases</div></div>
            <div className="stat"><div className="stat-num">{counts.venues}</div><div className="stat-label">Venues</div></div>
            <div className="stat"><div className="stat-num">{counts.gear}</div><div className="stat-label">Gear</div></div>
          </div>
        </div>
        <div className="hero-image">
          <img src={BELLEVILLE_THREE_IMG} alt="The Belleville Three" />
          <p className="hero-founders">
            Juan Atkins, Derrick May, and Kevin Saunderson. Three kids from Belleville, Michigan who changed music forever. The founders of Detroit Techno.
          </p>
        </div>
      </section>

      <section className="featured page-wrapper">
        <div className="section-header">
          <span className="section-title">Featured Artists</span>
          <div className="section-line"></div>
          <Link to="/artists" className="view-all">View All →</Link>
        </div>
        <div className="artist-grid">
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
                <div className="artist-alias">{artist.aliases?.[0]}</div>
                <div className="artist-origin">{artist.origin}</div>
                <div className="artist-tags">
                  {artist.genres?.slice(0, 2).map(g => <span className="tag" key={g}>{g}</span>)}
                </div>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </main>
  );
}

export default Home;