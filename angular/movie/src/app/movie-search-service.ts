import { Injectable } from '@angular/core';
import { Observable, of, Subject } from 'rxjs';
import { Movie } from './movie';

@Injectable({
  providedIn: 'root'
})
export class MovieSearchService {

  numberOfHitsStore_ : number = 0 ;
  numberOfHits : Subject<number> = new Subject();

  constructor() { 
    this.numberOfHits.next(this.numberOfHitsStore_);
  }

  data : Movie[]  = 
    [
      {  title: 'Back to the Future', year: 1985 },
      {  title: 'Armaggedon', year: 1993},
      {  title: 'The Great Gatsby', year: 2012 }
    ]
  
  getMovies(searchText: string) : Observable<Movie[]>{
    let searchYear = Number(searchText);
    console.log("Getting Movies");
    this.numberOfHits.next(this.numberOfHitsStore_++);
    return of(this.data.filter(m => m.year == searchYear)); 
  }
  
}
