import { Component, Input } from '@angular/core';
import { Vacancy } from '../../../models/vacancy';

@Component({
  selector: 'app-vacancy-edit',
  imports: [],
  templateUrl: './vacancy-edit.component.html',
  styleUrl: './vacancy-edit.component.css'
})
export class VacancyEditComponent {
  @Input() vacancy!: Vacancy;
}
