#!/bin/bash

# Binaai MVP v0 Bootstrap Script
# Run this script to set up the development environment

set -e

echo "🚀 Bootstrapping Binaai MVP v0..."

# Check if pnpm is available
if ! command -v pnpm &> /dev/null; then
    echo "📦 Enabling corepack and installing pnpm..."
    corepack enable
fi

# Setup pnpm if needed
echo "📦 Setting up package manager..."
if ! command -v pnpm &> /dev/null; then
    corepack prepare pnpm@latest --activate
fi

# Install global dependencies (skip if no global bin dir)
echo "📦 Installing global dependencies..."
pnpm install -g concurrently 2>/dev/null || echo "Skipping global install - will use npx instead"

# Install web dependencies
echo "🌐 Installing web app dependencies..."
cd apps/web
pnpm install
cd ../..

# Install API dependencies
echo "🐍 Installing API dependencies..."
cd apps/api
if command -v python3 &> /dev/null; then
    python3 -m pip install -r requirements.txt
elif command -v python &> /dev/null; then
    python -m pip install -r requirements.txt
else
    echo "❌ Python not found. Please install Python 3.11+ and try again."
    exit 1
fi
cd ../..

# Copy environment files
echo "⚙️ Setting up environment files..."
cp apps/web/env.example apps/web/.env.local
cp apps/api/env.example apps/api/.env

echo "✅ Bootstrap complete!"
echo ""
echo "📋 Next steps:"
echo "1. Configure environment variables in apps/web/.env.local and apps/api/.env"
echo "2. Run 'pnpm dev' to start both services"
echo "3. Visit http://localhost:3000 to see the app"
echo "4. Visit http://localhost:3000/canvas to see the pipeline canvas"
echo ""
echo "🔗 Useful commands:"
echo "  pnpm dev          # Start both web and API"
echo "  pnpm dev:web      # Start web only"
echo "  pnpm dev:api      # Start API only"
