import { Component, Input, SimpleChanges } from '@angular/core';
import { MovieSearchService } from '../../services/movie-search-service';

@Component({
  selector: 'app-movie-service-stats',
  templateUrl: './movie-service-stats.component.html',
  styleUrl: './movie-service-stats.component.css'
})
export class MovieServiceStatsComponent {
    
  numberOfHits : number = 0;
  numberOfCacheHits : number = 0;

  @Input() log: string = '';
  
  constructor(private movieSearchService : MovieSearchService){

  }

  ngOnInit(){
    this.manageSubscriptions();
  }

  ngOnChanges(changes: SimpleChanges){
    console.log(changes);
  }

  manageSubscriptions(){
    this.movieSearchService.numberOfCacheHits$.subscribe(data => this.numberOfCacheHits = data );
    this.movieSearchService.numberOfHits$.subscribe(data => this.numberOfHits = data );

  }
}
