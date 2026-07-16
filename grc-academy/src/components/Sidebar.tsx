import { Link, useParams } from 'react-router-dom'
import {
  Box,
  Checkbox,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from '@mui/material'
import { findCourse } from '../content/catalog'
import { lessonKey, useProgress } from '../hooks/useProgress'

export default function Sidebar() {
  const { courseSlug, moduleSlug, lessonSlug } = useParams()
  const { isCompleted } = useProgress()

  const course = courseSlug ? findCourse(courseSlug) : undefined
  if (!course) return null

  return (
    <Box sx={{ width: 300, flexShrink: 0, overflowY: 'auto', height: '100%', borderRight: 1, borderColor: 'divider' }}>
      <Box sx={{ p: 2 }}>
        <Typography variant="subtitle2" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: 0.5 }}>
          Sommaire du parcours
        </Typography>
      </Box>
      {course.modules.map((mod) => (
        <Box key={mod.slug} sx={{ mb: 1 }}>
          <Typography variant="body2" sx={{ px: 2, py: 0.5, fontWeight: 700 }}>
            {mod.title}
          </Typography>
          <List dense disablePadding>
            {mod.lessons.map((lesson) => {
              const key = lessonKey(course.slug, mod.slug, lesson.slug)
              const selected = mod.slug === moduleSlug && lesson.slug === lessonSlug
              return (
                <ListItemButton
                  key={lesson.slug}
                  component={Link}
                  to={`/cours/${course.slug}/lecon/${mod.slug}/${lesson.slug}`}
                  selected={selected}
                  sx={{ pl: 3, py: 0.25 }}
                >
                  <ListItemIcon sx={{ minWidth: 32 }}>
                    <Checkbox
                      edge="start"
                      checked={isCompleted(key)}
                      tabIndex={-1}
                      size="small"
                      disableRipple
                      onClick={(e) => e.stopPropagation()}
                    />
                  </ListItemIcon>
                  <ListItemText
                    primaryTypographyProps={{ variant: 'body2' }}
                    primary={lesson.title}
                  />
                </ListItemButton>
              )
            })}
          </List>
        </Box>
      ))}
    </Box>
  )
}
