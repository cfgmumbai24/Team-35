import { createContext, useEffect, useState  } from "react";

import {food_list } from "../assets/assets";

export const StoreContext =createContext(null)
const StoreContextProvider = (props) => {
     const [cartItems,setCartitems]=useState({});

     const addtocart=(itemId)=>{
          if(!cartItems[itemId]){
               setCartitems((prev)=>({...prev,[itemId]:1}))
          }
          else{
               setCartitems((prev)=>({...prev,[itemId]:prev[itemId]+1}))

          }

     }
 const removefromcart=(itemId)=>{
     setCartitems((prev)=>({...prev,[itemId]:prev[itemId]-1}))
 }
useEffect(()=>{
     console.log(cartItems);
},[cartItems])
     const contextValue={
         food_list,
         cartItems,
         setCartitems,
         addtocart,
         removefromcart
     }
     return (
          <StoreContext.Provider value={contextValue}>
               {props.children}
          </StoreContext.Provider>
     )
}
export default StoreContextProvider;
