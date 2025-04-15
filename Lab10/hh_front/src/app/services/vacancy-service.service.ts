import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Vacancy } from '../models/vacancy';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VacancyServiceService {
  private url = 'http://localhost:8000/api/vacancies/'
  constructor(private http: HttpClient) { }

  getAllVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.url);
  }

  postVacancy(vacancy: Vacancy): Observable<Vacancy> {
    return this.http.post<Vacancy>(this.url, vacancy);
  }

  getVacancy(id: string): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.url}${id}/`);
  }

  updateVacancy(){
  }

  deleteVacancy(id: string): Observable<Vacancy> {
    return this.http.delete<Vacancy>(`${this.url}${id}/`);
  }
}
