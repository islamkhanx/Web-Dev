import { Component } from '@angular/core';
import { Vacancy } from '../models/vacancy';
import { VacancyServiceService } from '../services/vacancy-service.service';
import { VacancyCardComponent } from "./vacancy-card/vacancy-card.component";

@Component({
  selector: 'app-vacancies',
  imports: [VacancyCardComponent],
  templateUrl: './vacancies.component.html',
  styleUrl: './vacancies.component.css'
})
export class VacanciesComponent {
  vacancies: Vacancy[] = [];
  
  constructor(private vacancyService: VacancyServiceService) {}

  ngOnInit(): void {
    this.loadVacancies();
  }

  loadVacancies(): void {
    this.vacancyService.getAllVacancies().subscribe(vacancies => {
      this.vacancies = vacancies;
    });
  }
  handleDeleteVacancy(id: number): void {
    this.vacancyService.deleteVacancy(id.toString()).subscribe(() => {
      this.vacancies = this.vacancies.filter(vacancy => vacancy.id !== id);
    });
  }
}
