import React from "react";
import Button from '@material-ui/core/Button';
import '../index.css';
import {Link } from "react-router-dom";

    function gettingstarted() {

        return (
            <Link to="/dashboard" style={{textDecoration: 'none'}}>
            <Button class = "btn" style={{color: '#FFFFFF', fontSize: 20, fontWeight: 'bold', textDecoration: 'none', textTransform: "none"}}> go to dashboard </Button>
            </Link>
        );

    }

    export default gettingstarted;