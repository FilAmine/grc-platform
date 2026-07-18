import { useEffect, useState } from 'react'
import { Link, Navigate, useParams } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import {
  Box,
  Breadcrumbs,
  Button,
  CircularProgress,
  Container,
  FormControlLabel,
  Checkbox,
  Stack,
  Typography,
} from '@mui/material'
import ArrowBackIcon from '@mui/icons-material/ArrowBack'
import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import Sidebar from './Sidebar'
import { findCourse } from '../content/catalog'
import { contentLoaders } from '../content/contentLoaders'
import { findLesson, flattenLessons } from '../content/types'
import { lessonKey, useProgress } from '../hooks/useProgress'

export default function LessonPage() {
  const { courseSlug, moduleSlug, lessonSlug } = useParams()
  const { isCompleted, toggle } = useProgress()
  const [content, setContent] = useState<string | null>(null)

  useEffect(() => {
    if (!courseSlug || !moduleSlug || !lessonSlug) return
    let cancelled = false
    setContent(null)
    contentLoaders[courseSlug]?.().then((mod) => {
      if (!cancelled) setContent(mod.default[moduleSlug]?.[lessonSlug] ?? null)
    })
    return () => {
      cancelled = true
    }
  }, [courseSlug, moduleSlug, lessonSlug])

  if (!courseSlug || !moduleSlug || !lessonSlug) return <Navigate to="/" replace />

  const course = findCourse(courseSlug)
  if (!course) return <Navigate to="/" replace />

  const found = findLesson(course, moduleSlug, lessonSlug)
  if (!found) return <Navigate to={`/cours/${courseSlug}`} replace />

  const { module: mod } = found
  const flat = flattenLessons(course)
  const currentIndex = flat.findIndex((f) => f.moduleSlug === moduleSlug && f.lesson.slug === lessonSlug)
  const prev = currentIndex > 0 ? flat[currentIndex - 1] : undefined
  const next = currentIndex < flat.length - 1 ? flat[currentIndex + 1] : undefined
  const key = lessonKey(course.slug, moduleSlug, lessonSlug)

  return (
    <Box sx={{ display: 'flex', height: '100%' }}>
      <Sidebar />
      <Box sx={{ flex: 1, overflowY: 'auto' }}>
        <Container maxWidth="md" sx={{ py: 5 }}>
          <Breadcrumbs sx={{ mb: 2 }}>
            <Typography component={Link} to="/" variant="body2" sx={{ color: 'text.secondary', textDecoration: 'none' }}>
              Catalogue
            </Typography>
            <Typography component={Link} to={`/cours/${course.slug}`} variant="body2" sx={{ color: 'text.secondary', textDecoration: 'none' }}>
              {course.title}
            </Typography>
            <Typography variant="body2" color="text.secondary">{mod.title}</Typography>
          </Breadcrumbs>

          <Box
            sx={{
              '& h1': { fontSize: '2rem', fontWeight: 700, mt: 0 },
              '& h2': { fontSize: '1.4rem', fontWeight: 700, mt: 4 },
              '& h3': { fontSize: '1.15rem', fontWeight: 600, mt: 3 },
              '& p': { lineHeight: 1.7, mb: 2 },
              '& li': { lineHeight: 1.7, mb: 0.5 },
              '& table': { borderCollapse: 'collapse', width: '100%', my: 2 },
              '& th, & td': { border: '1px solid', borderColor: 'divider', p: 1, textAlign: 'left', verticalAlign: 'top' },
              '& th': { bgcolor: 'action.hover' },
              '& blockquote': {
                borderLeft: 4,
                borderColor: 'secondary.main',
                pl: 2,
                ml: 0,
                fontStyle: 'italic',
                color: 'text.secondary',
              },
              '& code': { bgcolor: 'action.hover', px: 0.5, borderRadius: 0.5 },
            }}
          >
            {content === null ? (
              <Stack alignItems="center" sx={{ py: 8 }}>
                <CircularProgress size={28} />
              </Stack>
            ) : (
              <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
            )}
          </Box>

          <FormControlLabel
            sx={{ mt: 3 }}
            control={<Checkbox checked={isCompleted(key)} onChange={() => toggle(key)} />}
            label="Marquer cette leçon comme terminée"
          />

          <Stack direction="row" justifyContent="space-between" sx={{ mt: 4, pt: 3, borderTop: 1, borderColor: 'divider' }}>
            {prev ? (
              <Button
                component={Link}
                to={`/cours/${course.slug}/lecon/${prev.moduleSlug}/${prev.lesson.slug}`}
                startIcon={<ArrowBackIcon />}
              >
                {prev.lesson.title}
              </Button>
            ) : (
              <span />
            )}
            {next ? (
              <Button
                component={Link}
                to={`/cours/${course.slug}/lecon/${next.moduleSlug}/${next.lesson.slug}`}
                endIcon={<ArrowForwardIcon />}
                variant="contained"
              >
                {next.lesson.title}
              </Button>
            ) : (
              <Button component={Link} to={`/cours/${course.slug}`} variant="contained">
                Terminer le parcours
              </Button>
            )}
          </Stack>
        </Container>
      </Box>
    </Box>
  )
}
