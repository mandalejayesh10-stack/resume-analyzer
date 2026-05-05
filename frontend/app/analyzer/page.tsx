'use client'

import { useState, useEffect, Suspense } from 'react'
import { useSearchParams } from 'next/navigation'
import axios from 'axios'
import { CheckCircle, XCircle, AlertCircle, Loader2 } from 'lucide-react'
import FileUpload from '@/components/FileUpload'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

function AnalyzerContent() {
  const searchParams = useSearchParams()
  const resumeId = searchParams.get('id')

  const [resumeText, setResumeText] = useState('')
  const [analysis, setAnalysis] = useState<any>(null)
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [uploadedFile, setUploadedFile] = useState<any>(null)
  const [isUploading, setIsUploading] = useState(false)

  useEffect(() => {
    if (resumeId) {
      fetchResume(resumeId)
    }
  }, [resumeId])

  const fetchResume = async (id: string) => {
    try {
      const response = await axios.get(`${API_URL}/resumes/${id}`)
      setResumeText(response.data.content)
      setUploadedFile(response.data)
      // Auto-analyze
      analyzeResume(response.data.content)
    } catch (err) {
      setError('Failed to fetch resume')
    }
  }

  const analyzeResume = async (text: string) => {
    setIsAnalyzing(true)
    setError(null)

    try {
      const response = await axios.post(`${API_URL}/analyze`, {
        resume_text: text,
      })
      setAnalysis(response.data)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Analysis failed')
    } finally {
      setIsAnalyzing(false)
    }
  }

  const handleUploadSuccess = (data: any) => {
    setUploadedFile(data)
    setResumeText(data.content)
    analyzeResume(data.content)
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'pass':
        return <CheckCircle className="w-5 h-5 text-green-600" />
      case 'warning':
        return <AlertCircle className="w-5 h-5 text-yellow-600" />
      case 'fail':
        return <XCircle className="w-5 h-5 text-red-600" />
      default:
        return null
    }
  }

  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-yellow-600'
    return 'text-red-600'
  }

  if (!uploadedFile) {
    return (
      <div className="container mx-auto px-4 py-12 max-w-4xl">
        <h1 className="text-3xl font-bold mb-8 text-center">Resume Analyzer</h1>
        <FileUpload
          onUploadSuccess={handleUploadSuccess}
          isUploading={isUploading}
          setIsUploading={setIsUploading}
        />
      </div>
    )
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-7xl">
      <h1 className="text-3xl font-bold mb-8">Resume Analysis</h1>

      <div className="grid lg:grid-cols-2 gap-8">
        {/* Left: Resume Preview */}
        <div>
          <div className="card">
            <h2 className="text-xl font-semibold mb-4">Resume Content</h2>
            <div className="bg-gray-50 p-4 rounded-lg max-h-[600px] overflow-y-auto">
              <pre className="whitespace-pre-wrap text-sm text-gray-700 font-sans">
                {resumeText}
              </pre>
            </div>
          </div>
        </div>

        {/* Right: Analysis Results */}
        <div>
          {isAnalyzing ? (
            <div className="card text-center py-12">
              <Loader2 className="w-12 h-12 text-primary-600 animate-spin mx-auto mb-4" />
              <p className="text-lg font-medium mb-2">Analyzing your resume...</p>
              <p className="text-sm text-gray-600">This may take a few moments</p>
            </div>
          ) : analysis ? (
            <div className="space-y-6">
              {/* Scores */}
              <div className="grid grid-cols-2 gap-4">
                <div className="card text-center">
                  <p className="text-sm text-gray-600 mb-2">Resume Score</p>
                  <p className={`text-4xl font-bold ${getScoreColor(analysis.score)}`}>
                    {analysis.score}
                  </p>
                  <p className="text-xs text-gray-500 mt-1">out of 100</p>
                </div>
                <div className="card text-center">
                  <p className="text-sm text-gray-600 mb-2">ATS Score</p>
                  <p className={`text-4xl font-bold ${getScoreColor(analysis.ats_score)}`}>
                    {analysis.ats_score}
                  </p>
                  <p className="text-xs text-gray-500 mt-1">out of 100</p>
                </div>
              </div>

              {/* Summary */}
              {analysis.summary && (
                <div className="card">
                  <h3 className="font-semibold mb-2">Summary</h3>
                  <p className="text-sm text-gray-700">{analysis.summary}</p>
                </div>
              )}

              {/* Checks */}
              {analysis.checks && analysis.checks.length > 0 && (
                <div className="card">
                  <h3 className="font-semibold mb-4">Detailed Checks</h3>
                  <div className="space-y-3">
                    {analysis.checks.map((check: any, index: number) => (
                      <div key={index} className="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg">
                        {getStatusIcon(check.status)}
                        <div className="flex-1">
                          <p className="font-medium text-sm">{check.name}</p>
                          <p className="text-xs text-gray-600 mt-1">{check.message}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Weak Bullets */}
              {analysis.weak_bullets && analysis.weak_bullets.length > 0 && (
                <div className="card">
                  <h3 className="font-semibold mb-4">Bullet Point Improvements</h3>
                  <div className="space-y-4">
                    {analysis.weak_bullets.map((bullet: any, index: number) => (
                      <div key={index} className="border-l-4 border-yellow-400 pl-4">
                        <p className="text-sm text-gray-600 mb-2">
                          <span className="font-medium">Original:</span> {bullet.original}
                        </p>
                        <p className="text-sm text-green-700">
                          <span className="font-medium">Improved:</span> {bullet.improved}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Suggestions */}
              {analysis.suggestions && analysis.suggestions.length > 0 && (
                <div className="card">
                  <h3 className="font-semibold mb-4">Suggestions</h3>
                  <ul className="space-y-2">
                    {analysis.suggestions.map((suggestion: string, index: number) => (
                      <li key={index} className="flex items-start space-x-2">
                        <span className="text-primary-600 mt-1">•</span>
                        <span className="text-sm text-gray-700">{suggestion}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ) : error ? (
            <div className="card bg-red-50 border-red-200">
              <p className="text-red-800">{error}</p>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  )
}

export default function AnalyzerPage() {
  return (
    <Suspense fallback={
      <div className="container mx-auto px-4 py-12 text-center">
        <Loader2 className="w-12 h-12 text-primary-600 animate-spin mx-auto" />
      </div>
    }>
      <AnalyzerContent />
    </Suspense>
  )
}
