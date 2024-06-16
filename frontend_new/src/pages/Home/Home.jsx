import React, { useState , useEffect} from 'react'
import './Home.css'
import Header from '../../components/Header/Header'
import Discover from '../../components/Discover/Discover'
import AppDownload from '../../components/AppDownload/AppDownload'

import GoalDisplay from '../../components/GoalDisplay/GoalDisplay'


const Home = () => {
  const [category,setCategory]=useState("All");
  const [language, setLanguage] = useState("English")
  localStorage.setItem("lanugage", language)

  const UserProfile = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    

    
    useEffect(() => {
      const fetchUserData = async () => {
        try {
          const lang = await localStorage.getItem('language')
          const response = await fetch('http://127.0.0.1:8000/prefetch_login', {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
                },
            body: language
          });
          if (!response.ok) {
            throw new Error('Failed to fetch data');
          }
          const data = await response.json();
          setUser(data);
        } catch (error) {
          setError(error.message);
        } finally {
          setLoading(false);
        }
      }
      fetchUserData();
  }, []); // Empty dependency array means this effect runs once when the component mounts

  if (loading) {
   
  return (
    <div>
      <Header/>
      <Discover category={category} setCategory={setCategory}/>
      <GoalDisplay category={category}/>
      <AppDownload/>
    </div>
  );
};
export default Home
