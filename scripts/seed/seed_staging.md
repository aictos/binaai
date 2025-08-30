# Staging Seed

Instructions for seeding staging environment with sample data.

## Prerequisites

1. Supabase project created with buckets:
   - `uploads` - for user-uploaded media
   - `processed` - for processed output videos
   - `public-samples` - for royalty-free sample content

2. Environment variables configured in Render dashboard

## Seeding Steps

### 1. Upload Sample Media

Upload the following royalty-free content to `public-samples` bucket:

- **sample-video.mp4** - 10-second video clip (landscape orientation)
- **sample-image-1.jpg** - Person in motion (for pose estimation demo)  
- **sample-image-2.jpg** - Scene with multiple objects (for object detection demo)

### 2. Create Sample Pipeline

Via the web UI at staging.binaai.ai:

1. Navigate to `/canvas`
2. Create pipeline with nodes:
   - Media In (input) → ObjectDetect (YOLO) → PoseEstimate (BlazePose) → Export (output)
3. Save the pipeline
4. Run browser preview with sample media

### 3. Test API Endpoints

Verify the following endpoints work:

```bash
# Health check
curl https://api-staging.binaai.ai/healthz

# Create pipeline
curl -X POST https://api-staging.binaai.ai/v0/pipelines \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Pipeline", "nodes": [], "edges": []}'

# Upload URL (will return placeholder in dev)
curl -X POST https://api-staging.binaai.ai/v0/upload-url
```

### 4. Verify End-to-End Flow

1. Login/signup via Supabase Auth
2. Open canvas and load sample pipeline
3. Upload sample media or use pre-loaded samples
4. Run pipeline and verify processing status
5. Download/preview exported result

## Sample Data Sources

Use royalty-free content from:
- [Pexels](https://pexels.com) - Videos and images
- [Unsplash](https://unsplash.com) - High-quality images
- [Pixabay](https://pixabay.com) - Videos and images

Ensure all content is:
- Under 50MB per file
- Common formats (MP4, JPG, PNG)
- Appropriate for AI processing demos
