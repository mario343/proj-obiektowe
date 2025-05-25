import Fluent

struct CreateProduct: AsyncMigration {
    func prepare(on database: Database) async throws {
        try await
        database.schema("products")
            .id()
            .field("name", .string, .required)
            .field("price", .double, .required)
            .field("description", .string)
            .create()
    }

    func revert(on database: Database) async throws {
        try await
        database.schema("products").delete()
    }
}
