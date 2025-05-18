import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
    // add other components here
  ],
  imports: [
    BrowserModule,
    FormsModule,          // For template-driven forms
    ReactiveFormsModule,  // For reactive forms
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
