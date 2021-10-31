import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import logo from '../images/sonus_title.png'
import HomeNav from './homeNav'
import '../index.css';

require('typeface-dm-sans');


const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    menuButton: {
        marginRight: theme.spacing(2),
        color: 'white'
    },
    title: {
        flexGrow: 1,
        color: 'white'
    },
    appBarSolid: {
        backgroundColor: 'rgb(255, 255, 255)'
    },
    appBarTransparent: {
        backgroundColor: 'rgba(255, 255, 255,0.5)'
    },
    customizeToolbar: {
        minHeight: 100
      }
}));

export default function ButtonAppBar() {
    const classes = useStyles();
 
    const [navBackground, setNavBackground] = useState('appBarSolid')
    const navRef = React.useRef()
    navRef.current = navBackground
    useEffect(() => {
        const handleScroll = () => {
            const show = window.scrollY > 20
            if (show) {
                setNavBackground('appBarTransparent')
            } else {
                setNavBackground('appBarSolid')
            }
        }
        document.addEventListener('scroll', handleScroll)
        return () => {
            document.removeEventListener('scroll', handleScroll)
        }
    }, [])


    return (
        <div className={classes.root}>
            <AppBar position="fixed" className={classes[navRef.current]} elevation={0}>
                <Toolbar className={classes.customizeToolbar}>
                    <Box display='flex' flexGrow={1}>
                    <img src={logo} alt="logo" className={classes.logo} width="271px" height="134px" />
                    </Box>
                    <HomeNav/>
                    <a href="https://github.com/philipk19238/sonus.ai/" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}><Button style={{ color: '#3200BD', fontSize: 20, fontWeight: 'bold', textTransform: "none",  backgroundColor: 'transparent'   }}>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;documentation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Button></a>
                </Toolbar>
            </AppBar>
        </div>
    );
}