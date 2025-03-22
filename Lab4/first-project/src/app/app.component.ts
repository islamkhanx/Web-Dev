import { Component } from '@angular/core';
import { HomeComponent } from "./home/home.component";
import { Housinglocation } from './housinglocation';

@Component({
  selector: 'app-root',
  imports: [HomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'first-project';
}
