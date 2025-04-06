import React from 'react'
import logo from './logo.svg'
import './App.css'

// 새로 추가한 데이터 확인하기
import * as D from './data'

function App() {
  // 시작

  return (
    <div>
      {D.randomName()},{D.randomJobTitle()}
      <img src={D.randomAvatar()} height="50" />
      <img src={D.randomImage()} height="300" />
    </div>
  )
  // 끝

  //  return <h1>check!</h1>
  /*  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
  */
}

export default App
