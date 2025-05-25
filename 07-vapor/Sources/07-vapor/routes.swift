import Fluent
import Vapor


func routes(_ app: Application) throws {
    app.get { req async throws -> View in
        try await req.view.render("index")
    }

    try app.register(collection: ProductController())
}