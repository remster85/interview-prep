import { Component, EventEmitter, Output } from '@angular/core';
import { MovieSearchService } from '../../services/movie-search-service';
import { FormControl, FormGroup } from '@angular/forms';
import { Movie } from '../../models/movie';

@Component({
  selector: 'app-movie-admin',
  templateUrl: './movie-admin.component.html',
  styleUrl: './movie-admin.component.css'
})
export class MovieAdminComponent {


  @Output() newMovieEvent: EventEmitter<Movie> = new EventEmitter();
  
  constructor(private movieSearchService : MovieSearchService){
    this.initForm();
  }

  titleControl: FormControl<any> | undefined;
  yearControl:  FormControl<any> | undefined;
  movieForm: FormGroup<any> | undefined;


  initForm(){
    this.titleControl = new FormControl('');
    this.yearControl = new FormControl('');
    this.movieForm = new FormGroup({
        title: this.titleControl , 
        year: this.yearControl
      }
    );
  }

  addMovie(){
    console.log("form submitted");
    let movie = this.formToMovie();
    this.movieSearchService.addMovie(movie);
    this.newMovieEvent.emit(movie);

  }

  formToMovie() : Movie{
     return   {
      title: this.titleControl?.value,
      year: this.yearControl?.value
    };
  }

}
