import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import './ArtistDetail.css';

const API = 'https://cvlthm6c36.execute-api.us-east-1.amazonaws.com/Prod';

function ArtistDetail() {
  const { artist_id } = useParams();
  const [artist, setArtist] = useState(null);
  const [releases, setReleases] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API}/artists/${artist_id}`)
      .then(r => r.json())
      .then(data => {
        setArtist(data);
        setLoading(false);
      });
    fetch(`${API}/releases`)
      .then(r => r.json())
      .then(data => setReleases(data));
  }, [artist_id]);

  const initials = (name) => name.split(' ').map(w => w[0]).join('').slice(0, 2);

  const artistReleases = releases.filter(r =>
    r.artist === artist?.name ||
    artist?.aliases?.some(a => r.aliases_used === a) ||
    artist?.associated_acts?.some(act => r.artist === act)
  );

  const getReleaseForTrack = (trackName) =>
    artistReleases.find(r => r.tracklist?.includes(trackName));

  if (loading) return <div className="detail-loading">LOADING...</div>;
  if (!artist) return <div className="detail-loading">NOT FOUND</div>;

  return (
    <main className="artist-detail page-wrapper">
      <Link to="/artists" className="back-link">← Artists</Link>

      <div className="detail-hero">
        <div className="detail-img">
          {artist.image_url
            ? <img src={artist.image_url} alt={artist.name} />
            : <span className="detail-initials">{initials(artist.name)}</span>
          }
        </div>
        <div className="detail-header">
          <div className="detail-label">Artist</div>
          <h1 className="detail-name">{artist.name}</h1>
          {artist.aliases?.length > 0 && (
            <div className="detail-aliases">
              {artist.aliases.map(a => <span key={a} className="alias-pill">{a}</span>)}
            </div>
          )}
          <div className="detail-meta-row">
            <span>{artist.origin}</span>
            <span className="meta-divider">—</span>
            <span>{artist.active_years}</span>
          </div>
          <div className="detail-tags">
            {artist.genres?.map(g => <span className="tag" key={g}>{g}</span>)}
          </div>
        </div>
      </div>

      <div className="detail-body">
        <div className="detail-main">
          <div className="detail-section">
            <div className="detail-section-title">Biography</div>
            <p className="detail-bio">{artist.biography}</p>
          </div>

          {artist.notable_tracks?.length > 0 && (
            <div className="detail-section">
              <div className="detail-section-title">Notable Tracks</div>
              <div className="track-list">
                {artist.notable_tracks.map((t, i) => {
                  const release = getReleaseForTrack(t);
                  return (
                    <div className="track-row" key={t}>
                      {release?.image_url
                        ? <img src={release.image_url} alt={release.title} className="track-artwork" />
                        : <span className="track-num">0{i + 1}</span>
                      }
                      <div className="track-info">
                        <span className="track-name">{t}</span>
                        {release && <span className="track-release">{release.title} · {release.year}</span>}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {artistReleases.length > 0 && (
            <div className="detail-section">
              <div className="detail-section-title">Releases</div>
              <div className="releases-grid">
                {artistReleases.map(r => (
                  <div className="release-card" key={r.release_id}>
                    {r.image_url
                      ? <img src={r.image_url} alt={r.title} className="release-artwork" />
                      : <div className="release-artwork-placeholder">{r.year}</div>
                    }
                    <div className="release-title">{r.title}</div>
                    <div className="release-meta">{r.aliases_used || r.artist} · {r.year}</div>
                    <div className="release-format">{r.format}</div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        <div className="detail-sidebar">
          {artist.birth_name && (
            <div className="sidebar-block">
              <div className="sidebar-label">Birth Name</div>
              <div className="sidebar-value">{artist.birth_name}</div>
            </div>
          )}
          {artist.born && (
            <div className="sidebar-block">
              <div className="sidebar-label">Born</div>
              <div className="sidebar-value">{artist.born}</div>
            </div>
          )}
          {artist.associated_acts?.length > 0 && (
            <div className="sidebar-block">
              <div className="sidebar-label">Associated Acts</div>
              {artist.associated_acts.map(a => <div className="sidebar-value" key={a}>{a}</div>)}
            </div>
          )}
          {artist.associated_labels?.length > 0 && (
            <div className="sidebar-block">
              <div className="sidebar-label">Labels</div>
              {artist.associated_labels.map(l => <div className="sidebar-value" key={l}>{l}</div>)}
            </div>
          )}
          {artist.gear?.length > 0 && (
            <div className="sidebar-block">
              <div className="sidebar-label">Gear</div>
              {artist.gear.map(g => <div className="sidebar-value" key={g}>{g}</div>)}
            </div>
          )}
        </div>
      </div>
    </main>
  );
}

export default ArtistDetail;