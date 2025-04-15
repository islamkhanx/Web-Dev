import { Component } from '@angular/core';

import { Vacancy } from '../../models/vacancy';
import { VacancyCardComponent } from "../../vacancies/vacancy-card/vacancy-card.component";
import { CompanyServiceService } from '../../services/company-service.service';
import { ActivatedRoute } from '@angular/router';
import { VacancyServiceService } from '../../services/vacancy-service.service';

@Component({
  selector: 'app-vacancy-list',
  imports: [VacancyCardComponent],
  templateUrl: './vacancy-list.component.html',
  styleUrl: './vacancy-list.component.css'
})
export class VacancyListComponent {
  vacancies: Vacancy[] = [];
    
  constructor(
    private companyService: CompanyServiceService,
    private vacancyService: VacancyServiceService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.loadVacancies(id.toString());
  }

  loadVacancies(id: string): void {
    this.companyService.getVacancyByCompany(id).subscribe(vacancies => {
      this.vacancies = vacancies;
    });
  }
  handleDeleteVacancy(id: number): void {
    this.vacancyService.deleteVacancy(id.toString()).subscribe(() => {
      this.vacancies = this.vacancies.filter(vacancy => vacancy.id !== id);
    });
  }

}
