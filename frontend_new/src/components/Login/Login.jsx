// import React, { useState } from 'react';
// import './Login.css';

// const Login = () => {
//     const [isRightPanelActive, setIsRightPanelActive] = useState(false);

//     const handleOverlayClick = () => {
//         setIsRightPanelActive(!isRightPanelActive);
//     };

//     return (
//         <div className='loginSection'>
//             {/* <span className="big-circle">
//                 <span className="inner-circle"></span>
//             </span> */}
//             <img src="https://i.imgur.com/wcGWHvx.png" className="square" alt="" />
//             <div className={`container ${isRightPanelActive ? 'right-panel-active' : ''}`} id="container">
//                 <div className="form-container sign-up-container">
//                     <form action="#">
//                         <h1>Create Account</h1>
//                         {/* <div className="social-container">
//                             <a href="#" className="social"><i className="fab fa-facebook-f"></i></a>
//                             <a href="#" className="social"><i className="fab fa-google-plus-g"></i></a>
//                             <a href="#" className="social"><i className="fab fa-linkedin-in"></i></a>
//                         </div> */}
//                         {/* <span>or use your  for registration</span> */}
//                         <div className="infield">
//                             <input type="text" placeholder="Name" />
//                             <label></label>
//                         </div>
//                         <div className="infield">
//                             <input type="number" placeholder="Phone number" name="number" />
//                             <label></label>
//                         </div>
//                         <div className="infield">
//                             <input type="password" placeholder="Password" />
//                             <label></label>
//                         </div>
//                         <button className='btnpad'>Sign Up</button>
//                     </form>
//                 </div>
//                 <div className="form-container sign-in-container">
//                     <form action="#">
//                         <h1>Sign in</h1>
//                         {/* <div className="social-container">
//                             <a href="#" className="social"><i className="fab fa-facebook-f"></i></a>
//                             <a href="#" className="social"><i className="fab fa-google-plus-g"></i></a>
//                             <a href="#" className="social"><i className="fab fa-linkedin-in"></i></a>
//                         </div> */}
//                         {/* <span>or use your account</span> */}
//                         <div className="infield">
//                             <input type="number" placeholder="Phone number" name="number" />
//                             <label></label>
//                         </div>
//                         <div className="infield">
//                             <input type="password" placeholder="Password" />
//                             <label></label>
//                         </div>
//                         <a href="#" className="forgot">Forgot your password?</a>
//                         <button className='btnpad'>Sign In</button>
//                     </form>
//                 </div>
//                 <div className="overlay-container" id="overlayCon">
//                     <div className="overlay">
//                         <div className="overlay-panel overlay-left">
//                             <h1>Welcome Back!</h1>
//                             <p>To keep connected with us please login with your personal info</p>
//                             <button onClick={handleOverlayClick}>Sign In</button>
//                         </div>
//                         <div className="overlay-panel overlay-right">
//                             <h1>Hello, Friend!</h1>
//                             <p>Enter your personal details and start journey with us</p>
//                             <button onClick={handleOverlayClick}>Sign Up</button>
//                         </div>
//                     </div>
//                     <button id="overlayBtn" className="btnScaled" onClick={handleOverlayClick}></button>
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default Login;





import React, { useState } from 'react';
import './Login.css';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [isRightPanelActive, setIsRightPanelActive] = useState(false);
    const [name, setName] = useState("");
    const [signupPhone, setSignupPhone] = useState("");
    const [signupPassword, setSignupPassword] = useState("");
    const [loginPhone, setLoginPhone] = useState("");
    const [loginPassword, setLoginPassword] = useState("");

    const handleOverlayClick = () => {
        setIsRightPanelActive(!isRightPanelActive);
    };

    const handleSignUp = async (event) => {
        event.preventDefault();
        const payload = {
            name: name,
            phone_number: signupPhone,
            password: signupPassword
        };
    
        try {
            const response = await fetch("http://127.0.0.1:8000/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });
    
            if (!response.ok) {
                const errorData = await response.json();
                alert(`Signup failed: ${errorData.detail}`);
                return;
            }
    
            const data = await response.json();
            await localStorage
            alert("Signup successful!");
        } catch (error) {
            console.error("Error during signup:", error);
            alert("Signup failed: Network error or server is down.");
        }
    };
    
    
    const handleSignIn = async (event) => {
        event.preventDefault();
        try {
            const response = await fetch(`http://127.0.0.1:8000/login?phone_number=${loginPhone}&password=${loginPassword}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            });
    
            if (!response.ok) {
                const errorData = await response.json();
                alert(`Login failed: ${errorData.detail}`);
                return;
            }
    
            const data = await response.json();
            alert("Login successful!");
        } catch (error) {
            console.error("Error during login:", error);
            alert("Login failed: Network error or server is down.");
        }
    };
    
    return (
        <div className='loginSection'>
            <img src="https://i.imgur.com/wcGWHvx.png" className="square" alt="" />
            <div className={`container ${isRightPanelActive ? 'right-panel-active' : ''}`} id="container">
                <div className="form-container sign-up-container">
                    <form onSubmit={handleSignUp}>
                        <h1>Create Account</h1>
                        <div className="infield">
                            <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} required />
                            <label></label>
                        </div>
                        <div className="infield">
                            <input type="number" placeholder="Phone number" value={signupPhone} onChange={(e) => setSignupPhone(e.target.value)} required />
                            <label></label>
                        </div>
                        <div className="infield">
                            <input type="password" placeholder="Password" value={signupPassword} onChange={(e) => setSignupPassword(e.target.value)} required />
                            <label></label>
                        </div>
                        <button type="submit" className='btnpad'>Sign Up</button>
                    </form>
                </div>
                <div className="form-container sign-in-container">
                    <form onSubmit={handleSignIn}>
                        <h1>Sign in</h1>
                        <div className="infield">
                            <input type="number" placeholder="Phone number" value={loginPhone} onChange={(e) => setLoginPhone(e.target.value)} required />
                            <label></label>
                        </div>
                        <div className="infield">
                            <input type="password" placeholder="Password" value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)} required />
                            <label></label>
                        </div>
                        <a href="#" className="forgot">Forgot your password?</a>
                        <button type="submit" className='btnpad'>Sign In</button>
                    </form>
                </div>
                <div className="overlay-container" id="overlayCon">
                    <div className="overlay">
                        <div className="overlay-panel overlay-left">
                            <h1>Welcome Back!</h1>
                            <p>To keep connected with us please login with your personal info</p>
                            <button onClick={handleOverlayClick}>Sign In</button>
                        </div>
                        <div className="overlay-panel overlay-right">
                            <h1>Hello, Friend!</h1>
                            <p>Enter your personal details and start journey with us</p>
                            <button onClick={handleOverlayClick}>Sign Up</button>
                        </div>
                    </div>
                    <button id="overlayBtn" className="btnScaled" onClick={handleOverlayClick}></button>
                </div>
            </div>
        </div>
    );
};

export default Login;


