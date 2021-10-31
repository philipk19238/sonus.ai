import React from 'react';
import ButtonAppBar from './Navbar';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import { Link } from 'react-router-dom';
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
  data: ['+18326438261', '+18237239162', '+15126178726', '+12813959637']
};

const NumberList = ({ phoneNumbers }) => {
  const classes = useStyles();

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'right',
        alignItems: 'right',
        height: '100vh',
        paddingLeft: '0%',
        paddingRight: '10%',
        paddingTop: '16%'
      }}
      className='font-loader'
    >
      <Grid className='numList' item xs={12}>
        {phoneNumbers.map(phoneNumber => {
          return (
            <Paper
              className={classes.paper}
              style={{
                marginBottom: '2.5%',
                boxShadow: '1px 1px 5px #3200BD'
              }}
            >
              <Link
                to={{ pathname: '/individual/' + phoneNumber }}
                style={{ textDecoration: 'none' }}
              >
                <h2 style={{ color: '#3200BD' }}>{phoneNumber}</h2>
              </Link>
            </Paper>
          );
        })}
      </Grid>
    </div>
  );
};
export default NumberList;
