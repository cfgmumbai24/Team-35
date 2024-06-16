import React, { useState, useContext } from 'react';
import './Goal.css'
import { assets } from '../../assets/assets'
import { StoreContext } from '../../context/StoreContext';
import Modals from '../../Modals';

const Goal = ({id,name,price,description,image, link, steps}) => {
 const {cartItems,addtocart,removefromcart}=useContext(StoreContext);
 const [modalIsOpen, setIsOpen] = useState(false);
 const [modalData, setModalData] = useState({});

 const openModal = ({ link, steps }) => {
   setModalData({ link, steps });
   setIsOpen(true);
   console.log("Modal opened with data:", { link, steps });
 };

 const closeModal = () => {
   setIsOpen(false);
   console.log("Modal closed");
 };

  return (
     <div className='goal-item'>
     <div className="goal-item-img-container">
       <img className=" goal-item-image"src={image} alt="" />
       {!
       
       <div className="goal-item-counter">
         <img onClick={()=>removefromcart(id)}src={assets.remove_icon_red} alt=""/>
         <p>{cartItems[id]}</p>
         <img onClick={()=>addtocart(id)}src={assets.add_icon_green} alt=""/>
       </div>

       }
     </div>
     <div className="goal-item-info">
       <div className="goal-item-rating">
         <p>{name}</p>
           {/* <img src={assets.rating_starts}alt="" /> */}
       </div>
       <p className="goal-item-desc">{description}</p>
       <button className='btn1' onClick={() => openModal({ link, steps })}>
          Read More..
        </button>
       
     </div>
     <Modals
        modalIsOpen={modalIsOpen}
        closeModal={closeModal}
        modalData={modalData}
      />
   </div>
  )
}

export default Goal








  
     





