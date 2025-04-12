import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ProductListComponent } from "./product-list/product-list.component";

import { Product } from './product-list/product';
import ProductData from './data.json';

@Component({
  selector: 'app-root',
  imports: [ProductListComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'online_store';
  products: Product[] = ProductData;
  categories: string[] = Array.from(new Set(ProductData.map(p => p.category)));
  selectedCategory: string | null = null;

  get filteredProducts(): Product[] {
    if (!this.selectedCategory) return [];
    return this.products.filter(p => 
      p.category === this.selectedCategory
    );
  }

  handleCategorySelect(category: string) {
    this.selectedCategory = category;
  }

  handleProductUpdate(updatedProduct: Product) {
    this.products = this.products.map(product => 
      product.item_name === updatedProduct.item_name 
        ? updatedProduct 
        : product
    );
  }
}
