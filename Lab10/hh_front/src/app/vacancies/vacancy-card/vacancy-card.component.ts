import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Vacancy } from '../../models/vacancy';
import { RouterLink } from '@angular/router';
import { VacancyServiceService } from '../../services/vacancy-service.service';

@Component({
  selector: 'app-vacancy-card',
  imports: [RouterLink],
  templateUrl: './vacancy-card.component.html',
  styleUrl: './vacancy-card.component.css'
})
export class VacancyCardComponent {
  @Input() vacancy!: Vacancy;
  @Output() deleteVacancyEE = new EventEmitter<number>();

  deleteVacancy() {
    this.deleteVacancyEE.emit(this.vacancy.id);
  }
}
