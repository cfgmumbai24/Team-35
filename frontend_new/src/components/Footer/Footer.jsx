import React from 'react'
import './Footer.css'
import { assets } from '../../assets/assets'

const Footer  = () => {
  return (
    <div className='footer' id='footer'>
      <div className="footer-content">
        <div className="footer-content-left">
          <h1>Multiply</h1>
          <p>Unlock financial wisdom, embrace economic independence, and join a community dedicated to transforming lives through knowledge. Your journey to financial freedom starts here.</p>
          <div className="footer-social-icons">
            <img src={assets.facebook_icon} alt="" />
            <img src={assets.twitter_icon} alt="" />
            <img src={assets.linkedin_icon} alt="" />
          </div>
        </div>
        <div className="footer-content-center">
<h2>COMPANY</h2>
<ul>
  <li>Home</li>
  <li>About Us</li>
  <li>Delivery</li>
  <li>Privacy Policy</li>
</ul>
        </div>
        <div className="footer-content-right">
<h2>Get In-Touch</h2>
<ul>
  <li>+1-121-345-678</li>
  <li>customercar@gmail.com</li>
</ul>
        </div>
      </div>
      <hr/>
      <p className="footer-copyright">&copy; 2024 Craedor Society. Empowering India, One Financially Literate Step at a Time.</p>
    </div>
  )
}

export default Footer 

