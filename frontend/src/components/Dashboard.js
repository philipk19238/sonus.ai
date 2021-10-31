import React from 'react';
import ButtonAppBar from './Navbar';
import '../index.css';
import AvgCallTime from './avgCallTime'
import AvgSentiment from './avgSentiment'
import TotalCalls from './totalCalls'
import NumberList from './phoneNumberList'
import { Grid } from '@material-ui/core';
require('typeface-dm-sans');

const Dashboard = () => {
    return (
        <html>
        <ButtonAppBar/>
        <Grid container spacing={2}>
        <Grid item xs={4} >
        <AvgCallTime/>    
        <TotalCalls/>
        <AvgSentiment/>      

 

</Grid>
<Grid className = "numList" item xs={8}>
<NumberList/>                

</Grid>
</Grid>
                    </html>
    );
}
 
export default Dashboard;