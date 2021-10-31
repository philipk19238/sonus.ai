import React from 'react';
import ButtonAppBar from './Navbar';
import '../index.css';

const Visualizer = () => {
    return (
        <html>
        <ButtonAppBar/>
        <body >
        <div className = "font-loader"
                    style={{
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center"
                    }}
                >     
                    </div>
                    </body>
                    </html>

    );
}
 
export default Visualizer;