import { Component, Input } from '@angular/core';
import { Location, NgClass } from '@angular/common';
import { Vacancy } from '../../models/vacancy';
import { ActivatedRoute } from '@angular/router';
import { VacancyServiceService } from '../../services/vacancy-service.service';
import { VacancyEditComponent } from "./vacancy-edit/vacancy-edit.component";


@Component({
  selector: 'app-vacancy-detail',
  imports: [NgClass,  VacancyEditComponent],
  templateUrl: './vacancy-detail.component.html',
  styleUrl: './vacancy-detail.component.css'
})
export class VacancyDetailComponent {
  vacancy!: Vacancy;
  editmode: boolean = false;
  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private vacancyService: VacancyServiceService
  ) {}

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.vacancyService.getVacancy(id.toString()).subscribe(vacancy => {
      this.vacancy = vacancy
    })
  }

  goBack() {
    this.location.back();
  }
  toggleEdit() {
    this.editmode = !this.editmode;
  }
}
