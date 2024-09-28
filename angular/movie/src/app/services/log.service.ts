import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LogService {

  logStore : string = "" ;
  log : BehaviorSubject<string> = new BehaviorSubject("");

  constructor() {
    this.log.next(this.logStore);
   }
}
