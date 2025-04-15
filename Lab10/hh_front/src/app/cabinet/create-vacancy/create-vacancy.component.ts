import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { VacancyServiceService } from '../../services/vacancy-service.service';
import { CompanyServiceService } from '../../services/company-service.service';
import { Company } from '../../models/company';

@Component({
  selector: 'app-create-vacancy',
  imports: [ReactiveFormsModule],
  templateUrl: './create-vacancy.component.html',
  styleUrl: './create-vacancy.component.css'
})
export class CreateVacancyComponent {
  vacancyForm: FormGroup;
  companies: Company[] = [];
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private vacancyService: VacancyServiceService,
    private companyService: CompanyServiceService
  ) {
    this.vacancyForm = this.fb.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      salary: [null, [Validators.required, Validators.min(0)]],
      company: [null, Validators.required]
    })
  };

  ngOnInit() {
    this.companyService.getAllCompanies().subscribe({
      next: (res) => {
        this.companies = res;
        this.successMessage = 'ok';
        this.errorMessage = null;
        this.vacancyForm.reset();
      },
      error: (err) => {
        this.successMessage = null;
        this.errorMessage = err.error.message;
      }
    });
  }

  onSubmit() {
    if (this.vacancyForm.valid) {
      this.vacancyService.postVacancy(this.vacancyForm.value);
    }
  }
}
