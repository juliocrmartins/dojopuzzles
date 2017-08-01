import React from 'react'
var ReactMarkdown = require('react-markdown');


const Problem = (props) => {
  if(!props.showingProblem) {
    return (<div></div>)
  }

  return (
    <div className='problem'>
      <h1>{props.showingProblem.title}</h1>
      <div className='problem-description'>
        <ReactMarkdown source={props.showingProblem.description} />
      </div>
    </div>
  )
}

export default Problem
