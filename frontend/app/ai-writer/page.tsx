'use client'

import { useState } from 'react'
import axios from 'axios'
import { Sparkles, Loader2, FileText, Mail } from 'lucide-react'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export default function AIWriterPage() {
  const [activeTab, setActiveTab] = useState<'resume' | 'cover-letter'>('resume')

  // Resume Generator State
  const [role, setRole] = useState('')
  const [skills, setSkills] = useState('')
  const [experience, setExperience] = useState('')
  const [generatedResume, setGeneratedResume] = useState<any>(null)
  const [isGeneratingResume, setIsGeneratingResume] = useState(false)

  // Cover Letter State
  const [resumeText, setResumeText] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [generatedCoverLetter, setGeneratedCoverLetter] = useState('')
  const [isGeneratingCoverLetter, setIsGeneratingCoverLetter] = useState(false)

  const [error, setError] = useState<string | null>(null)

  const handleGenerateResume = async () => {
    if (!role || !skills) {
      setError('Please provide at least role and skills')
      return
    }

    setIsGeneratingResume(true)
    setError(null)

    try {
      const response = await axios.post(`${API_URL}/generate/resume`, {
        role,
        skills,
        experience,
      })
      setGeneratedResume(response.data)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Resume generation failed')
    } finally {
      setIsGeneratingResume(false)
    }
  }

  const handleGenerateCoverLetter = async () => {
    if (!resumeText || !jobDescription) {
      setError('Please provide both resume text and job description')
      return
    }

    setIsGeneratingCoverLetter(true)
    setError(null)

    try {
      const response = await axios.post(`${API_URL}/generate/cover-letter`, {
        resume_text: resumeText,
        job_description: jobDescription,
      })
      setGeneratedCoverLetter(response.data.cover_letter)
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Cover letter generation failed')
    } finally {
      setIsGeneratingCoverLetter(false)
    }
  }

  return (
    <div className="container mx-auto px-4 py-8 max-w-6xl">
      <div className="text-center mb-8">
        <Sparkles className="w-12 h-12 text-primary-600 mx-auto mb-4" />
        <h1 className="text-3xl font-bold mb-2">AI Writer</h1>
        <p className="text-gray-600">
          Generate professional resumes and cover letters with AI
        </p>
      </div>

      {/* Tabs */}
      <div className="flex space-x-4 mb-8 border-b border-gray-200">
        <button
          onClick={() => setActiveTab('resume')}
          className={`pb-4 px-4 font-medium transition-colors ${
            activeTab === 'resume'
              ? 'text-primary-600 border-b-2 border-primary-600'
              : 'text-gray-600 hover:text-gray-900'
          }`}
        >
          <FileText className="w-5 h-5 inline mr-2" />
          Resume Generator
        </button>
        <button
          onClick={() => setActiveTab('cover-letter')}
          className={`pb-4 px-4 font-medium transition-colors ${
            activeTab === 'cover-letter'
              ? 'text-primary-600 border-b-2 border-primary-600'
              : 'text-gray-600 hover:text-gray-900'
          }`}
        >
          <Mail className="w-5 h-5 inline mr-2" />
          Cover Letter Generator
        </button>
      </div>

      {error && (
        <div className="card bg-red-50 border-red-200 mb-8">
          <p className="text-red-800">{error}</p>
        </div>
      )}

      {/* Resume Generator */}
      {activeTab === 'resume' && (
        <div className="grid lg:grid-cols-2 gap-8">
          <div className="card">
            <h2 className="text-xl font-semibold mb-4">Input Details</h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Target Role *
                </label>
                <input
                  type="text"
                  className="input"
                  placeholder="e.g., Senior Software Engineer"
                  value={role}
                  onChange={(e) => setRole(e.target.value)}
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Skills *
                </label>
                <textarea
                  className="textarea h-24"
                  placeholder="e.g., React, Node.js, Python, AWS, Docker..."
                  value={skills}
                  onChange={(e) => setSkills(e.target.value)}
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Experience (Optional)
                </label>
                <textarea
                  className="textarea h-32"
                  placeholder="Describe your work experience, projects, achievements..."
                  value={experience}
                  onChange={(e) => setExperience(e.target.value)}
                />
              </div>

              <button
                onClick={handleGenerateResume}
                disabled={isGeneratingResume}
                className="btn-primary w-full"
              >
                {isGeneratingResume ? (
                  <>
                    <Loader2 className="w-5 h-5 inline mr-2 animate-spin" />
                    Generating...
                  </>
                ) : (
                  'Generate Resume'
                )}
              </button>
            </div>
          </div>

          <div className="card">
            <h2 className="text-xl font-semibold mb-4">Generated Resume</h2>
            
            {generatedResume ? (
              <div className="space-y-6">
                {/* Summary */}
                {generatedResume.summary && (
                  <div>
                    <h3 className="font-semibold text-sm text-gray-600 mb-2">PROFESSIONAL SUMMARY</h3>
                    <p className="text-sm text-gray-700">{generatedResume.summary}</p>
                  </div>
                )}

                {/* Skills */}
                {generatedResume.skills && generatedResume.skills.length > 0 && (
                  <div>
                    <h3 className="font-semibold text-sm text-gray-600 mb-2">SKILLS</h3>
                    <div className="flex flex-wrap gap-2">
                      {generatedResume.skills.map((skill: string, index: number) => (
                        <span key={index} className="px-3 py-1 bg-primary-100 text-primary-800 rounded-full text-sm">
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {/* Experience */}
                {generatedResume.experience && generatedResume.experience.length > 0 && (
                  <div>
                    <h3 className="font-semibold text-sm text-gray-600 mb-3">EXPERIENCE</h3>
                    <div className="space-y-4">
                      {generatedResume.experience.map((exp: any, index: number) => (
                        <div key={index}>
                          <p className="font-semibold text-sm">{exp.title}</p>
                          <p className="text-sm text-gray-600">{exp.company} • {exp.duration}</p>
                          <ul className="mt-2 space-y-1">
                            {exp.bullets.map((bullet: string, bIndex: number) => (
                              <li key={bIndex} className="text-sm text-gray-700 ml-4">
                                • {bullet}
                              </li>
                            ))}
                          </ul>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Education */}
                {generatedResume.education && generatedResume.education.length > 0 && (
                  <div>
                    <h3 className="font-semibold text-sm text-gray-600 mb-2">EDUCATION</h3>
                    <div className="space-y-2">
                      {generatedResume.education.map((edu: any, index: number) => (
                        <div key={index}>
                          <p className="font-semibold text-sm">{edu.degree}</p>
                          <p className="text-sm text-gray-600">{edu.institution} • {edu.year}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                <FileText className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Your generated resume will appear here</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Cover Letter Generator */}
      {activeTab === 'cover-letter' && (
        <div className="grid lg:grid-cols-2 gap-8">
          <div className="space-y-6">
            <div className="card">
              <h2 className="text-xl font-semibold mb-4">Your Resume</h2>
              <textarea
                className="textarea h-48"
                placeholder="Paste your resume content here..."
                value={resumeText}
                onChange={(e) => setResumeText(e.target.value)}
              />
            </div>

            <div className="card">
              <h2 className="text-xl font-semibold mb-4">Job Description</h2>
              <textarea
                className="textarea h-48"
                placeholder="Paste the job description here..."
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
              />
            </div>

            <button
              onClick={handleGenerateCoverLetter}
              disabled={isGeneratingCoverLetter}
              className="btn-primary w-full"
            >
              {isGeneratingCoverLetter ? (
                <>
                  <Loader2 className="w-5 h-5 inline mr-2 animate-spin" />
                  Generating...
                </>
              ) : (
                'Generate Cover Letter'
              )}
            </button>
          </div>

          <div className="card">
            <h2 className="text-xl font-semibold mb-4">Generated Cover Letter</h2>
            
            {generatedCoverLetter ? (
              <div className="bg-white p-6 border border-gray-200 rounded-lg">
                <pre className="whitespace-pre-wrap text-sm text-gray-700 font-sans">
                  {generatedCoverLetter}
                </pre>
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                <Mail className="w-12 h-12 mx-auto mb-4 opacity-50" />
                <p>Your generated cover letter will appear here</p>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
