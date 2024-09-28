import { EventEmitter, Injectable, Output } from '@angular/core';
import { Observable, of, Subject } from 'rxjs';
import { Movie } from '../models/movie';

@Injectable({
  providedIn: 'root'
})
export class MovieSearchService {

  numberOfHitsStore_ : number = 0 ;
  numberOfHits : Subject<number> = new Subject();

  numberOfCacheHitsStore_ : number = 0 ;
  numberOfCacheHits : Subject<number> = new Subject();

  searchHistoryMap : Map<string,Movie[]>  = new Map();

  @Output() newMovieEvent: EventEmitter<Movie> = new EventEmitter();

  constructor() { 
    this.numberOfHits.next(this.numberOfHitsStore_);
    this.numberOfCacheHits.next(this.numberOfCacheHitsStore_);
  }

  data : Movie[]  = 
    [
      {  title: 'Back to the Future', year: 1985 },
      {  title: 'Armaggedon', year: 1993},
      {  title: 'The Great Gatsby', year: 2012 }
    ]
  
  getMovies(searchText: string) : Observable<Movie[]>{

    if(this.searchHistoryMap.has(searchText)){
      this.numberOfCacheHits.next(this.numberOfCacheHitsStore_++);
      return of(this.searchHistoryMap.get(searchText)!);
    }

    if(!this.searchHistoryMap.has(searchText))  this.searchHistoryMap.set(searchText, []);

    let searchYear = Number(searchText);

    console.log("Getting Movies");

    let response = this.data.filter(m => m.year == searchYear);
    this.searchHistoryMap.set(searchText, response);

    this.numberOfHits.next(this.numberOfHitsStore_++);
    return of(response); 
  }
  
    
  addMovie(newMovie: Movie){
    this.searchHistoryMap.delete(String(newMovie.year));
    this.newMovieEvent.emit(newMovie);
    this.data.push(newMovie); 
  }
}


