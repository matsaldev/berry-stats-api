# 🧪 Running the Test Suite

This project includes a complete test suite using **pytest**, mirroring the application’s Clean Architecture structure.

---

## ✅ Run All Tests

From the project root directory:

```bash
pytest
```

---

## ✅ Run Tests with Verbose Output

```bash
pytest -v
```

This displays detailed information about each test.

---

## ✅ Run Tests with Output (Print Statements Enabled)

```bash
pytest -v -s
```

---

## 📁 Test Structure

The `tests/` directory mirrors the `app/` directory:

```
tests/
├── config/
├── entity/
├── handler/
├── infrastructure/
├── repository/
├── usecase/
└── test_main.py
```

This ensures clean separation and alignment with the application architecture.

---

## ✅ Expected Output

If all tests pass, you should see:

```
================== X passed in Y.YYs ==================
```

---

## ⚙️ Configuration

Test behavior is configured in:

```
pytest.ini
```

Located at the project root.

---

✅ The test suite covers:
- Usecase logic
- Repository behavior
- Infrastructure components
- Cache logic
- API endpoints (JSON and SVG)
- Application bootstrap

---

Run tests before pushing changes to ensure stability and correctness.