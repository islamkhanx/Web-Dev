import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Company } from '../models/company';
import { Vacancy } from '../models/vacancy';

@Injectable({
  providedIn: 'root'
})
export class CompanyServiceService {
  private url = 'http://localhost:8000/api/companies/'
  constructor(private http: HttpClient) {}

  getAllCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(this.url);
  }

  postCompany(company: Company): Observable<Company> {
    return this.http.post<Company>(this.url, company);
  }

  getCompany(id: string): Observable<Company> {
    return this.http.get<Company>(`${this.url}/${id}`);
  }
  getVacancyByCompany(id: string): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.url}${id}/vacancies/`);
  }

  updateCompany() {
    
  }

  deleteCompany(id: string): Observable<Company> {
    return this.http.delete<Company>(`${this.url}${id}/`);
  }
}
