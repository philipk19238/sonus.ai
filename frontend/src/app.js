import React from 'react';
import Home from './components/Home';
import Dashboard from './components/Dashboard';
import Individual from './components/Individual';
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
     <Route path="/dashboard" component={Dashboard} />
     <Route path='/individual/:id' component={Individual} />
   </Switch>
);}
export default App;
