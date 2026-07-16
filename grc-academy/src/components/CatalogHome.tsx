import { Link } from 'react-router-dom'
import {
  Box,
  Card,
  CardActionArea,
  CardContent,
  Chip,
  Container,
  LinearProgress,
  Stack,
  Typography,
} from '@mui/material'
import { courses } from '../content/catalog'
import { flattenLessons, totalLessons, totalMinutes } from '../content/types'
import { lessonKey, useProgress } from '../hooks/useProgress'

export default function CatalogHome() {
  const { isCompleted } = useProgress()

  return (
    <Box sx={{ height: '100%', overflowY: 'auto', bgcolor: 'background.default' }}>
      <Container maxWidth="md" sx={{ py: 6 }}>
        <Chip label="GRC Academy" color="secondary" size="small" sx={{ mb: 2, fontWeight: 600 }} />
        <Typography variant="h3" gutterBottom sx={{ fontSize: { xs: '2rem', sm: '2.5rem' } }}>
          Catalogue des formations
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
          Des parcours complets sur la gouvernance, les risques, la conformité et la sécurité dès la conception.
        </Typography>

        <Stack spacing={2}>
          {courses.map((course) => {
            const flat = flattenLessons(course)
            const total = totalLessons(course)
            const completedCount = flat.filter((f) =>
              isCompleted(lessonKey(course.slug, f.moduleSlug, f.lesson.slug)),
            ).length
            const progressPct = total === 0 ? 0 : Math.round((completedCount / total) * 100)

            return (
              <Card key={course.slug} variant="outlined">
                <CardActionArea component={Link} to={`/cours/${course.slug}`}>
                  <CardContent>
                    <Typography variant="h5" gutterBottom>
                      {course.title}
                    </Typography>
                    <Typography variant="subtitle1" color="text.secondary" gutterBottom>
                      {course.subtitle}
                    </Typography>
                    <Typography variant="body2" sx={{ mb: 2 }}>
                      {course.description}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" sx={{ mb: 1.5 }}>
                      {course.modules.length} modules · {total} leçons · ~{totalMinutes(course)} min
                    </Typography>
                    <Stack direction="row" justifyContent="space-between" sx={{ mb: 0.5 }}>
                      <Typography variant="body2">Progression</Typography>
                      <Typography variant="body2">{completedCount}/{total} leçons</Typography>
                    </Stack>
                    <LinearProgress variant="determinate" value={progressPct} sx={{ height: 6, borderRadius: 3 }} />
                  </CardContent>
                </CardActionArea>
              </Card>
            )
          })}
        </Stack>
      </Container>
    </Box>
  )
}
