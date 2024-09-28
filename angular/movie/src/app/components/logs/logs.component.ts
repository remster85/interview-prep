import { Component } from '@angular/core';
import { LogService } from '../../services/log.service';

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrl: './logs.component.css'
})
export class LogsComponent {

  logs: string = "";

  constructor(private logService : LogService){}

  ngOnInit(){
    this.manageSubcriptions();
  }

  manageSubcriptions(){
    this.logService.log.subscribe( data => this.logs = data);
  }

}
