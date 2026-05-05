# AI Resume Analyzer - Frontend

Next.js frontend for AI-powered resume analysis.

## Setup

1. Install dependencies:
```bash
npm install
# or
yarn install
```

2. Configure environment:
```bash
cp .env.local.example .env.local
# Edit .env.local with your API URL
```

3. Run development server:
```bash
npm run dev
# or
yarn dev
```

4. Open http://localhost:3000

## Pages

### Home (`/`)
- Hero section with value proposition
- File upload component
- Features overview
- How it works section

### Analyzer (`/analyzer`)
- Resume upload
- Real-time analysis
- Score display (Resume & ATS)
- Detailed checks (15+)
- Bullet point improvements
- Actionable suggestions

### Job Match (`/job-match`)
- Resume upload
- Job description input
- Match score calculation
- Missing keywords identification
- Recommendations

### AI Writer (`/ai-writer`)
- Resume generator (role, skills, experience)
- Cover letter generator (resume + job description)
- Formatted output display

### Dashboard (`/dashboard`)
- Upload new resume
- Analysis history
- Quick access to previous analyses

## Components

### FileUpload
- Drag & drop interface
- File type validation (PDF, DOCX)
- Upload progress indicator
- Error handling

### Navbar
- Navigation links
- Responsive design
- Brand identity

## Styling

- Tailwind CSS for utility-first styling
- Custom components in `globals.css`
- Responsive design for all screen sizes
- Clean, professional color scheme

## API Integration

All API calls use Axios with base URL from environment:
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
```

## Build & Deploy

### Development
```bash
npm run dev
```

### Production Build
```bash
npm run build
npm start
```

### Deploy to Vercel
1. Push to GitHub
2. Import project in Vercel
3. Set `NEXT_PUBLIC_API_URL` environment variable
4. Deploy

## Environment Variables

- `NEXT_PUBLIC_API_URL`: Backend API URL (required)

## Features

✅ Server-side rendering with Next.js 14
✅ TypeScript for type safety
✅ Responsive design with Tailwind CSS
✅ File upload with drag & drop
✅ Real-time loading states
✅ Error handling and validation
✅ Clean, professional UI
✅ Fast page navigation
✅ SEO optimized

## Performance

- Optimized images and assets
- Code splitting
- Lazy loading
- Minimal bundle size
- Fast page loads
