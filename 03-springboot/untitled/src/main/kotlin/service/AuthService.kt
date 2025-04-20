package org.example.service

import org.springframework.stereotype.Service
import jakarta.annotation.PostConstruct

@Service
class AuthService {

    private val validUsers = mapOf(
        "test" to "testowy",
        "user" to "pass"
    )

    @PostConstruct
    fun init() {
        println("Eager Singleton initialized.")
    }

    fun authenticate(username: String, password: String): Boolean {
        return validUsers[username] == password
    }
}
