package com.example.a09_android.mock

import com.example.a09_android.model.Category
import com.example.a09_android.model.Product

object MockData {
    val categories = listOf(
        Category(1, "Electronics"),
        Category(2, "Books"),
        Category(3, "Clothing"),
        Category(4, "Home & Garden"),
        Category(5, "Sports"),
        Category(6, "Beauty"),
        Category(7, "Toys"),
        Category(8, "Food & Beverages"),
        Category(9, "Automotive"),
        Category(10, "Health")
    )

    val products = listOf(
        Product(1, "Laptop", 3000.0, 1),
        Product(2, "Smartphone", 1500.0, 1),
        Product(3, "Headphones", 250.0, 1),
        Product(4, "Smart Watch", 800.0, 1),
        Product(5, "Bluetooth Speaker", 180.0, 1),

        Product(6, "The Witcher", 45.0, 2),
        Product(7, "Dune", 38.0, 2),
        Product(8, "Atomic Habits", 55.0, 2),
        Product(9, "Sapiens", 60.0, 2),
        Product(10, "The Alchemist", 40.0, 2),

        Product(11, "T-Shirt", 50.0, 3),
        Product(12, "Jeans", 120.0, 3),
        Product(13, "Winter Jacket", 300.0, 3),
        Product(14, "Running Shoes", 220.0, 3),
        Product(15, "Dress", 150.0, 3),

        Product(16, "Coffee Table", 400.0, 4),
        Product(17, "Gardening Tools Set", 90.0, 4),
        Product(18, "Bed Sheets", 120.0, 4),
        Product(19, "Wall Clock", 75.0, 4),
        Product(20, "Dining Chair", 150.0, 4),

        Product(21, "Yoga Mat", 60.0, 5),
        Product(22, "Dumbbell Set", 200.0, 5),
        Product(23, "Running Shoes", 250.0, 5),
        Product(24, "Bicycle", 1200.0, 5),
        Product(25, "Camping Tent", 350.0, 5),

        Product(26, "Perfume", 180.0, 6),
        Product(27, "Skincare Set", 120.0, 6),
        Product(28, "Hair Dryer", 90.0, 6),
        Product(29, "Makeup Palette", 65.0, 6),
        Product(30, "Electric Toothbrush", 110.0, 6),

        Product(31, "Lego Set", 150.0, 7),
        Product(32, "Board Game", 80.0, 7),
        Product(33, "Doll", 45.0, 7),
        Product(34, "Remote Control Car", 120.0, 7),
        Product(35, "Puzzle", 30.0, 7),

        Product(36, "Organic Coffee", 25.0, 8),
        Product(37, "Chocolate Box", 35.0, 8),
        Product(38, "Olive Oil", 40.0, 8),
        Product(39, "Tea Collection", 30.0, 8),
        Product(40, "Protein Bars (12 pack)", 45.0, 8),

        Product(41, "Car Phone Holder", 25.0, 9),
        Product(42, "Jump Starter", 200.0, 9),
        Product(43, "Car Vacuum", 80.0, 9),
        Product(44, "Tire Pressure Gauge", 15.0, 9),
        Product(45, "Car Wax", 30.0, 9),

        Product(46, "Blood Pressure Monitor", 90.0, 10),
        Product(47, "Thermometer", 25.0, 10),
        Product(48, "First Aid Kit", 40.0, 10),
        Product(49, "Massage Gun", 150.0, 10),
        Product(50, "Air Purifier", 300.0, 10)
    )
}