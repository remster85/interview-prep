import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MovieSearchComponent } from './components/movie-search/movie-search.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MovieAdminComponent } from './components/movie-admin/movie-admin.component';
import { LogsComponent } from './components/logs/logs.component';
import { MovieServiceStatsComponent } from './components/movie-service-stats/movie-service-stats.component';
import { MovieDisplayComponent } from './components/movie-display/movie-display.component';
import { AgGridAngular } from 'ag-grid-angular';

@NgModule({
  declarations: [
    AppComponent,
    MovieSearchComponent,
    MovieAdminComponent,
    LogsComponent,
    MovieServiceStatsComponent,
    MovieDisplayComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    AgGridAngular
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
