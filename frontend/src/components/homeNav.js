import React from "react";
import Button from '@material-ui/core/Button';
import '../index.css';
   import {Link } from "react-router-dom";

    function homeNav() {

        return (
            <Link to="/" style={{textDecoration: 'none'}}>
            <Button className = "btn2" style={{ color: '#3200BD', fontSize: 20, fontWeight: 'bold', textTransform: "none",  backgroundColor: 'transparent' }}>home</Button>
            </Link>
        );

    }

    export default homeNav;