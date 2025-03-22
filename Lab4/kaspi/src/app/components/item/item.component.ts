import { Component, Input } from '@angular/core';
import { Item } from '../../item';

@Component({
  selector: 'app-item',
  imports: [],
  templateUrl: './item.component.html',
  styleUrl: './item.component.css'
})
export class ItemComponent {
  @Input() item!: Item;
  getRatingWidth(): string {
    return (this.item.rating / 5 * 100) + '%';
  }
}
