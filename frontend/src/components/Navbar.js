import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

const TICKER_ITEMS = [
  'DETROIT TECHNO ARCHIVE', 'BELLEVILLE THREE', 'JUAN ATKINS',
  'DERRICK MAY', 'KEVIN SAUNDERSON', 'KMS RECORDS', 'TRANSMAT',
  'METROPLEX', 'ROLAND TR-909', 'THE MUSIC INSTITUTE', 'HART PLAZA',
  'STRINGS OF LIFE', 'NO UFOs', 'BIG FUN', 'INNER CITY'
];

function Navbar() {
  const tickerText = [...TICKER_ITEMS, ...TICKER_ITEMS].join(' \u2014 ');

  return (
    <header>
      <div className="ticker">
        <div className="ticker-inner">{tickerText}</div>
      </div>
      <nav className="nav">
        <NavLink to="/" className="nav-logo">DTA</NavLink>
        <div className="nav-links">
          <NavLink to="/artists" className={({ isActive }) => isActive ? 'active' : ''}>Artists</NavLink>
          <NavLink to="/labels" className={({ isActive }) => isActive ? 'active' : ''}>Labels</NavLink>
          <NavLink to="/gear" className={({ isActive }) => isActive ? 'active' : ''}>Gear</NavLink>
          <NavLink to="/venues" className={({ isActive }) => isActive ? 'active' : ''}>Venues</NavLink>
        </div>
      </nav>
    </header>
  );
}

export default Navbar;