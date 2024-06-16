import React, { useContext }  from 'react'
import './GoalDisplay.css'
import StoreContextProvider, { StoreContext } from '../../context/StoreContext';
import Goal from '../Goal/Goal';
import { food_list } from '../../assets/assets';



const GoalDisplay = ({category}) => {
     const {food_list} = useContext(StoreContext)
  return (
     <div className='goal-display' id='goal-display'>
     <h2>Explore more</h2>
     <div className="goal-display-list">
       {food_list.map((item,index)=>{
         if(category==="All" || category===item.category){
           return <Goal key={index} id={item._id} name={item.name} description={item.description} price={item.price} image={item.image} link={item.link} steps={item.steps}/>
         }
          
       })}
     </div>
   </div>
  )
}

export default GoalDisplay







 