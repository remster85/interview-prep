import { Component } from '@angular/core';
import { Movie } from './models/movie';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'AMC';
  currentLog = 'ahah';

  newMovie(event : Movie){
      this.currentLog = `A new movie was added ! ${event.title}`;
  }
}
