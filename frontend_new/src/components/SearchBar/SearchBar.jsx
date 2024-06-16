import React, { useState } from 'react';
import './SearchBar.css';
import { assets } from '../../assets/assets';  // Assuming assets are imported from this path

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleInputChange = (e) => {
    setQuery(e.target.value);
    if (onSearch) {
      onSearch(e.target.value);
    }
  };

  return (
    <div className="search-bar-container">
      <input
        type="text"
        value={query}
        onChange={handleInputChange}
        className="search-input"
        placeholder="Search"
      />
      <img src={assets.microphone} alt="mic" className="search-icon mic-icon" />
      <img src={assets.search_icon} alt="search" className="search-icon search-icon-end" />
    </div>
  );
};

export default SearchBar;