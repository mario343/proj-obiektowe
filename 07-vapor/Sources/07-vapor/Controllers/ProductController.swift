import Vapor
import Fluent

struct ProductController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {

    routes.get { req in
        return req.view.render("index")
    }
    
    let products = routes.grouped("products")    
    products.get(use: index)
    products.get("create", use: createView)
    products.post(use: create)

    products.post("delete", ":productID", use: delete)

    products.group(":productID") { product in
        product.get(use: show)
        product.post(use: update)
    }

    }

    struct ProductsContext: Encodable {
        var products: [ProductOutput]
    }

    struct ProductContext: Encodable {
        var product: ProductOutput
    }

    func index(req: Request) throws -> EventLoopFuture<View> {
    return Product.query(on: req.db)
        .all()
        .flatMap { products in
            let productOutputs = products.compactMap { product -> ProductOutput? in
                guard let id = product.id else { return nil }
                return ProductOutput(
                    id: id,
                    name: product.name,
                    price: product.price,
                    description: product.description
                )
            }
            let context = ProductsContext(products: productOutputs)
            return req.view.render("products/index", context)
        }}

    func createView(req: Request) throws -> EventLoopFuture<View> {
    return req.view.render("products/create")
}

    func create(req: Request) throws -> EventLoopFuture<Response> {
        let input = try req.content.decode(ProductInput.self)
        let product = Product(name: input.name, price: input.price, description: input.description)
        return product.save(on: req.db).map {
            req.redirect(to: "/products")
        }
    }

    func show(req: Request) throws -> EventLoopFuture<View> {
        guard let productID = req.parameters.get("productID", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(productID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                guard let id = product.id else {
                    return req.eventLoop.future(error: Abort(.internalServerError))
                }
                let output = ProductOutput(
                    id: id,
                    name: product.name,
                    price: product.price,
                    description: product.description
                )
                return req.view.render("products/product", ProductContext(product: output))
            }
    }

    func update(req: Request) throws -> EventLoopFuture<Response> {
        let input = try req.content.decode(ProductInput.self)

        guard let productID = req.parameters.get("productID", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(productID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                product.name = input.name
                product.price = input.price
                product.description = input.description
                return product.save(on: req.db).map {
                    req.redirect(to: "/products")
                }
            }
    }

    func delete(req: Request) throws -> EventLoopFuture<Response> {
        guard let productID = req.parameters.get("productID", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(productID, on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                product.delete(on: req.db).map {
                    req.redirect(to: "/products")
                }
            }
    }
}
