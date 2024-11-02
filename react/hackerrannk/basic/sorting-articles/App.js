import React, { useState } from 'react';
import './App.css';
import 'h8k-components';

import Articles from './components/Articles';

const title = "Sorting Articles";

function App({articles}) {

    const [articlesToDisplay, setArticlesToDisplay] = useState([...articles].sort((a,b)=> b.upvotes - a.upvotes  ));

    function sortByUpVotes(){
        let sortedArticles = [...articles].sort((a,b)=> b.upvotes - a.upvotes  );
        setArticlesToDisplay(sortedArticles);
    }

    function sortByMostRecent(){
        let sortedArticles = [...articles].sort((a, b) => new Date(b.date) - new Date(a.date));
        setArticlesToDisplay(sortedArticles);
    }

    return (
        <div className="App">
            <h8k-navbar header={title}></h8k-navbar>
            <div className="layout-row align-items-center justify-content-center my-20 navigation">
                <label className="form-hint mb-0 text-uppercase font-weight-light">Sort By</label>
                <button data-testid="most-upvoted-link" className="small" onClick={sortByUpVotes}>Most Upvoted</button>
                <button data-testid="most-recent-link" className="small"  onClick={sortByMostRecent}>Most Recent</button>
            </div>
            <Articles articles={articlesToDisplay}/>
        </div>
    );

}

export default App;
