import React from 'react';
import ButtonAppBar from './Navbar';
import GettingStarted from "./gettingstarted";
import '../index.css';
import demo from '../images/sonusDemo.jpeg'


require('typeface-dm-sans');


const Home = () =>  {
return (
    <html>
    <div className = "font-loader">
    <ButtonAppBar/>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <br></br>


    <body>
    <img className = 'demo' src={demo} width="720px" height="450px" alt="sonus demo" align = "right"/>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "left",
                alignItems: "left",
                }}
            >
    <h1 align = "left" style={{ color: '#3200BD', fontSize: 84, fontWeight: 'bold' }}>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;what can sonus<br></br><span style={{ color: '#FF97FF', fontSize: 84, fontWeight: 'bold'}}>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;do for you? </span></h1>
    </div>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "left",
                alignItems: "left"
                }}
            >
    <p style={{ color: '#B8B8B8', fontSize: 24}} align="left">
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style={{ color: '#3200BD', fontSize: 24, fontWeight: 'bold' }} >sonus </span>is a customer success management<br></br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tool that allows you to prioritize your most <br></br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;important clients.<br></br>
</p>
    </div>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "left",
                alignItems: "left"
                }}
            >
    <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <GettingStarted/></p>
    </div>
    <br></br>
    <br></br>
    <br></br>
    <div className = "font-loader"
    style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}
    >
    </div>
    </body>
    </div>
    </html>
);
}
export default Home;