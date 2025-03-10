import { Profile } from '@pages/profile/Profile'
import { createBrowserRouter } from 'react-router-dom'

export const router = createBrowserRouter([
  {
    path: '/profile',
    element: <Profile />,
  },
  {
    path: '/',
    element: <div>Hello App</div>,
  },
])
