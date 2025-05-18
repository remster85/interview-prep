import './App.css';
import { useState } from 'react';

function App() {

  const [userInput, setUserInput] = useState("")
  return (
    <div>
      <h2>Test</h2>
      <div>
        <label htmlFor="input">Enter text:</label>
        <input
          id="input"
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
        <p>You typed: {userInput}</p>
      </div>
    </div>
  );
}
export default App;
