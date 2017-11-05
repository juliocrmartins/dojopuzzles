import React, { Component } from 'react'
import './App.css'
import axios from 'axios'

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
    axios.get('http://api.dojopuzzles.com/problems/random')
         .then(response => {
            this.setState({
              showingProblem: {
                title: response.data.title,
                description: response.data.description,
              }
          })
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
