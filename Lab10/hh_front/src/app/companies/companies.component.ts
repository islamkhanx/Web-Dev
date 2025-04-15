import { Component } from '@angular/core';
import { Company } from '../models/company';
import { CompanyServiceService } from '../services/company-service.service';
import { CompanyCardComponent } from "./company-card/company-card.component";
import { Router } from '@angular/router';

@Component({
  selector: 'app-companies',
  imports: [CompanyCardComponent],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent {
  companies: Company[] = [];
  constructor(
    private companyService: CompanyServiceService,
    private router: Router
  ) {}
  
  ngOnInit() {
    this.companyService.getAllCompanies().subscribe(companies => {
      this.companies = companies;
    });
  }
  handleViewVacancies(companyId: number): void {
    this.router.navigate(['/companies', companyId, 'vacancies']);
  }
  hendleDeleteCompanyEE(companyId: number): void {
    this.companyService.deleteCompany(companyId.toString()).subscribe(() => {
      this.companies = this.companies.filter(company => company.id !== companyId);
    });
  }
}
