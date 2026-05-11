import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Artists from './pages/Artists';
import Labels from './pages/Labels';
import Gear from './pages/Gear';
import ArtistDetail from './pages/ArtistDetail';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/artists" element={<Artists />} />
        <Route path="/labels" element={<Labels />} />
        <Route path="/gear" element={<Gear />} />
        <Route path="/artists/:artist_id" element={<ArtistDetail />} />
      </Routes>
    </Router>
  );
}

export default App;