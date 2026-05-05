'use client'

import { useState } from 'react'
import axios from 'axios'
import { Target, Loader2 } from 'lucide-react'
import FileUpload from '@/components/FileUpload'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export default function JobMatchPage() {
  const [resumeText, setResumeText] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [matchResult, setMatchResult] = useState<any>(null)
  const [isMatching, setIsMatching] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [isUploading, setIsUploading] = useState(false)

  const handleUploadSuccess = (data: any) => {
    setResumeText(data.content)
  }

  const handleMatch = async () => {
    if (!resumeText || !jobDescription) {
      setError('Please provide both resume and job description')
      return
    }

    setIsMatching(true)
    setError(null)

    try {
      const response = await axios.post(`${API_URL}/job-match`, {
        resume_text: resumeText,
        job_description: jobDescription,
      })
      setMatchResult(response.data)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Job matching failed')
    } finally {
      setIsMatching(false)
    }
  }

  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-yellow-600'
    return 'text-red-600'
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-7xl">
      <div className="text-center mb-8">
        <Target className="w-12 h-12 text-primary-600 mx-auto mb-4" />
        <h1 className="text-3xl font-bold mb-2">Job Description Matcher</h1>
        <p className="text-gray-600">
          Compare your resume against a job description to see how well you match
        </p>
      </div>

      <div className="grid lg:grid-cols-2 gap-8 mb-8">
        {/* Resume Upload */}
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Your Resume</h2>
          {!resumeText ? (
            <FileUpload
              onUploadSuccess={handleUploadSuccess}
              isUploading={isUploading}
              setIsUploading={setIsUploading}
            />
          ) : (
            <div>
              <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-4">
                <p className="text-sm text-green-800">✓ Resume uploaded successfully</p>
              </div>
              <button
                onClick={() => setResumeText('')}
                className="text-sm text-primary-600 hover:underline"
              >
                Upload different resume
              </button>
            </div>
          )}
        </div>

        {/* Job Description */}
        <div className="card">
          <h2 className="text-xl font-semibold mb-4">Job Description</h2>
          <textarea
            className="textarea h-64"
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />
        </div>
      </div>

      {/* Match Button */}
      <div className="text-center mb-8">
        <button
          onClick={handleMatch}
          disabled={!resumeText || !jobDescription || isMatching}
          className="btn-primary"
        >
          {isMatching ? (
            <>
              <Loader2 className="w-5 h-5 inline mr-2 animate-spin" />
              Analyzing Match...
            </>
          ) : (
            'Analyze Match'
          )}
        </button>
      </div>

      {/* Error */}
      {error && (
        <div className="card bg-red-50 border-red-200 mb-8">
          <p className="text-red-800">{error}</p>
        </div>
      )}

      {/* Results */}
      {matchResult && (
        <div className="space-y-6">
          {/* Match Score */}
          <div className="card text-center">
            <p className="text-lg text-gray-600 mb-2">Match Score</p>
            <p className={`text-6xl font-bold ${getScoreColor(matchResult.match_score)}`}>
              {matchResult.match_score}%
            </p>
          </div>

          <div className="grid lg:grid-cols-2 gap-6">
            {/* Strengths */}
            {matchResult.strengths && matchResult.strengths.length > 0 && (
              <div className="card">
                <h3 className="font-semibold mb-4 text-green-700">✓ Your Strengths</h3>
                <ul className="space-y-2">
                  {matchResult.strengths.map((strength: string, index: number) => (
                    <li key={index} className="flex items-start space-x-2">
                      <span className="text-green-600 mt-1">•</span>
                      <span className="text-sm text-gray-700">{strength}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {/* Skill Gaps */}
            {matchResult.skill_gaps && matchResult.skill_gaps.length > 0 && (
              <div className="card">
                <h3 className="font-semibold mb-4 text-red-700">⚠ Skill Gaps</h3>
                <ul className="space-y-2">
                  {matchResult.skill_gaps.map((gap: string, index: number) => (
                    <li key={index} className="flex items-start space-x-2">
                      <span className="text-red-600 mt-1">•</span>
                      <span className="text-sm text-gray-700">{gap}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          {/* Keywords */}
          <div className="grid lg:grid-cols-2 gap-6">
            {/* Present Keywords */}
            {matchResult.present_keywords && matchResult.present_keywords.length > 0 && (
              <div className="card">
                <h3 className="font-semibold mb-4">Present Keywords</h3>
                <div className="flex flex-wrap gap-2">
                  {matchResult.present_keywords.map((keyword: string, index: number) => (
                    <span
                      key={index}
                      className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm"
                    >
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>
            )}

            {/* Missing Keywords */}
            {matchResult.missing_keywords && matchResult.missing_keywords.length > 0 && (
              <div className="card">
                <h3 className="font-semibold mb-4">Missing Keywords</h3>
                <div className="flex flex-wrap gap-2">
                  {matchResult.missing_keywords.map((keyword: string, index: number) => (
                    <span
                      key={index}
                      className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm"
                    >
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Recommendations */}
          {matchResult.recommendations && matchResult.recommendations.length > 0 && (
            <div className="card">
              <h3 className="font-semibold mb-4">Recommendations</h3>
              <ul className="space-y-3">
                {matchResult.recommendations.map((rec: string, index: number) => (
                  <li key={index} className="flex items-start space-x-2 p-3 bg-blue-50 rounded-lg">
                    <span className="text-primary-600 mt-1">→</span>
                    <span className="text-sm text-gray-700">{rec}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
