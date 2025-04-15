import { Routes } from '@angular/router';
import { VacanciesComponent } from './vacancies/vacancies.component';
import { CompaniesComponent } from './companies/companies.component';
import { CabinetComponent } from './cabinet/cabinet.component';
import { HomeComponent } from './home/home.component';
import { VacancyDetailComponent } from './vacancies/vacancy-detail/vacancy-detail.component';
import { VacancyListComponent } from './companies/vacancy-list/vacancy-list.component';
import { CreateVacancyComponent } from './cabinet/create-vacancy/create-vacancy.component';
import { CreateCompanyComponent } from './cabinet/create-company/create-company.component';

export const routes: Routes = [
    { path: '', component: HomeComponent, pathMatch: 'full' },
    { path: 'vacancies', component: VacanciesComponent },
    { path: 'vacancies/:id', component: VacancyDetailComponent },

    { path: 'companies', component: CompaniesComponent},
    { path: 'companies/:id/vacancies', component: VacancyListComponent},
    { 
        path: 'cabinet',
        component: CabinetComponent, 
        children: [
        { path: 'create-company', component: CreateCompanyComponent },
        { path: 'create-vacancy', component: CreateVacancyComponent }
      ]}
];
