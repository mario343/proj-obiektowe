import io.ktor.server.application.*
import io.ktor.server.response.*
import io.ktor.server.request.*
import io.ktor.server.routing.*
import kotlinx.serialization.Serializable
import com.example.JWTConfig
import com.example.UserRepository
import io.ktor.http.*

fun Route.authRoutes() {
    route("/auth") {
        post("/register") {
            val credentials = call.receive<Credentials>()
            
              if (credentials.username.isBlank() || credentials.password.isBlank()) {
                call.respond(HttpStatusCode.BadRequest, mapOf("error" to "Nazwa użytkownika i hasło nie mogą być puste"))
                return@post
            }
            
            if (credentials.username.length < 3 || credentials.password.length < 6) {
                call.respond(HttpStatusCode.BadRequest, mapOf("error" to "Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6"))
                return@post
            }
            if (credentials.username.length > 16 || credentials.password.length > 32) {
                call.respond(HttpStatusCode.BadRequest, mapOf("error" to "Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32"))
                return@post
            }

            val success = UserRepository.register(credentials.username, credentials.password)
            
            if (success) {
                call.respond(mapOf("message" to "Zarejestrowano pomyślnie"))
            } else {
                call.respond(mapOf("error" to "Użytkownik już istnieje"))
            }
        }

        post("/login") {
            val credentials = call.receive<Credentials>()
            val user = UserRepository.getUser(credentials.username)
            


             if (credentials.username.isBlank() || credentials.password.isBlank()) {
                call.respond(HttpStatusCode.BadRequest, mapOf("error" to "Nazwa użytkownika i hasło nie mogą być puste"))
                return@post
            }

            if (user == null || !UserRepository.verifyPassword(credentials.password, user.passwordHash)) {
                call.respond(HttpStatusCode.Unauthorized, mapOf("error" to "Nieprawidłowa nazwa użytkownika lub hasło"))
                return@post
            }
            
            val token = JWTConfig.generateToken(credentials.username)
            call.respond(mapOf("token" to token))
        }
    }
}

@Serializable
data class Credentials(val username: String, val password: String)
