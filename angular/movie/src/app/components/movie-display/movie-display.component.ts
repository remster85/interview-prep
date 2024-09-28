import { Component } from '@angular/core';
import { MovieSearchService } from '../../services/movie-search-service';
import { Movie } from '../../models/movie';
import { ColDef, GridReadyEvent } from 'ag-grid-community';

@Component({
  selector: 'app-movie-display',
  templateUrl: './movie-display.component.html',
  styleUrl: './movie-display.component.css'
})

export class MovieDisplayComponent {

  constructor(private movieSearchService : MovieSearchService){}

  rowData: Movie[] = [];

  // Column Definitions: Defines the columns to be displayed.
  columnDefs: ColDef[] = [
  { field: "title" },
  { field: "year" }
];
  
  ngOnInit(){
    this.refreshData();
  }

  refreshData(){
    this.movieSearchService.getAllMovies().subscribe( data => this.rowData = data);
  }

  onGridReady($params: GridReadyEvent<Movie>){
    this.refreshData();
  }
}
