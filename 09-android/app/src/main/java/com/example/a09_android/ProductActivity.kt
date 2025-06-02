package com.example.a09_android

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ShoppingCart
import androidx.compose.material3.*
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.a09_android.mock.MockData
import com.example.a09_android.model.Cart
import com.example.a09_android.ui.theme.AppTheme

class ProductActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val categoryId = intent.getIntExtra("categoryId", 0)
        val category = MockData.categories.find { it.id == categoryId }
        val products = MockData.products.filter { it.categoryId == categoryId }

        setContent {
            AppTheme {
                val cartSize by remember { derivedStateOf { Cart.items.size } }

                Scaffold(
                    floatingActionButton = {
                        FloatingActionButton(
                            onClick = {
                                startActivity(Intent(this@ProductActivity, CartActivity::class.java))
                            },
                            modifier = Modifier.padding(16.dp)
                        ) {
                            BadgedBox(badge = {
                                if (cartSize > 0) {
                                    Badge { Text("$cartSize") }
                                }
                            }) {
                                Icon(Icons.Default.ShoppingCart, contentDescription = "Cart")
                            }
                        }
                    }
                ) { paddingValues ->
                    Column(
                        modifier = Modifier
                            .padding(paddingValues)
                            .padding(16.dp)
                    ) {
                        Text(
                            category?.name ?: "Products",
                            style = MaterialTheme.typography.titleLarge
                        )
                        Spacer(modifier = Modifier.height(16.dp))
                        LazyColumn {
                            items(products) { product ->
                                Card(
                                    modifier = Modifier
                                        .fillMaxWidth()
                                        .padding(vertical = 8.dp)
                                        .clickable {
                                            Cart.addItem(product)
                                        },
                                    elevation = CardDefaults.cardElevation(2.dp)
                                ) {
                                    Column(modifier = Modifier.padding(16.dp)) {
                                        Text(product.name, style = MaterialTheme.typography.titleMedium)
                                        Text("Price: ${product.price} PLN", style = MaterialTheme.typography.bodyMedium)
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
