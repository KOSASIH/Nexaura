import React, { useState, useEffect, useContext } from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { theme } from '../styles/theme';
import { GlobalStyle } from '../styles/global';
import { AppContext } from '../context/AppContext';
import { ConversationalInterface } from '../components/ConversationalInterface';
import { InsightsDashboard } from '../components/InsightsDashboard';
import { Login } from '../components/Login';
import { Register } from '../components/Register';
import { Profile } from '../components/Profile';
import { Navbar } from '../components/Navbar';
import { Footer } from '../components/Footer';
import { api } from '../api';
import { toast } from 'react-toastify';

const App = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const { dispatch } = useContext(AppContext);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      api.get('/api/auth/me')
        .then(response => response.data)
        .then(user => {
          setUser(user);
          dispatch({ type: 'SET_USER', user });
          setLoading(false);
        })
        .catch(error => {
          localStorage.removeItem('token');
          setUser(null);
          dispatch({ type: 'SET_USER', user: null });
          setLoading(false);
        });
    } else {
      setUser(null);
      dispatch({ type: 'SET_USER', user: null });
      setLoading(false);
    }
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <BrowserRouter>
        <Navbar user={user} />
        <Switch>
          <Route path="/" exact component={ConversationalInterface} />
          <Route path="/insights" component={InsightsDashboard} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/profile" component={Profile} />
          <Redirect to="/" />
        </Switch>
        <Footer />
      </BrowserRouter>
    </ThemeProvider>
  );
};

export default App;
