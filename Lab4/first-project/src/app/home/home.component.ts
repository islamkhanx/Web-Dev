import { Component } from '@angular/core';
import { HousinglocationComponent } from "../housinglocation/housinglocation.component";
import { Housinglocation } from "../housinglocation";
@Component({
  selector: 'app-home',
  imports: [HousinglocationComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  housingLocation : Housinglocation = {
    id: 9999,
    name: "Islamkhans Home",
    city: "Almaty",
    state: "Kazakshtan",
    photo: `https://angular.dev/assets/images/tutorials/common/example-house.jpg`,
    availableUnits: 0,
    wifi: false,
    laundry: false
  }
}
