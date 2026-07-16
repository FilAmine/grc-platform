import { Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'
import CourseHome from './components/CourseHome'
import LessonPage from './components/LessonPage'

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<CourseHome />} />
        <Route path="/lecon/:moduleSlug/:lessonSlug" element={<LessonPage />} />
      </Route>
    </Routes>
  )
}
