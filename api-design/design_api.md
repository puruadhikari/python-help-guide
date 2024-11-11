## REST API Design

- Designing URIs (/products?page=1&pageSize=10)
- HTTP Methods (GET,POST,PUT,PATCH,DELETE)
- HTTP Status Codes (200,201,3XX, 400,401,404,429,500)
- Designing Resources **Association of entities** (e.g. customer and order here - /customers/123/orders )
- Paging, Sorting e.g /products?sort=price , and Filtering e.g. /customers?state=GA
- Error handling (http error codes)
- Caching (client side caching) , header ETag and if-none-match , GET will return 304 if the entity has not changed 
- Version API (two options: URI, Query String and Header). URI may not be the best and it require change to code. Custom header X-version
- Logging (trace-id) : as a header to ensure tracking of requests
- Security - in transit (TLS) and inside security (Option - Auth Tokens (Cookie, Token (JWT- iDaaS),OAuth)
- Rate Limiting and Throttling
- async usage if needed anywhere

### 1. Designing URIs

Uniform Resource Identifiers (URIs): Used to identify resources. Should be intuitive and descriptive.

_Example: /api/customers/123 represents a specific customer._

**Nouns Not Verbs**: URIs should represent entities (nouns), not actions (verbs).

_Example: Use /orders/123 instead of /getOrderDetails/123_.

**Hierarchical Paths**: Represent relationships in URIs using a clear hierarchy.

_Example: /customers/123/orders for orders belonging to a specific customer._

Query Parameters: Use for **optional information**, such as filtering, sorting, and paging.

Example: /products?page=1&pageSize=10
Example: /customers/2?includeProject=True

### 2. HTTP Methods: Common methods include:

- GET: Retrieve a resource.
- POST: Create a new resource.
- PUT: Replace an existing resource.
- PATCH: Update part of a resource.
- DELETE: Remove a resource.


| Endpoint        | GET            | POST             | PUT              | PATCH            | DELETE                                       |
|-----------------|----------------|------------------|------------------|------------------|----------------------------------------------|
| `/customers`    | Retrieve list of customers | Create a new customer | N/A | N/A | Error as onc should not delete all customers |
| `/customers/{id}` | Retrieve a specific customer by ID | N/A | Update a customer by ID | Partially update a customer by ID | Delete a customer by ID                      |

### 3. HTTP Status Codes

2xx Success:

200 OK: The request was successful.

201 Created: A resource was created (usually after a POST).

3xx Redirection: Redirect client to a different location.

4xx Client Errors:

400 Bad Request: Invalid input data.

401 Unauthorized: Authentication is needed.

404 Not Found: Resource could not be found.

429 Too Many Request : Repond with **Retry-After** indicating when the client should retry again.

5xx Server Errors: Indicate problems with the server.

### 4. Designing Resources

Resource Naming: Use plural nouns to represent collections.

Example: /users, /products.

Associations: Define relationships through nested URIs.

Example: /customers/123/orders to list orders for a specific customer.

Data Representation: Return JSON by default, but support other formats via the Accept header.

Consistency: Use consistent naming conventions throughout the API.

### 5. Paging, Sorting, and Filtering

Paging: Prevent overload by limiting the number of resources returned.

Example: /products?page=2&pageSize=25.

Sorting: Enable sorting using query parameters.

Example: /products?sort=price.

Filtering: Allow filtering on specific fields.

Example: /customers?state=GA.

### 7. Error Handling

Meaningful Responses: Provide useful error messages in JSON format.

Example:

Consistent Error Codes: Use standard HTTP codes with meaningful messages.

### 8. Headers

**Request Headers:** Provide metadata about the request, such as:

- Accept: Specifies the media types the client can handle (e.g., application/json).

- Content-Type: Indicates the format of the request body (e.g., application/json).

- Authorization: Contains credentials for authenticating the client (e.g., Bearer <token>).

- Response Headers: Provide metadata about the response, such as:

- Content-Type: Specifies the media type of the returned content (e.g., application/json).

- Cache-Control: Directives for caching mechanisms (e.g., no-cache).

- ETag: A unique identifier for the version of the resource, used for caching validation.

- Custom Headers: You can define custom headers to pass additional context or information. Use a consistent naming convention, such as X-Custom-Header.

### 9. Versioning

- URI-based Versioning: Include version in the URI.

_Example: /api/v1/products._

- Header-based Versioning: Specify version in a custom header.

_Example: X-API-Version: 1._

- Content-Type Versioning: Use versioning in Accept header.

_Example: Accept: application/vnd.myapi.v1+json._

### 10. Caching

Client-Side Caching: Use headers like Cache-Control, Expires, and ETag.

ETag: Provides a unique identifier for a resource to validate if a cached version is still valid.

Example:

Client Request:

Server Response:

### 11. Security

Authentication vs Authorization: Authentication identifies the user, while authorization determines what they can do.

Methods:

OAuth: For token-based authentication using third-party providers like Google or Facebook.

JWT (JSON Web Tokens): Token containing encoded information about the user.

HTTPS: Always enforce HTTPS to protect data in transit.

CORS (Cross-Origin Resource Sharing): Control which domains can interact with the API to protect from unauthorized usage.

### 12. Asynchronous APIs

Definition: Asynchronous APIs allow clients to request operations that may take a long time to complete without blocking the client.

Techniques:

* **Long Polling**: Client makes a request and waits until the server responds, which may take time.
* **WebSockets:** Establish a persistent connection between client and server for real-time communication.
* **Callback URLs**: Client provides a callback URL where the server can send the result when the processing is complete.
* **Message Queues**: Server processes the request asynchronously and sends a message to a queue when complete.

Example Scenarios:

Order Processing: Processing a purchase order that requires multiple steps, such as payment and inventory updates.

Data Import: Importing large datasets that take a long time to process.

Notification Services: Sending notifications to users when an event occurs, such as a change in stock prices.

### 13. Rate Limiting and Throttling

**Rate Limiting:** Control the number of requests a client can make within a specific time frame to prevent abuse.

Example: Allow up to 100 requests per hour per user.

Throttling: Slow down the rate of requests when limits are approached rather than blocking entirely.

**Headers for Rate Limiting:**

X-RateLimit-Limit: Maximum number of requests allowed.

X-RateLimit-Remaining: Number of requests left in the current window.

X-RateLimit-Reset: Time at which the rate limit will reset.

14. HATEOAS (Hypermedia as the Engine of Application State)

Definition: A principle of REST that allows clients to dynamically navigate the API using hyperlinks provided in the responses.

Benefits: Simplifies client interaction with the API by providing links to related resources.

Example:

### 15. Advanced REST Topics

Asynchronous APIs: Implement long-running operations with async techniques for better user experience.

Example 1: Order Processing - Handling payment authorization and shipment in the background while providing a status update to the client.

Example 2: Video Processing - Converting video formats and notifying the user once processing is complete.


### 16. Monitoring and Analytics

Logging: Implement logging for all API requests and responses to diagnose issues and track usage.

Metrics: Track key metrics like response time, error rates, and request volume to ensure API health.

Tools: Use monitoring tools like Prometheus, New Relic, or Elastic Stack to monitor and analyze API performance.

