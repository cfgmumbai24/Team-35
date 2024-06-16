import React from 'react'
import './Discover.css'
import { menu_list } from '../../assets/assets'

const Discover = ({category,setCategory}) => {
  return (
    <div className='discover-menu' id='discover-menu'>
      <h1>Discover What's In For You</h1>
      <p className='discover-menu-text'>Discover how Craedor Society can empower you with essential financial knowledge and tools for a secure future!</p>
      <div className="discover-menu-list">
        {menu_list.map((item,index)=>{
          return (
            <div onClick={()=>setCategory(prev=>prev===item.menu_name?"All":item.menu_name)}key={index} className="discover-menu-list-item">
              <img className={category===item.menu_name?"active":""} src={item.menu_image} alt=""/>
              <p>{item.menu_name}
              </p>

            </div>
          )
        }

        )}
      </div>
      <hr />
    </div>
  )
}

export default Discover
