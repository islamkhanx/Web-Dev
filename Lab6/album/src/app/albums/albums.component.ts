import { Component, signal, Signal, inject } from '@angular/core';
import { AlbumsService } from '../albums.service';
import { Albums } from '../albums';
import { toSignal } from '@angular/core/rxjs-interop';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';


@Component({
  selector: 'app-albums',
  imports: [CommonModule, RouterLink, RouterOutlet, RouterLinkActive],
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent {
  items: Signal<Albums[]>;

  constructor(private albumsService: AlbumsService) {
    this.items = toSignal(
      this.albumsService.getAlbums(),
      { initialValue: [] });
  }
  isAlbumSelected() {
    return window.location.pathname !== '/albums' && 
           window.location.pathname.startsWith('/albums/');
  }
  deleteAlbum(id: number) {
    this.albumsService.deleteAlbum(id);
  }
}
