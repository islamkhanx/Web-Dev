import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumsDetailComponent } from './albums/albums-detail/albums-detail.component';
import { AlbumPhotosComponent } from './albums/album-photos/album-photos.component';

export const routes: Routes = [
    { path: '', component: HomeComponent , pathMatch: 'full' },
    { path: 'about', component: AboutComponent },
    { 
        path: 'albums',
        component: AlbumsComponent,
        children: [
            {
                path: ':id',
                component: AlbumsDetailComponent,
                pathMatch: 'full',
            },
            {
                path: ':id/photos',
                component: AlbumPhotosComponent,
                pathMatch: 'full',
            }
    ]},
    // { path: 'albums/:id/photos', component: AlbumPhotosComponent },
];
