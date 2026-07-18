export interface Lesson {
  slug: string
  title: string
  minutes: number
}

export interface Module {
  slug: string
  title: string
  description: string
  lessons: Lesson[]
}

export interface Course {
  slug: string
  title: string
  subtitle: string
  description: string
  modules: Module[]
}

// moduleSlug -> lessonSlug -> raw Markdown content, loaded lazily per course
// (see content/contentLoaders.ts) so a course's lesson text isn't bundled
// until someone actually opens one of its lessons.
export type CourseContent = Record<string, Record<string, string>>

export interface FlatLesson {
  moduleSlug: string
  moduleTitle: string
  lesson: Lesson
  index: number
}

export function flattenLessons(c: Course): FlatLesson[] {
  const flat: FlatLesson[] = []
  let index = 0
  for (const mod of c.modules) {
    for (const lesson of mod.lessons) {
      flat.push({ moduleSlug: mod.slug, moduleTitle: mod.title, lesson, index })
      index += 1
    }
  }
  return flat
}

export function findLesson(c: Course, moduleSlug: string, lessonSlug: string) {
  const mod = c.modules.find((m) => m.slug === moduleSlug)
  const lesson = mod?.lessons.find((l) => l.slug === lessonSlug)
  return mod && lesson ? { module: mod, lesson } : undefined
}

export const totalMinutes = (c: Course) =>
  c.modules.reduce((sum, m) => sum + m.lessons.reduce((s, l) => s + l.minutes, 0), 0)

export const totalLessons = (c: Course) =>
  c.modules.reduce((sum, m) => sum + m.lessons.length, 0)
