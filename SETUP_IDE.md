# 🧠 Run & Debug the Project in VS Code

Follow these steps to configure and debug the project inside **Visual Studio Code**.

## 📚 Quick Navigation

- [🧠 Run & Debug the Project in PyCharm](#-run-the-project-in-pycharm)

---

## ✅ 1️⃣ Open the Project

- Open **VS Code**
- Click **File → Open Folder**
- Select:

```
berry_stats_api
```

---

## ✅ 2️⃣ Select Python 3.12 Interpreter

Press:

```
Ctrl + Shift + P
```

Type:

```
Python: Select Interpreter
```

Choose:

```
berry_stats_api/venv/bin/python
```

✅ Must be **Python 3.12**

If the virtual environment doesn’t exist:

```bash
chmod +x SETUP_ENV.bash && ./SETUP_ENV.bash
```

---

## ✅ 3️⃣ Create Debug Configuration (`launch.json`)

Go to:

```
Run → Add Configuration…
```

Choose:

```
Python
```

Replace the generated content with:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI (Debug)",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "app.main:app",
        "--reload"
      ],
      "cwd": "${workspaceFolder}",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      },
      "console": "integratedTerminal"
    }
  ]
}
```

✅ This ensures:
- Correct module execution
- Proper PYTHONPATH
- Reload support
- Debug breakpoints working

---

## ✅ 4️⃣ Start Debugging 🚀

Go to the **Run & Debug** panel and select:

```
FastAPI (Debug)
```

Click ▶ **Start Debugging**

✅ You can now use breakpoints.

---

## ✅ 5️⃣ Open Swagger UI

Open your browser:

```
http://127.0.0.1:8000/docs
```

✅ API documentation should load.

---

🎉 You’re ready to develop and debug!

---

# 🧠 Run the Project in PyCharm

Follow these simple steps to configure and run the project inside **PyCharm**.

## 📚 Quick Navigation

- [🧠 Run & Debug the Project in VS Code](#-run--debug-the-project-in-vs-code)

---

## ✅ 1️⃣ Open the Project

- Open **PyCharm**
- Click **Open**
- Select the project root folder:

```
berry_stats_api
```

---

## ✅ 2️⃣ Configure the Python Interpreter (3.12 Required)

Go to:

```
File → Settings → Project → Python Interpreter
```

- Click ⚙️ → **Add Interpreter**
- Choose **Existing Environment**
- Select:

```
berry_stats_api/venv/bin/python
```

✅ Make sure it shows **Python 3.12**

---

## ✅ 3️⃣ Mark the Project Root as Sources Root

In the Project panel:

- Right-click `berry_stats_api`
- Click:

```
Mark Directory as → Sources Root
```

✅ The folder should turn blue

---

## ✅ 4️⃣ Create a Run Configuration

Go to:

```
Run → Edit Configurations → ➕ Add New → Python
```

Configure:

- **Name:** `Berry Stats API`
- **Run:** Module name
- **Module:** `uvicorn`
- **Parameters:**  
  ```
  app.main:app --reload
  ```
- **Working directory:**  
  ```
  berry_stats_api
  ```
- **Interpreter:** Select your `venv`

Click **Apply → OK**

---

## ✅ 5️⃣ Run the Application 🚀

Click the green ▶ button.

Then open:

```
http://127.0.0.1:8000/docs
```

You should see the Swagger UI ✅

---

🎉 You're ready to develop!

---