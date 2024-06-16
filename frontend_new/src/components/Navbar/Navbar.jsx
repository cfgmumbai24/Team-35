// import React, { useState } from 'react'
// import './Navbar.css'
// import { assets } from '../../assets/assets'
// import { Link } from 'react-router-dom';
// import SearchBar from '../SearchBar/SearchBar';
// import login from '../Login/Login';
// import { useNavigate } from 'react-router-dom';

// const Navbar = () => {
//      const [menu,setMenu]=useState("Home");

//      const navigate = useNavigate();
     
//      const handleSearch = (query) => {
//       console.log('Search query:', query);
//       // Implement search functionality here
//     };

//     const redirect =()=>{
//       navigate('/login',{replace:true})
//     }

//   return (
//     <div className='navbar'>
//       <h1>MULTIPLY</h1>
//       <ul className='navbar-menu'>
//         <Link to='/' onClick={() => setMenu("Home")} className={menu === 'Home' ? "active" : ""}>Home</Link>
//         <a href='#discover-menu' onClick={() => setMenu("Discover")} className={menu === 'Discover' ? "active" : ""}>Discover</a>
//         <a href='#footer' onClick={() => setMenu("Mobile-App")} className={menu === 'Mobile-App' ? "active" : ""}>Mobile-App</a>
//         <a href='#app-download' onClick={() => setMenu("Contact Us")} className={menu === 'Contact Us' ? "active" : ""}>Contact Us</a>
//       </ul>
//       <div className="navbar-right">
      
//       <SearchBar onSearch={handleSearch} />
//       <div className="navbar-search-icon">
//       </div>
//           <button className='btn2' onclick={redirect} >Sign In</button>
      
//     </div>
//     </div>
//   )
// }

// export default Navbar;
import React, { useState } from 'react';
import './Navbar.css';
import { Link, useNavigate } from 'react-router-dom';
import SearchBar from '../SearchBar/SearchBar';

const Navbar = () => {
  const [menu, setMenu] = useState('Home');
  const navigate = useNavigate();

  const handleSearch = (query) => {
    console.log('Search query:', query);
    // Implement search functionality here
  };

  const redirect = () => {
    navigate('/login', { replace: true });
  };

  return (
    <div className='navbar'>
      <h1>MULTIPLY</h1>
      <ul className='navbar-menu'>
        <Link to='/' onClick={() => setMenu('Home')} className={menu === 'Home' ? 'active' : ''}>
          Home
        </Link>
        <a href='#discover-menu' onClick={() => setMenu('Discover')} className={menu === 'Discover' ? 'active' : ''}>
          Discover
        </a>
        <a href='#footer' onClick={() => setMenu('Mobile-App')} className={menu === 'Mobile-App' ? 'active' : ''}>
          Mobile-App
        </a>
        <a
          href='#app-download'
          onClick={() => setMenu('Contact Us')}
          className={menu === 'Contact Us' ? 'active' : ''}
        >
          Contact Us
        </a>
      </ul>
      <div className='navbar-right'>
        <SearchBar onSearch={handleSearch} />
        <div className='navbar-search-icon'></div>
        <button className='btn2' onClick={redirect}>
          Sign In
        </button>
      </div>
    </div>
  );
};

export default Navbar;
