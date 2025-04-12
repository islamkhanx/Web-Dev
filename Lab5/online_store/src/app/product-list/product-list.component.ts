import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Product } from './product';
import { ProductItemComponent } from './product-item/product-item.component';

@Component({
  selector: 'app-product-list',
  imports: [ProductItemComponent],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  @Input() products!: Product[];
  @Input() selectedCategory: string | null = null;
  @Output() productDeactivated = new EventEmitter<Product>();
  @Output() productLiked = new EventEmitter<Product>();

  handleProductDeactivation(deactivatedProduct: Product) {
    this.productDeactivated.emit(deactivatedProduct);
  }
  
  handleProductLike(likedProduct: Product) {
    this.productLiked.emit(likedProduct);
  }
}
