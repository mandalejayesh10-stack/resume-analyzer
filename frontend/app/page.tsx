'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Upload, FileText, Target, Sparkles } from 'lucide-react'
import FileUpload from '@/components/FileUpload'

export default function Home() {
  const router = useRouter()
  const [isUploading, setIsUploading] = useState(false)

  const handleUploadSuccess = (data: any) => {
    // Navigate to analyzer page with resume data
    router.push(`/analyzer?id=${data.id}`)
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-primary-600 to-primary-800 text-white py-20">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="text-center">
            <h1 className="text-5xl font-bold mb-6">
              AI Resume Analyzer
            </h1>
            <p className="text-xl mb-8 text-primary-100 max-w-2xl mx-auto">
              Get instant AI-powered feedback on your resume. Optimize for ATS, improve your content, and land more interviews.
            </p>
            
            {/* Upload Section */}
            <div className="max-w-2xl mx-auto">
              <FileUpload 
                onUploadSuccess={handleUploadSuccess}
                isUploading={isUploading}
                setIsUploading={setIsUploading}
              />
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 max-w-6xl">
          <h2 className="text-3xl font-bold text-center mb-12">
            Powerful Features
          </h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="card text-center">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <FileText className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold mb-3">Resume Analysis</h3>
              <p className="text-gray-600">
                Get detailed feedback with 15+ checks covering formatting, keywords, action verbs, and more.
              </p>
            </div>

            <div className="card text-center">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Target className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold mb-3">Job Matching</h3>
              <p className="text-gray-600">
                Compare your resume against job descriptions and identify missing keywords and skills.
              </p>
            </div>

            <div className="card text-center">
              <div className="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Sparkles className="w-8 h-8 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold mb-3">AI Generation</h3>
              <p className="text-gray-600">
                Generate professional resumes and cover letters tailored to your experience and target role.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-20 bg-gray-100">
        <div className="container mx-auto px-4 max-w-6xl">
          <h2 className="text-3xl font-bold text-center mb-12">
            How It Works
          </h2>
          
          <div className="grid md:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="w-12 h-12 bg-primary-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                1
              </div>
              <h3 className="font-semibold mb-2">Upload Resume</h3>
              <p className="text-sm text-gray-600">Upload your PDF or DOCX resume file</p>
            </div>

            <div className="text-center">
              <div className="w-12 h-12 bg-primary-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                2
              </div>
              <h3 className="font-semibold mb-2">AI Analysis</h3>
              <p className="text-sm text-gray-600">Our AI analyzes your resume content</p>
            </div>

            <div className="text-center">
              <div className="w-12 h-12 bg-primary-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                3
              </div>
              <h3 className="font-semibold mb-2">Get Feedback</h3>
              <p className="text-sm text-gray-600">Receive detailed scores and suggestions</p>
            </div>

            <div className="text-center">
              <div className="w-12 h-12 bg-primary-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">
                4
              </div>
              <h3 className="font-semibold mb-2">Improve</h3>
              <p className="text-sm text-gray-600">Apply improvements and land interviews</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
