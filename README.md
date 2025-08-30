# Binaai MVP v0

A production-ready monorepo for browser-based AI video processing pipelines.

## 🚀 Quick Start

### Prerequisites

- Node.js 20+
- Python 3.11+
- pnpm (via corepack)

### Local Development

1. **Bootstrap the project:**
   ```bash
   corepack enable
   pnpm install -g concurrently
   ```

2. **Install dependencies:**
   ```bash
   # Web app
   cd apps/web && pnpm install && cd -
   
   # API
   cd apps/api && pip install -r requirements.txt && cd -
   ```

3. **Start development servers:**
   ```bash
   # Both services (recommended)
   pnpm dev
   
   # Or individually:
   pnpm dev:web   # Next.js on :3000
   pnpm dev:api   # FastAPI on :8000
   ```

4. **Verify setup:**
   - Web: http://localhost:3000
   - API health: http://localhost:8000/healthz
   - Canvas: http://localhost:3000/canvas

## 🏗️ Architecture

```
binaai/
├── apps/
│   ├── web/          # Next.js frontend
│   └── api/          # FastAPI backend
├── packages/
│   └── shared/       # Shared types & schemas
├── infra/
│   ├── docker/       # Dockerfiles
│   └── render/       # Render.com config
├── scripts/
│   └── seed/         # Staging seed data
└── .github/
    └── workflows/    # CI/CD pipelines
```

## 🛠️ Tech Stack

- **Frontend:** Next.js 14, React 18, Tailwind CSS, React Flow
- **Backend:** FastAPI, Python 3.11, Uvicorn
- **Auth/DB/Storage:** Supabase
- **Deployment:** Render.com
- **CI/CD:** GitHub Actions
- **Package Manager:** pnpm

## 🌐 Environment Variables

### Web App (`apps/web`)
```bash
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
NEXT_PUBLIC_SENTRY_DSN=your_sentry_dsn
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### API (`apps/api`)
```bash
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
SENTRY_DSN=your_sentry_dsn
DATABASE_URL=your_database_url
SUPABASE_BUCKET_UPLOADS=uploads
SUPABASE_BUCKET_PROCESSED=processed
SUPABASE_BUCKET_PUBLIC=public-samples
```

## 📦 API Endpoints

### Core Endpoints
- `GET /healthz` - Health check
- `POST /v0/pipelines` - Create pipeline
- `GET /v0/pipelines/{id}` - Get pipeline
- `POST /v0/pipelines/{id}/runs` - Create run
- `GET /v0/runs/{id}` - Get run status

### Media Endpoints  
- `POST /v0/upload-url` - Get signed upload URL
- `POST /v0/export` - Export processed video

## 🚢 Deployment

### Render.com Setup

1. **Connect GitHub repository** to Render
2. **Import services** from `infra/render/render.yaml`
3. **Set environment variables** in Render dashboard
4. **Configure domains:**
   - Production: `app.binaai.ai`
   - Staging: `staging.binaai.ai`

### Supabase Setup

1. **Create new project** at supabase.com
2. **Create storage buckets:**
   - `uploads` - User uploads
   - `processed` - Processed videos  
   - `public-samples` - Sample media
3. **Copy keys** to environment variables

## 🧪 Development Notes

### MVP v0 Constraints
- **No queues:** Simple background tasks only
- **No SSE:** Polling for run status
- **No payments:** Stripe integration in future phases
- **Local dev:** Works without external dependencies

### Browser AI Models
- **YOLO:** Object detection (placeholder)
- **BlazePose:** Pose estimation (placeholder)
- **ONNX Runtime:** For browser inference

### File Processing
- **ffmpeg:** Video processing (CPU only)
- **MoviePy:** Python video manipulation
- **Supabase Storage:** File uploads/downloads

## 🔄 Workflow

1. **Upload media** → Supabase Storage
2. **Create pipeline** → Define processing nodes
3. **Run pipeline** → Background processing
4. **Poll status** → Check progress
5. **Download result** → Processed video

## 📋 Next Phases

- [ ] Real Supabase signed URLs
- [ ] Server-side AI processing  
- [ ] SSE + Celery workers
- [ ] Caption nodes (BLIP-2/Florence-2)
- [ ] Stripe billing integration
- [ ] GPU workers (Modal/Runpod)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/name`
3. Make changes and test locally
4. Submit pull request

## 📄 License

Private repository - All rights reserved.
