import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieServiceStatsComponent } from './movie-service-stats.component';

describe('MovieServiceStatsComponent', () => {
  let component: MovieServiceStatsComponent;
  let fixture: ComponentFixture<MovieServiceStatsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MovieServiceStatsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MovieServiceStatsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
