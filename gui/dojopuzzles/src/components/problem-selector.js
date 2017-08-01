import React from 'react'


const ProblemSelector = (props) => {
  if(!props.showingProblem) {
    return (
      <div className="jumbotron">
        <p className="lead">Um Coding Dojo é um encontro onde um grupo de programadores se reúne para treinar técnicas e metodologias de desenvolvimento de software através da solução de um pequeno desafio de programação utilizando boas práticas de programação.</p>
        <p><span
          onClick={props.onFindProblemClick}
          className="btn btn-lg btn-success"
          role="button">Encontre um problema</span></p>
      </div>
    )
  } else if (!props.problemSelected) {
    return (
      <div>
        <ul className="nav nav-pills nav-fill">
          <li className="nav-item">
            <span
              onClick={props.onProblemSelectedClick}
              className="btn btn-success"
              role="button">Gostei! Vou usar este!</span>
          </li>
          <li className="nav-item">
            <span
              onClick={props.onFindProblemClick}
              className="btn btn-danger"
              role="button">Mostre-me outro problema!</span>
          </li>
        </ul>
      </div>
    )   
  } else {
    return <div />
  }

}

export default ProblemSelector