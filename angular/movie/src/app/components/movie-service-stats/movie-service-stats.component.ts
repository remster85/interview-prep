import { Component, Input, OnDestroy, SimpleChanges } from '@angular/core';
import { MovieSearchService } from '../../services/movie-search-service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-movie-service-stats',
  templateUrl: './movie-service-stats.component.html',
  styleUrl: './movie-service-stats.component.css'
})
export class MovieServiceStatsComponent  implements OnDestroy{
    
  numberOfHits : number = 0;
  numberOfCacheHits : number = 0;
  subscriptionCacheHits : Subscription;
  subscriptionHits : Subscription;

  @Input() log: string = '';
  
  constructor(private movieSearchService : MovieSearchService){
    this.subscriptionCacheHits = this.movieSearchService.numberOfCacheHits$.subscribe(data => this.numberOfCacheHits = data );
    this.subscriptionHits = this.movieSearchService.numberOfHits$.subscribe(data => this.numberOfHits = data );
  }

  ngOnDestroy(): void {
    this.subscriptionCacheHits.unsubscribe();
    this.subscriptionHits.unsubscribe();
    
  }

  ngOnInit(){

  }

  ngOnChanges(changes: SimpleChanges){
    console.log(changes);
  }

}
