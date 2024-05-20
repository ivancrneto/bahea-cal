// import ApiCalendar from "react-google-calendar-api";
import {} from 'react-router-dom'
import  { GoogleLogin, hasGrantedAllScopesGoogle }  from  '@react-oauth/google' ;
import { jwtDecode } from 'jwt-decode';
// import axios from 'axios';

// const apiCalendar = new ApiCalendar(config);
export default function Login() {
  
  // const scope = [ "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created",
  //                 "https://www.googleapis.com/auth/userinfo.email",
  //                 "https://www.googleapis.com/auth/userinfo.profile",
  //                 "openid"]
  // console.log('scope configurado = ', scope)
  const login = GoogleLogin({
    onSuccess: tokenResponse => console.log('tokenResponse = ', tokenResponse),
  });
  console.log('logiiiin:', login)

  const scope = [
    "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
  ]
  console.log('escopo configurado:')
  console.log(scope)

  // return (<div>
  //         <button onClick={ () => login()}>Login com Google</button>
  //         <button>(nao funciona) Log out</button>
  //   </div>);

  const handleLogin = async (credentialResponse) => {
    var obj = jwtDecode(credentialResponse.credential);
    console.log('obj: ',obj);
    var data = JSON.stringify(obj);
    console.log('data = ', data);

    // const data = {your data to send to server};

  //   const config = {
  //     method: 'POST',
  //     url: 'http://127.0.0.1:8000/api/v1/calendar/token/',
  //     headers: {},
  //     data: data
  //   }


  // await axios(config)
    const response = fetch('http://localhost:8000/api/v1/calendar/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Allow-Control-Allow-Origin': '*'
      },
      body: data,                
    });
    console.log('response body =', response.body)

    const hasAccess = hasGrantedAllScopesGoogle(
      response.body,
      "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created",
      "https://www.googleapis.com/auth/userinfo.email",
      "https://www.googleapis.com/auth/userinfo.profile",
      "openid"
    );  
    console.log('hasAccess = ', hasAccess);


  }

  return(<GoogleLogin onSuccess={handleLogin} />)
}



     