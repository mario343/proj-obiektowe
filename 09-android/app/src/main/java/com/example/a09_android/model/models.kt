package com.example.a09_android.model

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class Category(
    val id: Int,
    val name: String
) : Parcelable

@Parcelize
data class Product(
    val id: Int,
    val name: String,
    val price: Double,
    val categoryId: Int
) : Parcelable