'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import axios from 'axios'
import { FileText, Calendar, TrendingUp, Loader2 } from 'lucide-react'
import FileUpload from '@/components/FileUpload'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export default function DashboardPage() {
  const router = useRouter()
  const [resumes, setResumes] = useState<any[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [isUploading, setIsUploading] = useState(false)

  useEffect(() => {
    fetchResumes()
  }, [])

  const fetchResumes = async () => {
    try {
      const response = await axios.get(`${API_URL}/resumes`)
      setResumes(response.data)
    } catch (err) {
      console.error('Failed to fetch resumes:', err)
    } finally {
      setIsLoading(false)
    }
  }

  const handleUploadSuccess = (data: any) => {
    router.push(`/analyzer?id=${data.id}`)
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    })
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-6xl">
      <h1 className="text-3xl font-bold mb-8">Dashboard</h1>

      {/* Upload Section */}
      <div className="card mb-8">
        <h2 className="text-xl font-semibold mb-4">Upload New Resume</h2>
        <FileUpload
          onUploadSuccess={handleUploadSuccess}
          isUploading={isUploading}
          setIsUploading={setIsUploading}
        />
      </div>

      {/* Analysis History */}
      <div className="card">
        <h2 className="text-xl font-semibold mb-6">Analysis History</h2>

        {isLoading ? (
          <div className="text-center py-12">
            <Loader2 className="w-12 h-12 text-primary-600 animate-spin mx-auto mb-4" />
            <p className="text-gray-600">Loading your resumes...</p>
          </div>
        ) : resumes.length === 0 ? (
          <div className="text-center py-12 text-gray-500">
            <FileText className="w-16 h-16 mx-auto mb-4 opacity-50" />
            <p className="text-lg mb-2">No resumes uploaded yet</p>
            <p className="text-sm">Upload your first resume to get started</p>
          </div>
        ) : (
          <div className="space-y-4">
            {resumes.map((resume) => (
              <div
                key={resume.id}
                className="border border-gray-200 rounded-lg p-4 hover:border-primary-400 transition-colors cursor-pointer"
                onClick={() => router.push(`/analyzer?id=${resume.id}`)}
              >
                <div className="flex items-start justify-between">
                  <div className="flex items-start space-x-4 flex-1">
                    <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                      <FileText className="w-6 h-6 text-primary-600" />
                    </div>
                    
                    <div className="flex-1">
                      <h3 className="font-semibold text-lg mb-1">{resume.filename}</h3>
                      
                      <div className="flex items-center space-x-4 text-sm text-gray-600">
                        <span className="flex items-center">
                          <Calendar className="w-4 h-4 mr-1" />
                          {formatDate(resume.created_at)}
                        </span>
                        
                        {resume.score && (
                          <span className="flex items-center">
                            <TrendingUp className="w-4 h-4 mr-1" />
                            Score: {resume.score}/100
                          </span>
                        )}
                      </div>
                    </div>
                  </div>

                  {resume.score && (
                    <div className="text-right">
                      <div className={`text-2xl font-bold ${
                        resume.score >= 80 ? 'text-green-600' :
                        resume.score >= 60 ? 'text-yellow-600' :
                        'text-red-600'
                      }`}>
                        {resume.score}
                      </div>
                      <div className="text-xs text-gray-500">Resume Score</div>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
