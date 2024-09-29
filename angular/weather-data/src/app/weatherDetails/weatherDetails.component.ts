import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'weather-details',
  templateUrl: './weatherDetails.component.html',
  styleUrls: ['./weatherDetails.component.scss']
})

export class WeatherDetails implements OnInit {
  @Input() weatherData: data[];

  city: string = "";
  showNoResult: boolean = false;
  showData: boolean = false;
  matchedData: data | undefined;

  ngOnInit() {

  }

  onCityChange(city){
    console.log("on city change " + city);
    let matches = this.weatherData.filter(c => c.name.toLowerCase() == city.toLowerCase());
    if(matches.length > 0){
      this.showData = true;
      this.matchedData = matches[0];
      this.showNoResult = false;
    }else{
      this.showData = false;
      this.showNoResult = true;
    }
  }

}

interface data {
  name: string;
  temperature: string;
  wind: string;
  humidity: string;
}
