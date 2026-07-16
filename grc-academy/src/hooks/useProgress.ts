import { useCallback, useEffect, useState } from 'react'

const STORAGE_KEY = 'grc-academy:completed-lessons'

function readCompleted(): Set<string> {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? new Set(JSON.parse(raw)) : new Set()
  } catch {
    return new Set()
  }
}

function writeCompleted(set: Set<string>) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(set)))
  } catch {
    // localStorage unavailable (private mode, etc.) — progress just won't persist.
  }
}

export function lessonKey(courseSlug: string, moduleSlug: string, lessonSlug: string) {
  return `${courseSlug}/${moduleSlug}/${lessonSlug}`
}

export function useProgress() {
  const [completed, setCompleted] = useState<Set<string>>(() => readCompleted())

  useEffect(() => {
    writeCompleted(completed)
  }, [completed])

  const isCompleted = useCallback((key: string) => completed.has(key), [completed])

  const toggle = useCallback((key: string) => {
    setCompleted((prev) => {
      const next = new Set(prev)
      if (next.has(key)) next.delete(key)
      else next.add(key)
      return next
    })
  }, [])

  const markCompleted = useCallback((key: string) => {
    setCompleted((prev) => {
      if (prev.has(key)) return prev
      const next = new Set(prev)
      next.add(key)
      return next
    })
  }, [])

  return { completed, isCompleted, toggle, markCompleted }
}
