import FluentSQLiteDriver
import Leaf
import Vapor
import Fluent

public func configure(_ app: Application) async throws {

    app.databases.use(DatabaseConfigurationFactory.sqlite(.file("db.sqlite")), as: .sqlite)
    app.migrations.add(CreateProduct())

    try await app.autoMigrate()

    app.views.use(.leaf)

    try routes(app)
}
