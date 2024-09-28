import { Component } from '@angular/core';
import { MovieSearchService } from '../movie-search-service';
import { Movie } from '../movie';
@Component({
  selector: 'app-movie-search',
  templateUrl: './movie-search.component.html',
  styleUrl: './movie-search.component.css'
})
export class MovieSearchComponent {

  constructor(private movieSearchService: MovieSearchService){}

  movieSearchText : string = "2024";
  movieResponse : Movie[]= []; 
  logs: string = "";
  searchHistoryHits: number = 0;
  searchHistoryMap : Map<string,Movie[]>  = new Map();

  ngOnInit(){
    this.manageSubscriptions();
  }

  manageSubscriptions(){
    // this.movieSearchService.numberOfHits.subscribe( data => {
    //   this.searchHistoryHits = data;
    // });
  }


  onKeyDown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      this.search();  // Call search() if Enter is pressed
    }
  }

  search(){
    let text = `Searching Movie ${this.movieSearchText}`;
    let searchedText = this.movieSearchText;
    this.logs = text;

    if(this.searchHistoryMap.has(searchedText)){
      this.searchHistoryHits++;
      this.logs = `Cache was used to respond to your search ${searchedText}`;
      this.movieResponse = this.searchHistoryMap.get(searchedText)!;
      return;
    }

    this.movieSearchService.getMovies(this.movieSearchText).subscribe(
      (data : Movie[]) => {
        this.movieResponse = data;
        this.searchHistoryHits++;

        if(!this.searchHistoryMap.has(searchedText))  this.searchHistoryMap.set(searchedText, []);
        this.searchHistoryMap.set(searchedText, data);

        let lastSearch = this.movieSearchText;
        this.logs = `MovieSearchService has responded for your search ${lastSearch}`;
      }
    )
  }
}
