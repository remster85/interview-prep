import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, of, Subject } from 'rxjs';
import { Movie } from '../models/movie';

@Injectable({
  providedIn: 'root'
})
export class MovieSearchService {

  private numberOfHitsSubject = new BehaviorSubject<number>(0);
  public numberOfHits$ = this.numberOfHitsSubject.asObservable(); // Observable variable
  

  private numberOfCacheHitsSubject = new BehaviorSubject<number>(0);
  public numberOfCacheHits$ = this.numberOfCacheHitsSubject.asObservable(); // Observable variable

  searchHistoryMap : Map<string,Movie[]>  = new Map();

  constructor() { 
  }

  data : Movie[]  = 
    [
      {  title: 'Back to the Future', year: 1985 },
      {  title: 'Armaggedon', year: 1993},
      {  title: 'The Great Gatsby', year: 2012 }
    ]
  
  getMovies(searchText: string) : Observable<Movie[]>{

    if(this.searchHistoryMap.has(searchText)){
      this.numberOfCacheHitsSubject.next(this.numberOfCacheHitsSubject.value + 1);
      return of(this.searchHistoryMap.get(searchText)!);
    }

    if(!this.searchHistoryMap.has(searchText))  this.searchHistoryMap.set(searchText, []);

    let searchYear = Number(searchText);

    console.log("Getting Movies");

    let response = this.data.filter(m => m.year == searchYear);
    this.searchHistoryMap.set(searchText, response);
    this.numberOfHitsSubject.next(this.numberOfHitsSubject.value  + 1);
    return of(response); 
  }
  
    
  addMovie(newMovie: Movie){
    this.searchHistoryMap.delete(String(newMovie.year));
    this.data.push(newMovie); 
  }
}


