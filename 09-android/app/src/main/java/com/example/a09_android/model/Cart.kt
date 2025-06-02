package com.example.a09_android.model

import androidx.compose.runtime.snapshots.SnapshotStateList
import androidx.compose.runtime.mutableStateListOf

object Cart {
    private val _items = mutableStateListOf<Product>()
    val items: SnapshotStateList<Product> get() = _items

    fun addItem(product: Product) {
        _items.add(product)
    }

    fun removeItem(product: Product) {
        _items.remove(product)
    }

    fun clear() {
        _items.clear()
    }
}
