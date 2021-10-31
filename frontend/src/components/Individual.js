import React, { useEffect, useState } from 'react';
import ButtonAppBar from './Navbar';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { Howl } from 'howler';
import { useParams } from 'react-router-dom';

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
  phoneNumber: '+1 832-938-4589',
  averageLength: '9.4',
  averageSentiment: 'happy',
  data: [
    {
      length: 6,
      sentiment: 'happy',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e.mp3'
    },
    {
      length: 10,
      sentiment: 'angry',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC589ef5b0e38c799a4652ad18c0a2bb39/Recordings/REc6dbf04e2b6191d41e1d9dda6c00aa79.mp3'
    },
    {
      length: 15,
      sentiment: 'happy',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e.mp3'
    },
    {
      length: 11,
      sentiment: 'happy',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e.mp3'
    },
    {
      length: 5,
      sentiment: 'neutral',
      file:
        'https://api.twilio.com/2010-04-01/Accounts/AC8053fa3bf118f0bb033d17bd27e5f19c/Recordings/RE12bfbf3a297130d1348aebc4c1edc91e.mp3'
    }
  ]
};

const Individual = () => {
  const classes = useStyles();
  const { id } = useParams();
  const [data, setData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    console.log(`This is the id ${id}`);
  }, [id]);
  const soundPlay = src => {
    const sound = new Howl({
      src: [src]
    });
    sound.play();
  };
  useEffect(() => {
    setIsLoading(true);
    fetch('http://localhost:5000/api/search/' + id)
      .then(res => res.json())
      .then(result => {
        console.log(result);
        setData(result.data);
        setIsLoading(false);
      });
  }, [id]);
  if (!isLoading) {
    return (
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh',
          paddingLeft: '10%',
          paddingRight: '10%',
          paddingTop: '1%'
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
                boxShadow: '1px 1px 5px #3200BD',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center'
              }}
            >
              <Grid item xs={2}>
                <img src='https://img.icons8.com/material-sharp/50/000000/user.png' />
              </Grid>
              <Grid item xs={8}>
                <h3 style={{ color: '#3200BD' }}>{data.phone_number}</h3>
              </Grid>
            </Paper>
            <Paper
              className={classes.paper}
              style={{
                marginTop: '10%',
                height: '20%',
                boxShadow: '1px 1px 5px #3200BD',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center'
              }}
            >
              <h3 style={{ color: '#3200BD' }}>
                avg call time: {data.average_length} seconds
              </h3>
            </Paper>
            <Paper
              className={classes.paper}
              style={{
                marginTop: '10%',
                height: '20%',
                boxShadow: '1px 1px 5px #3200BD',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center'
              }}
            >
              <h3 style={{ color: '#3200BD' }}>
                avg sentiment: {data.average_sentiment}
              </h3>
            </Paper>
          </Grid>
          <Grid item xs={8}>
            {data.calls.map(audioData => (
              <Paper
                className={classes.paper}
                style={{
                  marginBottom: '2.5%',
                  boxShadow: '1px 1px 5px #3200BD'
                }}
              >
                <Grid container spacing={2}>
                  <Grid
                    item
                    xs={6}
                    style={{
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'center'
                    }}
                  >
                    <img
                      className='play'
                      src='https://img.icons8.com/ios-glyphs/50/000000/circled-play.png'
                      onClick={() => {
                        soundPlay(audioData.link + '.mp3');
                      }}
                      style={{ paddingRight: '5%' }}
                    />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                    <img src='https://img.icons8.com/windows/32/000000/audio-wave--v2.png' />
                  </Grid>
                  <Grid
                    item
                    xs={4}
                    style={{ textAlign: 'left', paddingLeft: '5%' }}
                  >
                    <h3 style={{ color: '#3200BD' }}>
                      sentiment: {audioData.sentiment}
                    </h3>
                  </Grid>
                </Grid>
              </Paper>
            ))}
          </Grid>
        </Grid>
      </div>
    );
  } else {
    return <div>Loading...</div>;
  }
};

export default Individual;
