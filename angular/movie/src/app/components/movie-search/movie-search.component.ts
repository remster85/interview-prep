import { Component } from '@angular/core';
import { MovieSearchService } from '../../services/movie-search-service';
import { Movie } from '../../models/movie';
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
  numberOfHits: number = 0;
  numberOfCacheHits: number = 0;

  ngOnInit(){
    this.manageSubscriptions();
  }

  manageSubscriptions(){
    this.movieSearchService.numberOfHits.subscribe( data => {
      this.numberOfHits = data;
    });
    this.movieSearchService.numberOfCacheHits.subscribe( data => {
      this.numberOfCacheHits = data;
    });
  }

  onKeyDown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      this.search();  // Call search() if Enter is pressed
    }
  }

  search(){
    let text = `Searching Movie ${this.movieSearchText}`;
    this.logs = text;

    this.movieSearchService.getMovies(this.movieSearchText).subscribe(
      (data : Movie[]) => {
        this.movieResponse = data;
        let lastSearch = this.movieSearchText;
        this.logs = `MovieSearchService has responded for your search ${lastSearch}`;
      }
    )
  }
}