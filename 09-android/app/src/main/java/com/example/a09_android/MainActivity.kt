package com.example.a09_android

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ShoppingCart
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.example.a09_android.mock.MockData
import com.example.a09_android.model.Cart
import com.example.a09_android.ui.theme.AppTheme


class MainActivity : ComponentActivity() {
    @OptIn(ExperimentalMaterial3Api::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            val cartSize by remember { derivedStateOf { Cart.items.size } }

            AppTheme   {
                Scaffold(
                    topBar = {
                        TopAppBar(
                            title = {
                                Text(
                                    "Categories",
                                    fontWeight = FontWeight.Bold,
                                    modifier = Modifier.fillMaxWidth(),
                                    textAlign = TextAlign.Center
                                )
                            }
                        )
                    },
                    floatingActionButton = {
                        ExtendedFloatingActionButton(
                            onClick = {
                                startActivity(Intent(this@MainActivity, CartActivity::class.java))
                            },
                            modifier = Modifier.padding(16.dp),
                            containerColor = MaterialTheme.colorScheme.primary,
                            contentColor = Color.White,
                            icon = {
                                BadgedBox(badge = {
                                    if (cartSize > 0) {
                                        Badge {
                                            Text("$cartSize", color = Color.White)
                                        }
                                    }
                                }) {
                                    Icon(
                                        Icons.Filled.ShoppingCart,
                                        contentDescription = "Cart"
                                    )
                                }
                            },
                            text = {
                                Text("View Cart", fontWeight = FontWeight.Bold)
                            }
                        )
                    }
                ) { paddingValues ->
                    LazyColumn(
                        modifier = Modifier
                            .padding(paddingValues)
                            .fillMaxSize(),
                        contentPadding = PaddingValues(16.dp),
                        verticalArrangement = Arrangement.spacedBy(12.dp)
                    ) {
                        items(MockData.categories) { category ->
                            ElevatedButton(
                                onClick = {
                                    val intent = Intent(
                                        this@MainActivity,
                                        ProductActivity::class.java
                                    )
                                    intent.putExtra("categoryId", category.id)
                                    startActivity(intent)
                                },
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .height(50.dp),
                                colors = ButtonDefaults.elevatedButtonColors()
                            ) {
                                Text(
                                    text = category.name,
                                    style = MaterialTheme.typography.titleLarge.copy(
                                        fontWeight = FontWeight.Bold
                                    )
                                )
                            }
                        }
                    }
                }
            }
        }
    }
}
