import { Link, Navigate, useParams } from 'react-router-dom'
import {
  Box,
  Breadcrumbs,
  Button,
  Card,
  CardContent,
  Chip,
  Container,
  LinearProgress,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Stack,
  Typography,
} from '@mui/material'
import CheckCircleIcon from '@mui/icons-material/CheckCircle'
import RadioButtonUncheckedIcon from '@mui/icons-material/RadioButtonUnchecked'
import PlayCircleOutlineIcon from '@mui/icons-material/PlayCircleOutline'
import { findCourse } from '../content/catalog'
import { flattenLessons, totalLessons, totalMinutes } from '../content/types'
import { lessonKey, useProgress } from '../hooks/useProgress'

export default function CourseDetail() {
  const { courseSlug } = useParams()
  const { isCompleted } = useProgress()

  if (!courseSlug) return <Navigate to="/" replace />
  const course = findCourse(courseSlug)
  if (!course) return <Navigate to="/" replace />

  const flat = flattenLessons(course)
  const total = totalLessons(course)
  const completedCount = flat.filter((f) => isCompleted(lessonKey(course.slug, f.moduleSlug, f.lesson.slug))).length
  const nextLesson = flat.find((f) => !isCompleted(lessonKey(course.slug, f.moduleSlug, f.lesson.slug))) ?? flat[0]
  const progressPct = total === 0 ? 0 : Math.round((completedCount / total) * 100)

  return (
    <Box sx={{ height: '100%', overflowY: 'auto', bgcolor: 'background.default' }}>
      <Container maxWidth="md" sx={{ py: 6 }}>
        <Breadcrumbs sx={{ mb: 2 }}>
          <Typography component={Link} to="/" variant="body2" sx={{ color: 'text.secondary', textDecoration: 'none' }}>
            Catalogue
          </Typography>
          <Typography variant="body2" color="text.secondary">{course.title}</Typography>
        </Breadcrumbs>

        <Chip label="Parcours" color="secondary" size="small" sx={{ mb: 2, fontWeight: 600 }} />
        <Typography variant="h3" gutterBottom sx={{ fontSize: { xs: '2rem', sm: '2.5rem' } }}>
          {course.title}
        </Typography>
        <Typography variant="h6" color="text.secondary" gutterBottom>
          {course.subtitle}
        </Typography>
        <Typography variant="body1" sx={{ mt: 2, mb: 3 }}>
          {course.description}
        </Typography>

        <Stack direction="row" spacing={3} sx={{ mb: 3 }} flexWrap="wrap">
          <Typography variant="body2" color="text.secondary">
            {course.modules.length} modules · {total} leçons · ~{totalMinutes(course)} min
          </Typography>
        </Stack>

        <Box sx={{ mb: 3 }}>
          <Stack direction="row" justifyContent="space-between" sx={{ mb: 0.5 }}>
            <Typography variant="body2">Progression</Typography>
            <Typography variant="body2">{completedCount}/{total} leçons</Typography>
          </Stack>
          <LinearProgress variant="determinate" value={progressPct} sx={{ height: 8, borderRadius: 4 }} />
        </Box>

        <Button
          component={Link}
          to={`/cours/${course.slug}/lecon/${nextLesson.moduleSlug}/${nextLesson.lesson.slug}`}
          variant="contained"
          size="large"
          startIcon={<PlayCircleOutlineIcon />}
          sx={{ mb: 5 }}
        >
          {completedCount === 0 ? 'Commencer la formation' : 'Continuer la formation'}
        </Button>

        <Stack spacing={2}>
          {course.modules.map((mod, i) => (
            <Card key={mod.slug} variant="outlined">
              <CardContent>
                <Typography variant="overline" color="text.secondary">
                  Module {i}
                </Typography>
                <Typography variant="h6" gutterBottom>
                  {mod.title.replace(/^Module \d+ — /, '')}
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                  {mod.description}
                </Typography>
                <List dense disablePadding>
                  {mod.lessons.map((lesson) => {
                    const done = isCompleted(lessonKey(course.slug, mod.slug, lesson.slug))
                    return (
                      <ListItemButton
                        key={lesson.slug}
                        component={Link}
                        to={`/cours/${course.slug}/lecon/${mod.slug}/${lesson.slug}`}
                        sx={{ borderRadius: 1 }}
                      >
                        <ListItemIcon sx={{ minWidth: 32 }}>
                          {done ? (
                            <CheckCircleIcon fontSize="small" color="secondary" />
                          ) : (
                            <RadioButtonUncheckedIcon fontSize="small" color="disabled" />
                          )}
                        </ListItemIcon>
                        <ListItemText
                          primary={lesson.title}
                          secondary={`${lesson.minutes} min`}
                        />
                      </ListItemButton>
                    )
                  })}
                </List>
              </CardContent>
            </Card>
          ))}
        </Stack>
      </Container>
    </Box>
  )
}
