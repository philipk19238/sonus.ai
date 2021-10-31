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
    <body className = "spacer">
    <img className = 'demo' src={demo} width="45%" height="25%" alt="sonus demo" align = "right"/>
    <div className = "font-loader" 
                style={{
                display: "flex",
                justifyContent: "left",
                alignItems: "left",
                }}
            >
    <h1 className = "hdr" align = "left" style={{ color: '#3200BD', fontSize: 84, fontWeight: 'bold' }}>what can sonus<br></br><span style={{ color: '#FF97FF', fontSize: 84, fontWeight: 'bold'}}>do for you? </span></h1>
    </div>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "left",
                alignItems: "left"
                }}
            >
    <p className = "hdr" align = "left" style={{ color: '#B8B8B8', fontSize: 24}}>
    <span style={{ color: '#3200BD', fontSize: 24, fontWeight: 'bold' }} >sonus </span>is a customer success management<br></br>
    tool that allows you to prioritize your most <br></br>important clients.<br></br>
</p>
    </div>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "left",
                alignItems: "left"
                }}
            >
    <p className = "hdr" align = "left">
      <GettingStarted/></p>
    </div>
    </body>
    </div>
    </html>
);
}
export default Home;