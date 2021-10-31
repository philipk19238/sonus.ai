import React from 'react';
import Home from './components/Home';
import Visualizer from './components/Visualizer';
import {
    BrowserRouter,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import './index.css';

require('typeface-dm-sans');

function App() {
return (
    <Switch>
     <Route exact path="/" component={Home} />
     <Route path="/visualizer" component={Visualizer} />
   </Switch>
);}
export default App;