import React, { useEffect, useState } from 'react';
import ButtonAppBar from './Navbar';
import '../index.css';
import AvgCallTime from './avgCallTime';
import AvgSentiment from './avgSentiment';
import TotalCalls from './totalCalls';
import NumberList from './phoneNumberList';
import { Grid } from '@material-ui/core';
require('typeface-dm-sans');

const Dashboard = () => {
  const [data, setData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    setIsLoading(true);
    fetch('http://localhost:5000/api/search/all')
      .then(res => res.json())
      .then(result => {
        console.log(result);
        setData(result.data);
        setIsLoading(false);
      });
  }, []);
  if (!isLoading) {
    return (
      <html>
        <ButtonAppBar />
        <Grid container spacing={2}>
          <Grid item xs={4}>
            <AvgCallTime avgTime={data.average_time} />
            <TotalCalls totalCall={data.total_calls} />
            <AvgSentiment averageSentiment={data.average_sentiment} />
          </Grid>
          <Grid className='numList' item xs={8}>
            <NumberList phoneNumbers={data.phone_numbers} />
          </Grid>
        </Grid>
      </html>
    );
  } else {
    return <div>Loading ...</div>;
  }
};

export default Dashboard;
