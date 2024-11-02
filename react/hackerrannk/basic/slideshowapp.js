import React, { useState } from 'react';

function Slides({slides}) {

    const[slideNumber, setSlideNumber] = useState(0);
    const[isPrevButtonDisabled, setIsPrevButtonDisabled] = useState(true);
    const[isNextButtonDisabled, setIsNextButtonDisabled] = useState(false);

    function goPrev(){
        setSlideNumber(slideNumber-1);
        if(slideNumber == 1) setIsPrevButtonDisabled(true);
        
    }

    function goNext(){
        setSlideNumber(slideNumber+1);
        if(slideNumber == slides.length-2) setIsNextButtonDisabled(true);   
        setIsPrevButtonDisabled(false);   
    }

    function restart(){
        setSlideNumber(0);
        setIsPrevButtonDisabled(true);
        setIsNextButtonDisabled(false);
    }


    return (
        <div>
            <div id="navigation" className="text-center">
                <button data-testid="button-restart" className="small outlined"  onClick={restart}>Restart</button>
                <button data-testid="button-prev" className="small" onClick={goPrev} disabled={isPrevButtonDisabled}>Prev</button>
                <button data-testid="button-next" className="small" onClick={goNext}disabled={isNextButtonDisabled}>Next</button>
            </div>
            <div id="slide" className="card text-center">
                <h1 data-testid="title">{slides[slideNumber].title}</h1>
                <p data-testid="text">{slides[slideNumber].text}</p>
            </div>
        </div>
    );

}

export default Slides;
