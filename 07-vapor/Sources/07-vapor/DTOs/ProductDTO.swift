
import Vapor

struct ProductInput: Content {
    let name: String
    let price: Double
    let description: String
}

struct ProductOutput: Content {
    let id: UUID
    let name: String
    let price: Double
    let description: String
}