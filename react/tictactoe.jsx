import { useState } from "react";

export default function Game() {
  return (
    <>
      <Board></Board>
    </>
  );


function Square({value, onSquareClick}) {
  return <button className="square" onClick={onSquareClick}>{value}</button>;
}


function Board() {

  const[squares, setSquares] = useState(Array(9).fill(null));
  const[isPlayerX, setIsPlayerX] = useState(true);
  const winner = isGameOverCheck() ? "We have a winner " : "Game in Progress";

  function isGameOverCheck(){
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];

    for(let i=0; i<8; i++){
      if(squares[lines[i][0]]  && squares[lines[i][0]] == squares[lines[i][1]] &&  squares[lines[i][1]] == squares[lines[i][2]]) return true;
    }

    return false;
  }

  function handleClick(i){
    const nextSquares = squares.slice();

    if(nextSquares[i] != null || isGameOverCheck()) return;

    nextSquares[i] = isPlayerX ? "X" : "O";
    setIsPlayerX(!isPlayerX);
    setSquares(nextSquares);

  }

  return (
    <> {winner}
      <div className="board-row">
          <Square onSquareClick={() => handleClick(0)} value={squares[0]}></Square>
          <Square onSquareClick={() => handleClick(1)} value={squares[1]} ></Square>
          <Square onSquareClick={() => handleClick(2)} value={squares[2]}></Square>
      </div>
      <div className="board-row">
        <Square onSquareClick={() => handleClick(3)} value={squares[3]}></Square>
        <Square onSquareClick={() => handleClick(4)} value={squares[4]}></Square>
        <Square onSquareClick={() => handleClick(5)} value={squares[5]}></Square>
      </div>
      <div className="board-row">
        <Square onSquareClick={() => handleClick(6)} value={squares[6]}></Square>
        <Square onSquareClick={() => handleClick(7)} value={squares[7]}></Square>
        <Square onSquareClick={() => handleClick(8)} value={squares[8]}></Square>
      </div>
    </>
  );
}

}
