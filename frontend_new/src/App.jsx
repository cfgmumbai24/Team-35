import React, { useState } from 'react'
import Navbar from './components/Navbar/Navbar'
import { Route , Routes} from 'react-router-dom'
import Home from './pages/Home/Home'
import Cart from './pages/Cart/Cart'
import PlaceOrder from './pages/PlaceOrder/PlaceOrder'
import Footer from './components/Footer/Footer'
import Login from './components/Login/Login'
import FloatingButton from './components/FloatingButton/FloatingButton'
// import CarouselFadeExample from './components/Carousel/CarouselFadeExample'
const App = () => {
  const [showChatbot, setShowChatbot] = useState(false);
  const [showLogin,setShowLogin] =useState(false)
  return (
    <>
    <div className='app'>
      <Navbar/>
      {/* <CarouselFadeExample/> */}
      <Routes>
        <Route path='/' element={<Home/>} exact />
        <Route path='/login' element={<Login/> }/>
      </Routes>
    </div>
<Footer />
<FloatingButton onClick={() => setShowChatbot(!showChatbot)} />
      {showChatbot && <Chatbot onClose={() => setShowChatbot(false)} />}
    </>
    
  )
}

export default App
