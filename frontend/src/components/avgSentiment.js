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
const sentimentcard = (
    <React.Fragment>
      <CardContent style={{backgroundColor: "#FFFFFF"}}>
        <Typography style={{color: "#3200BD", fontSize: 24, fontWeight: 'bold'}}>
          avg. sentiment
        </Typography>
        <Divider style={{ background: '#3200BD' }} variant="middle" />
        <Typography style={{color: "#3200BD", fontSize: 24}}>
            <br/>
          happy
        </Typography>
      </CardContent>
    </React.Fragment>
  );
  
  export default function SentimentCard() {
    return (
        <div className = "nextCard" > 
      <Box sx={{maxWidth: 250}}>
        <Card className = "cardStyle" variant="outlined">{sentimentcard} </Card>
      </Box>
      </div>
    );
  }