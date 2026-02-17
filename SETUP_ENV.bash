#!/usr/bin/env bash

set -e

echo "🚀 Setting up Berry Stats API environment..."
echo ""

# -----------------------------------------
# 1️⃣ Ensure 'python' exists
# -----------------------------------------

if ! command -v python &> /dev/null; then
    echo "❌ 'python' command not found."
    echo "Please install Python 3.12 and ensure it is in your PATH."
    exit 1
fi

# -----------------------------------------
# 2️⃣ Ensure Python version is 3.12
# -----------------------------------------

PYTHON_VERSION=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')

if [[ "$PYTHON_VERSION" != "3.12" ]]; then
    echo "❌ Python 3.12 is required."
    echo "Detected version: $PYTHON_VERSION"
    echo ""
    echo "Please install Python 3.12 and ensure 'python' points to it."
    exit 1
fi

echo "✅ Using Python $PYTHON_VERSION"
echo ""

# -----------------------------------------
# 3️⃣ Check if already inside a virtual environment
# -----------------------------------------

if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "✅ Already running inside virtual environment:"
    echo "   $VIRTUAL_ENV"
    echo ""
    echo "Skipping venv creation."
else

    # -----------------------------------------
    # 4️⃣ Check if venv directory exists
    # -----------------------------------------

    if [ -d "venv" ]; then
        echo "✅ Existing virtual environment detected at ./venv"
        echo "Activating it..."
        source venv/bin/activate
    else
        echo "📦 Creating new virtual environment..."
        python -m venv venv
        source venv/bin/activate
    fi
fi

echo "✅ Virtual environment ready"
echo ""

# -----------------------------------------
# 5️⃣ Upgrade pip
# -----------------------------------------

echo "⬆️ Upgrading pip..."
python.exe -m pip install --upgrade pip

echo ""

# -----------------------------------------
# 6️⃣ Install dependencies
# -----------------------------------------

if [ -f "requirements.txt" ]; then
    echo "📥 Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found. Installing core dependencies..."
    pip install fastapi uvicorn httpx
fi

echo ""
echo "✅ Environment setup complete!"
echo ""
echo "To activate the environment later (if not active):"
echo "  source venv/bin/activate"
echo ""
echo "To start the server:"
echo "  uvicorn app.main:app --reload"
echo ""
echo "Open:"
echo "  http://127.0.0.1:8000/docs"
echo ""
