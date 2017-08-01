import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import Footer from './components/footer'
import Header from './components/header'
import Problem from './components/problem'
import ProblemSelector from './components/problem-selector'

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      problemSelected: null,
      showingProblem: null,
    }
  }

  onFindProblemClick = () => {
    // TODO get random problem from API

    this.setState({
      showingProblem: {
        title: 'Problem Title ' + Math.random(),
        description: '### This is a header\n\nAnd this is a paragraph',
      }
    })
  }

  onProblemSelectedClick = () => {
    this.setState({
      problemSelected: this.state.showingProblem
    })
  }

  render() {
    return (
      <div className="container">
        <Header />
        
        <ProblemSelector
          onProblemSelectedClick={this.onProblemSelectedClick}
          onFindProblemClick={this.onFindProblemClick}
          showingProblem={this.state.showingProblem}
          problemSelected={this.state.problemSelected} />

        <Problem
          showingProblem={this.state.showingProblem} />

        <Footer />
      </div>
    );
  }
}

export default App;
