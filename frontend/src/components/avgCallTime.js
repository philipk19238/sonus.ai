import * as React from 'react';
import Box from '@material-ui/core/Box';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import '../index.css';

require('typeface-dm-sans');

const card = (
    <React.Fragment>
      <CardContent style={{backgroundColor: "#FFFFFF"}}>
        <Typography style={{color: "#3200BD", fontSize: 24, fontWeight: 'bold'}}>
          avg. call time
        </Typography>
        <Divider style={{ background: '#3200BD' }} variant="middle" />
        <Typography style={{color: "#3200BD", fontSize: 24}}>
            <br/>
          10 minutes
        </Typography>
      </CardContent>
    </React.Fragment>
  );
  
  export default function OutlinedCard() {
    return (
        <div className = "cardPadder" > 
      <Box sx={{ maxWidth: 250}}>
        <Card className = "cardStyle" variant="outlined">{card} </Card>
      </Box>
      </div>
    );
  }