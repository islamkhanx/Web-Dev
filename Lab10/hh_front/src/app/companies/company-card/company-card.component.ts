import { Component, EventEmitter, Input, input, Output } from '@angular/core';
import { Company } from '../../models/company';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-company-card',
  imports: [RouterLink],
  templateUrl: './company-card.component.html',
  styleUrl: './company-card.component.css'
})
export class CompanyCardComponent {
  @Input() company!: Company;
  @Output() deleteCompanyEE = new EventEmitter<number>();

  deleteCompany() {
    this.deleteCompanyEE.emit(this.company.id);
  }
}
