import React from 'react'
import ReactDOM from 'react-dom/client'
import Login from './Login.jsx'
import Login1 from  './Buttonapi.jsx'

import Login1 from  './Buttonapi.jsx'

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Time from "./routes/Time.jsx";

import './index.css'

const router = createBrowserRouter([

  {
      path:"/",
      element: <Login/>,

  },
  {
    path: "/hello",
    element: <div> hello</div>,
  },
  {
    path: "/Time",
    element: <Time />,
  },

  {
      path: "/buttonapi",
      element: <Login1/>,

  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <GoogleOAuthProvider clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}>
      <RouterProvider router={router} />
    </GoogleOAuthProvider>
  </React.StrictMode>
)