import React, { useState } from 'react';
import './Login.css';

const Login = () => {
    // const [isRightPanelActive, setIsRightPanelActive] = useState(false);
    // const [phone, setPhone] = useState("");
    // const [password, setPassword] = useState("");
    // const handleOverlayClick = () => {
    //     setIsRightPanelActive(!isRightPanelActive);
    // };

    const handleSignIn = async () => {
        // const phone = phone;
        // const pass = password
        // console.log("\n Phone:", phone);
        // console.log("\n Password:", pass);
        // const payload = {
        //     "phone": phone,
        //     "pass": pass
        // }
        const response = await fetch("http://127.0.0.1:8000/prefetch_login", {
            method: "GET"
            // headers: {
            //     "Content-Type": "application/json"
            // }
            // body: JSON.stringify(payload)

        })

        const data = response.json()
        console.log("\n Response:", response);
        console.log("\n Data:", data);
    }

    return (
        <button className='btnpad' onClick={handleSignIn}>Sign Up</button>
        // <div className='loginSection'>
        //     {/* <span className="big-circle">
        //         <span className="inner-circle"></span>
        //     </span> */}
        //     <img src="https://i.imgur.com/wcGWHvx.png" className="square" alt="" />
        //     <div className={`container ${isRightPanelActive ? 'right-panel-active' : ''}`} id="container">
        //         <div className="form-container sign-up-container">
        //             <form action="#">
        //                 <h1>Create Account</h1>
        //                 {/* <div className="social-container">
        //                     <a href="#" className="social"><i className="fab fa-facebook-f"></i></a>
        //                     <a href="#" className="social"><i className="fab fa-google-plus-g"></i></a>
        //                     <a href="#" className="social"><i className="fab fa-linkedin-in"></i></a>
        //                 </div> */}
        //                 {/* <span>or use your  for registration</span> */}
        //                 <div className="infield">
        //                     <input type="text" placeholder="Name" />
        //                     <label></label>
        //                 </div>
        //                 <div className="infield">
        //                     <input type="number" placeholder="Phone number" name="number" />
        //                     <label></label>
        //                 </div>
        //                 <div className="infield">
        //                     <input type="password" placeholder="Password" />
        //                     <label></label>
        //                 </div>
        //                 {/* <button className='btnpad' onClick={handleSignIn}>Sign Up</button> */}
        //             </form>
        //         </div>
        //         <div className="form-container sign-in-container">
        //             <form action="#">
        //                 <h1>Sign in</h1>
        //                 {/* <div className="social-container">
        //                     <a href="#" className="social"><i className="fab fa-facebook-f"></i></a>
        //                     <a href="#" className="social"><i className="fab fa-google-plus-g"></i></a>
        //                     <a href="#" className="social"><i className="fab fa-linkedin-in"></i></a>
        //                 </div> */}
        //                 {/* <span>or use your account</span> */}
        //                 <div className="infield">
        //                     <input type="number" placeholder="Phone number" name="number" />
        //                     <label></label>
        //                 </div>
        //                 <div className="infield">
        //                     <input type="password" placeholder="Password" />
        //                     <label></label>
        //                 </div>
        //                 <a href="#" className="forgot">Forgot your password?</a>
        //                 <button className='btnpad'>Sign In</button>
        //             </form>
        //         </div>
        //         <div className="overlay-container" id="overlayCon">
        //             <div className="overlay">
        //                 <div className="overlay-panel overlay-left">
        //                     <h1>Welcome Back!</h1>
        //                     <p>To keep connected with us please login with your personal info</p>
        //                     <button onClick={handleOverlayClick}>Sign In</button>
        //                 </div>
        //                 <div className="overlay-panel overlay-right">
        //                     <h1>Hello, Friend!</h1>
        //                     <p>Enter your personal details and start journey with us</p>
        //                     <button onClick={handleOverlayClick}>Sign Up</button>
        //                 </div>
        //             </div>
        //             <button id="overlayBtn" className="btnScaled" onClick={handleOverlayClick}></button>
        //         </div>
        //     </div>
        // </div>
    );
};

export default Login;
