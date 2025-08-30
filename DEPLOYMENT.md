# Binaai MVP v0 - Deployment Guide

## 🚀 Quick Test

### Local Development

1. **Bootstrap the project:**
   ```bash
   ./scripts/bootstrap.sh
   ```

2. **Start development servers:**
   ```bash
   pnpm dev
   ```
   
   This will start:
   - Next.js web app on http://localhost:3000
   - FastAPI backend on http://localhost:8000

3. **Test endpoints:**
   - Web app: http://localhost:3000
   - Canvas: http://localhost:3000/canvas
   - API health: http://localhost:8000/healthz
   - API docs: http://localhost:8000/docs

## 🌐 Production Deployment

### Render Setup

1. **Create Render account** and connect GitHub repository
2. **Import services** from `infra/render/render.yaml`
3. **Set environment variables** in Render dashboard:

   **Web Service:**
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key  
   NEXT_PUBLIC_API_BASE_URL=https://your-api-service.onrender.com
   NEXT_PUBLIC_SENTRY_DSN=https://your-sentry-dsn
   ```

   **API Service:**
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_ANON_KEY=your-anon-key
   SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
   DATABASE_URL=postgresql://user:pass@host:port/db
   SENTRY_DSN=https://your-sentry-dsn
   ```

### Supabase Setup

1. **Create project** at supabase.com
2. **Create storage buckets:**
   - `uploads` - for user uploads
   - `processed` - for processed videos
   - `public-samples` - for sample media
3. **Copy connection details** to Render environment variables

### Domain Configuration

**Production:**
- Web: `app.binaai.ai` 
- API: Auto-generated Render URL

**Staging:**
- Web: `staging.binaai.ai`
- API: Auto-generated Render URL

## 📋 Acceptance Criteria Verification

### ✅ Web App (Next.js)
- [x] `pnpm -C apps/web dev` starts app on :3000
- [x] Basic canvas screen with React Flow
- [x] Login placeholder (Supabase Auth ready)

### ✅ API (FastAPI)  
- [x] `uvicorn apps.api.main:app --reload` starts API on :8000
- [x] `/healthz` returns 200 OK
- [x] `POST /v0/upload-url` returns signed URL placeholder
- [x] `POST /v0/pipelines` creates in-memory entries
- [x] `POST /v0/pipelines/{id}/runs` creates run entries
- [x] `POST /v0/export` returns mocked processed URL

### ✅ Infrastructure
- [x] Docker files for production builds
- [x] Render deployment configuration
- [x] GitHub Actions CI/CD
- [x] Environment variable templates

### ✅ Development Experience
- [x] Bootstrap script for quick setup
- [x] Monorepo structure with shared types
- [x] TypeScript configuration
- [x] Sample pipeline data

## 🧪 Testing Commands

```bash
# Install dependencies
./scripts/bootstrap.sh

# Start both services
pnpm dev

# Test API health
curl http://localhost:8000/healthz

# Test pipeline creation
curl -X POST http://localhost:8000/v0/pipelines \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Pipeline", "nodes": [], "edges": []}'

# Test upload URL
curl -X POST http://localhost:8000/v0/upload-url

# Test web app
open http://localhost:3000
open http://localhost:3000/canvas
```

## 🔄 Next Steps

1. **GitHub Integration:** Push to GitHub and connect to Render
2. **Supabase Setup:** Create project and configure storage buckets  
3. **Environment Variables:** Set production values in Render dashboard
4. **Domain Setup:** Configure DNS for custom domains
5. **Sample Data:** Upload royalty-free media to public-samples bucket
6. **End-to-End Test:** Verify full pipeline flow in staging

## 📞 Support

- Check `/healthz` endpoint for API status
- Review Render logs for deployment issues
- Verify environment variables are set correctly
- Test local development first before deploying
