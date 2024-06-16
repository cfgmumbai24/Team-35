import React, { useState } from 'react';
import './FloatingButton.css';
import { assets } from '../../assets/assets'; // Ensure you have the chat icon in your assets

const FloatingButton = ({ onClick }) => {
  return (
    <div className="floating-button" onClick={onClick}>
      <img src={assets.chat_icon} alt="Chat" className="chat-icon" />
    </div>
  );
};

export default FloatingButton;
