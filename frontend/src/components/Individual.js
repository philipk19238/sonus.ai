import React from 'react';
import ButtonAppBar from './Navbar';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

import '../index.css';
require('typeface-dm-sans');
const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary
  }
}));

const mockData = {
  phoneNumber: '+18329384589',
  averageLength: '76',
  averageSentiment: '5',
  data: [
    {
      length: 5,
      sentiment: 'happy',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e'
    },
    {
      length: 10,
      sentiment: 'mad',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e'
    },
    {
      length: 15,
      sentiment: 'sad',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e'
    },
    {
      length: 5,
      sentiment: 'neutral',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e'
    },
    {
      length: 5,
      sentiment: 'neutral',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e'
    }
  ]
};

const Individual = () => {
  const classes = useStyles();
  const startPlaying = src => {
    let audio = new Audio(src);
    audio.play();
  };
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        paddingLeft: '10%',
        paddingRight: '10%',
        paddingTop: '5%'
      }}
      className='font-loader'
    >
      <ButtonAppBar />
      <Grid container spacing={2}>
        <Grid item xs={4} style={{ paddingRight: '5%' }}>
          <Paper
            className={classes.paper}
            style={{
              height: '20%',
              boxShadow: '5px 5px 10px #3200BD',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center'
            }}
          >
            <Grid item xs={2}>
              <img src='https://img.icons8.com/material-sharp/50/000000/user.png' />
            </Grid>
            <Grid item xs={8}>
              <h2 style={{ color: '#3200BD' }}>{mockData.phoneNumber}</h2>
            </Grid>
          </Paper>
          <Paper
            className={classes.paper}
            style={{
              marginTop: '10%',
              height: '20%',
              boxShadow: '5px 5px 10px #3200BD',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center'
              // backgroundColor: '#F8DEF7'
            }}
          >
            <h2 style={{ color: '#3200BD' }}>
              average length: {mockData.averageLength}
            </h2>
          </Paper>
          <Paper
            className={classes.paper}
            style={{
              marginTop: '10%',
              height: '20%',
              boxShadow: '5px 5px 10px #3200BD',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center'
            }}
          >
            <h2 style={{ color: '#3200BD' }}>
              average sentiment: {mockData.averageSentiment}
            </h2>
          </Paper>
        </Grid>
        <Grid item xs={8}>
          {mockData.data.map(audioData => (
            <Paper
              className={classes.paper}
              style={{
                marginBottom: '2.5%',
                boxShadow: '1px 1px 5px #3200BD'
              }}
            >
              <Grid container spacing={8}>
                <Grid
                  item
                  xs={2}
                  style={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center'
                  }}
                >
                  <img
                    src='https://img.icons8.com/ios-glyphs/50/000000/circled-play.png'
                    onClick={() => startPlaying(mockData.file)}
                  ></img>
                </Grid>
                <Grid item xs={10}>
                  <h2 style={{ color: '#3200BD' }}>{mockData.phoneNumber}</h2>
                </Grid>
              </Grid>
            </Paper>
          ))}
        </Grid>
      </Grid>
    </div>
  );
};

export default Individual;
