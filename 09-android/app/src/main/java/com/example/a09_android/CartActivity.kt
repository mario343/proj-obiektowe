package com.example.a09_android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.a09_android.model.Cart
import com.example.a09_android.ui.theme.AppTheme

class CartActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AppTheme {
                CartView()
            }
        }
    }
}

@Composable
fun CartView() {
    val products = Cart.items

    Column(modifier = Modifier.padding(16.dp)) {
        Text("Cart", style = MaterialTheme.typography.titleLarge)
        Spacer(modifier = Modifier.height(16.dp))

        if (products.isEmpty()) {
            Text("Cart is empty.", style = MaterialTheme.typography.bodyMedium)
        } else {
            LazyColumn {
                items(products) { product ->
                    Card(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 8.dp),
                        elevation = CardDefaults.cardElevation(2.dp)
                    ) {
                        Column(modifier = Modifier.padding(16.dp)) {
                            Text(product.name, style = MaterialTheme.typography.titleMedium)
                            Text("Price: ${product.price} PLN", style = MaterialTheme.typography.bodyMedium)
                            Spacer(modifier = Modifier.height(8.dp))
                            Button(onClick = { Cart.removeItem(product) }) {
                                Text("Delete")
                            }
                        }
                    }
                }
            }
            Spacer(modifier = Modifier.height(16.dp))
            val total = products.sumOf { it.price }
            Text("Total: $total PLN", style = MaterialTheme.typography.titleMedium)

            Spacer(modifier = Modifier.height(16.dp))
            Button(
                onClick = { Cart.clear() },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Empty the cart")
            }
        }
    }
}
