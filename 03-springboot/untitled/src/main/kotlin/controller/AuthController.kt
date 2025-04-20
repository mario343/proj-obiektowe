package org.example.controller

import org.example.model.UserRequest
import org.example.service.AuthService
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api")
class AuthController(
    private val authService: AuthService
) {

    private val protectedData = listOf("Montreal", "Canadiens")

    @PostMapping("/login")
    fun login(@RequestBody request: UserRequest): Any {
        return if (authService.authenticate(request.username, request.password)) {
            mapOf("status" to "success", "data" to protectedData)
        } else {
            mapOf("status" to "fail", "message" to "Invalid credentials")
        }
    }
}