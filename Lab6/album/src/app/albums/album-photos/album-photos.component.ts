import { Component, Signal } from '@angular/core';
import { Photo } from '../../albums';
import { AlbumsService } from '../../albums.service';
import { ActivatedRoute } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-album-photos',
  imports: [],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent {
  photos: Signal<Photo[]>;
  constructor(
    private route: ActivatedRoute,
    private albumsService: AlbumsService
  )
  {
    const albumId = Number(this.route.snapshot.paramMap.get('id'));
    this.photos = toSignal(this.albumsService.getAlbumPhotos(albumId), { initialValue: [] as Photo[] });
  }
}
