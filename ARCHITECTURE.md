# 🏗 Architecture Flow

This project follows a layered (Clean Architecture–inspired) structure that separates concerns into four distinct layers:

- **Handler**
- **Usecase**
- **Repository**
- **Entity**

Each layer has a clearly defined responsibility and communicates only with the layer directly below it.

---

## 🔄 Request Flow Overview
```text
Client (HTTP Request)
↓
Handler (FastAPI Layer)
↓
Usecase (Business Logic Layer)
↓
Repository (Data Access Layer)
↓
External API (PokeAPI)
```

---

## 📌 Layer Responsibilities

### 1️⃣ Handler Layer (Interface / Delivery Layer)

**Responsibility:**  
Handles HTTP-related concerns.

- Defines API endpoints
- Validates query parameters
- Calls the appropriate Usecase
- Formats the HTTP response
- Translates internal errors into HTTP responses

✅ Knows about FastAPI  
❌ Does NOT contain business logic  
❌ Does NOT directly call external APIs  

---

### 2️⃣ Usecase Layer (Application / Business Logic Layer)

**Responsibility:**  
Implements the core application logic.

- Receives parameters from the Handler
- Calls the Repository to retrieve data
- Processes and transforms raw data
- Instantiates Entities
- Returns structured results

✅ Contains business rules  
✅ Orchestrates the flow of data  
❌ Does NOT know about HTTP  
❌ Does NOT know about infrastructure details  

---

### 3️⃣ Repository Layer (Infrastructure / Data Access Layer)

**Responsibility:**  
Acts as a gateway to external data sources.

- Fetches data from PokeAPI
- Returns raw data to the Usecase
- Encapsulates external API logic

✅ Handles external communication  
✅ Isolates infrastructure concerns  
❌ Does NOT implement business rules  
❌ Does NOT format HTTP responses  

This design allows replacing PokeAPI with:
- A database
- A cache
- A mock service
- Another external provider

Without modifying the Usecase logic.

---

### 4️⃣ Entity Layer (Domain Model Layer)

**Responsibility:**  
Represents pure data structures.

- Contains only state (attributes)
- No behavior
- No business logic
- No framework dependencies

✅ Framework-independent  
✅ Easily testable  
✅ Reusable across layers  

Entities represent the core data model of the application.

---

# 🔁 End-to-End Execution Example

When a client calls:

```text
GET /berries?limit=5
```


The execution flow is:

1. **Handler**
   - Receives `limit=5`
   - Validates the parameter
   - Calls `GetBerriesUseCase.execute(5)`

2. **Usecase**
   - Calls `BerryRepository.fetch_berries(5)`
   - Processes raw data
   - Creates `Berry` entities
   - Returns a list of entities

3. **Repository**
   - Calls PokeAPI
   - Retrieves raw JSON
   - Returns raw berry data

4. **Handler**
   - Converts Entities to JSON
   - Returns HTTP response

---

# ✅ Architectural Benefits

- ✅ Clear separation of concerns
- ✅ Business logic independent from framework
- ✅ Infrastructure easily replaceable
- ✅ Improved testability
- ✅ Scalability for future features
- ✅ Cleaner codebase

---

# 🧠 Why This Architecture Matters

This structure prevents:

- Mixing HTTP logic with business logic
- Hard-coding infrastructure dependencies
- Tight coupling between layers
- Difficult unit testing

Instead, it promotes:

- Maintainability
- Extensibility
- Clean dependency direction (outer layers depend on inner layers)

---

# 📐 Dependency Direction

Dependencies always point inward:
```text
Handler → Usecase → Repository
↓
Entity
```


- The **Usecase** depends on the Repository abstraction.
- The **Handler** depends on the Usecase.
- The **Entity** is independent and shared.
- The Repository does not depend on the Handler.
- The Usecase does not depend on FastAPI.

---

This ensures a clean, modular, and production-ready architecture.
