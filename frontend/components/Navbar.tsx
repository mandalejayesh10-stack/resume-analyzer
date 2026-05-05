'use client'

import Link from 'next/link'
import { FileText } from 'lucide-react'

export default function Navbar() {
  return (
    <nav className="bg-white border-b border-gray-200">
      <div className="container mx-auto px-4 max-w-6xl">
        <div className="flex items-center justify-between h-16">
          <Link href="/" className="flex items-center space-x-2">
            <FileText className="w-8 h-8 text-primary-600" />
            <span className="text-xl font-bold text-gray-900">
              AI Resume Analyzer
            </span>
          </Link>
          
          <div className="flex items-center space-x-6">
            <Link 
              href="/analyzer" 
              className="text-gray-600 hover:text-primary-600 transition-colors"
            >
              Analyzer
            </Link>
            <Link 
              href="/job-match" 
              className="text-gray-600 hover:text-primary-600 transition-colors"
            >
              Job Match
            </Link>
            <Link 
              href="/ai-writer" 
              className="text-gray-600 hover:text-primary-600 transition-colors"
            >
              AI Writer
            </Link>
            <Link 
              href="/dashboard" 
              className="text-gray-600 hover:text-primary-600 transition-colors"
            >
              Dashboard
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}
