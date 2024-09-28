import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MovieSearchComponent } from './components/movie-search/movie-search.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MovieAdminComponent } from './components/movie-admin/movie-admin.component';

@NgModule({
  declarations: [
    AppComponent,
    MovieSearchComponent,
    MovieAdminComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
