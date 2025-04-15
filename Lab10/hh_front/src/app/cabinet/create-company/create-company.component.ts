import { Component } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { Company } from '../../models/company';
import { CompanyServiceService } from '../../services/company-service.service';

@Component({
  selector: 'app-create-company',
  imports: [ReactiveFormsModule, FormsModule],
  templateUrl: './create-company.component.html',
  styleUrl: './create-company.component.css'
})
export class CreateCompanyComponent {
  companyForm: FormGroup;
  companies: Company[] = [];
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(
    private fb: FormBuilder,
    private companyService: CompanyServiceService
  ) {
    this.companyForm = this.fb.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      city: [null, [Validators.required]],
      address: [null, Validators.required]
    })
  };

  ngOnInit() {
    this.companyService.getAllCompanies().subscribe({
      next: (res) => this.companies = res
    });
  }

  onSubmit() {
    if (this.companyForm.valid) {
      console.log(this.companyForm.value);
      this.companyService.postCompany(this.companyForm.value).subscribe({});
    }
  }
}
