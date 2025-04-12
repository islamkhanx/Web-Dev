import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Product } from '../product';

@Component({
  selector: 'app-product-item',
  imports: [],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css'
})
export class ProductItemComponent {
  @Input() product!: Product;
  @Output() productDeactivated = new EventEmitter<Product>();
  @Output() productLiked = new EventEmitter<Product>();

  deactivateProduct() {
    this.productDeactivated.emit({
      ...this.product,
      is_active: false
    });
  }

  addLike() {
    this.productLiked.emit({
      ...this.product,
      likes: this.product.likes + 1
    });
  }
}
