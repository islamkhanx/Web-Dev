import { HttpClient } from '@angular/common/http';
import { Injectable} from '@angular/core';
import { Albums, Photo } from './albums';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  private url: string = 'https://jsonplaceholder.typicode.com/albums';
  constructor(private http: HttpClient) {}

  getAlbums(): Observable<Albums[]> {
    return this.http.get<Albums[]>(this.url);
  }
  getAlbum(id: number): Observable<Albums> {
    return this.http.get<Albums>(`${this.url}/${id}`);
  }
  deleteAlbum(id: number) {
    this.http.delete(`${this.url}/${id}`).subscribe();
  }

  updateAlbum(id: number, new_title: string) {
    const album = { id: id, title: new_title };
    this.http.put(`${this.url}/${album.id}`, album).subscribe();
  }
  
  getAlbumPhotos(id: number): Observable<Photo[]> {
    return this.http.get<Photo[]>(`${this.url}/${id}/photos`);
  }
}