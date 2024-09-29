import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'temperature-converter',
  templateUrl: './temperatureConverter.component.html',
  styleUrls: ['./temperatureConverter.component.scss']
})

export class TemperatureConverter implements OnInit {

  celsiusTemp : number | any;
  fahrenheitTemp : number | any;

  ngOnInit() {
    // C = (F − 32) × 5/9
    // F = C*9/5 + 32
  }

  onCelsiusChange(celsius : number){
    this.fahrenheitTemp  = (celsius) *9/5 + 32;
  }

  onFahrenheitChange(fahrenheit : number){
    this.celsiusTemp  = (fahrenheit - 32) * 5/9;
  }


}
