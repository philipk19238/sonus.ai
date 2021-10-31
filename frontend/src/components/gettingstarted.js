import React from "react";
import Button from '@material-ui/core/Button';
import '../index.css';
import {Link } from "react-router-dom";

    function gettingstarted() {

        return (
            <Link to="/visualizer" style={{textDecoration: 'none'}}>
            <Button class = "btn" style={{color: '#FFFFFF', fontSize: 20, fontWeight: 'bold', textDecoration: 'none', textTransform: "none"}}> get started </Button>
            </Link>
        );

    }

    export default gettingstarted;