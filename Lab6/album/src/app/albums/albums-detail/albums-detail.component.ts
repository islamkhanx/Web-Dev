import { Component, inject, Signal } from '@angular/core';
import { ActivatedRoute, Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { AlbumsService } from '../../albums.service';
import { toSignal } from '@angular/core/rxjs-interop';
import { Albums } from '../../albums';

@Component({
  selector: 'app-albums-detail',
  imports: [RouterLink, RouterOutlet, RouterLinkActive],
  templateUrl: './albums-detail.component.html',
  styleUrl: './albums-detail.component.css'
})
export class AlbumsDetailComponent {
  album: Signal<Albums>;
  constructor(
    private route: ActivatedRoute,
    private albumsService: AlbumsService
  ) {
    const albumId = Number(this.route.snapshot.paramMap.get('id'));
    this.album = toSignal(this.albumsService.getAlbum(albumId), { initialValue: {} as Albums });
  }
  saveAlbum(newTitle: string) {
    const albumId = Number(this.route.snapshot.paramMap.get('id'));
    this.albumsService.updateAlbum(albumId, newTitle);
  }
}
