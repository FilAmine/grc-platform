import { Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'
import CatalogHome from './components/CatalogHome'
import CourseDetail from './components/CourseDetail'
import LessonPage from './components/LessonPage'

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<CatalogHome />} />
        <Route path="/cours/:courseSlug" element={<CourseDetail />} />
        <Route path="/cours/:courseSlug/lecon/:moduleSlug/:lessonSlug" element={<LessonPage />} />
      </Route>
    </Routes>
  )
}
