import React, { useState } from 'react';

function Slides({ slides }) {
    const [slideNumber, setSlideNumber] = useState(0);
    const [isPrevButtonDisabled, setIsPrevButtonDisabled] = useState(true);
    const [isNextButtonDisabled, setIsNextButtonDisabled] = useState(false);
    const [isRestartButtonDisabled, setIsRestartButtonDisabled] = useState(true);

    function updateButtonStates(newSlideNumber) {
        setIsPrevButtonDisabled(newSlideNumber === 0);
        setIsNextButtonDisabled(newSlideNumber === slides.length - 1);
        setIsRestartButtonDisabled(newSlideNumber === 0);
    }

    function goPrev() {
        if (slideNumber > 0) {
            const newSlideNumber = slideNumber - 1;
            setSlideNumber(newSlideNumber);
            updateButtonStates(newSlideNumber);
        }
    }

    function goNext() {
        if (slideNumber < slides.length - 1) {
            const newSlideNumber = slideNumber + 1;
            setSlideNumber(newSlideNumber);
            updateButtonStates(newSlideNumber);
        }
    }

    function restart() {
        setSlideNumber(0);
        updateButtonStates(0);
    }

    return (
        <div>
            <div id="navigation" className="text-center">
                <button
                    data-testid="button-restart"
                    className="small outlined"
                    disabled={isRestartButtonDisabled}
                    onClick={restart}
                >
                    Restart
                </button>
                <button
                    data-testid="button-prev"
                    className="small"
                    onClick={goPrev}
                    disabled={isPrevButtonDisabled}
                >
                    Prev
                </button>
                <button
                    data-testid="button-next"
                    className="small"
                    onClick={goNext}
                    disabled={isNextButtonDisabled}
                >
                    Next
                </button>
            </div>
            <div id="slide" className="card text-center">
                <h1 data-testid="title">{slides[slideNumber].title}</h1>
                <p data-testid="text">{slides[slideNumber].text}</p>
            </div>
        </div>
    );
}

export default Slides;
