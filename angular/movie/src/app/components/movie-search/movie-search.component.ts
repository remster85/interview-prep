import { Component } from '@angular/core';
import { MovieSearchService } from '../../services/movie-search-service';
import { Movie } from '../../models/movie';
import { LogService } from '../../services/log.service';
@Component({
  selector: 'app-movie-search',
  templateUrl: './movie-search.component.html',
  styleUrl: './movie-search.component.css'
})
export class MovieSearchComponent {

  constructor(private movieSearchService: MovieSearchService, private logService : LogService){}

  movieSearchText : string = "2024";
  movieResponse : Movie[]= []; 
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
    this.logService.log.next(text);

    this.movieSearchService.getMovies(this.movieSearchText).subscribe(
      (data : Movie[]) => {
        this.movieResponse = data;
        let lastSearch = this.movieSearchText;
        this.logService.log.next(`MovieSearchService has responded for your search ${lastSearch}`);
      }
    )
  }
}
