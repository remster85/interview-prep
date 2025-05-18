import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent implements OnInit, OnDestroy {
  fxRate = 1.1;               // live FX rate, updates every 3 seconds
  overrideFxRate: number | null = null;  // overridden FX rate (null means no override)
  inputCurrency: 'EUR' | 'USD' = 'EUR';  // input currency type
  amount = 1;                 // user input amount
  converted = 1.1;            // converted value shown
  private intervalId: any;

  ngOnInit() {
    this.startFxRateUpdates();
  }

  ngOnDestroy() {
    clearInterval(this.intervalId);
  }

  startFxRateUpdates() {
    this.intervalId = setInterval(() => {
      const change = (Math.random() * 0.1) - 0.05;  // random between -0.05 and +0.05
      this.fxRate = +(this.fxRate + change).toFixed(4);

      // Check override: disable if difference > 2%
      if (
        this.overrideFxRate !== null &&
        Math.abs((this.overrideFxRate - this.fxRate) / this.fxRate) > 0.02
      ) {
        this.overrideFxRate = null;
      }

      this.updateConvertedValue();
    }, 3000);
  }

  getEffectiveFxRate(): number {
    return this.overrideFxRate !== null ? this.overrideFxRate : this.fxRate;
  }

  onOverrideRateChange(value: number) {
    if (isNaN(value) || value <= 0) {
      this.overrideFxRate = null;
    } else {
      this.overrideFxRate = +value.toFixed(4);
    }
    this.updateConvertedValue();
  }

  onCurrencySwitch() {
    // When switching currency, swap amount and converted values for continuity
    this.amount = this.converted;
    this.updateConvertedValue();
  }

  onAmountChange(value: number) {
    if (isNaN(value) || value < 0) {
      this.converted = 0;
      return;
    }
    this.amount = value;
    this.updateConvertedValue();
  }

  updateConvertedValue() {
    const rate = this.getEffectiveFxRate();
    if (this.inputCurrency === 'EUR') {
      this.converted = +(this.amount * rate);
    } else {
      // input is USD, convert back to EUR
      this.converted = +(this.amount / rate);
    }
  }
}
