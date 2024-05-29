// import ApiCalendar from "react-google-calendar-api";
import {} from 'react-router-dom'
// import  { GoogleLogin } from '@react-oauth/google' ;
// import { hasGrantedAllScopesGoogle } from '@react-oauth/google';
// import { jwtDecode } from 'jwt-decode';
// import axios from 'axios';
import { useGoogleLogin } from '@react-oauth/google';

// const apiCalendar = new ApiCalendar(config);
export default function Login() {
  
  // const scope = [ "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created",
  //                 "https://www.googleapis.com/auth/userinfo.email",
  //                 "https://www.googleapis.com/auth/userinfo.profile",
  //                 "openid"]
  // console.log('scope configurado = ', scope)

  // const login = GoogleLogin({
  //   onSuccess: tokenResponse => console.log('tokenResponse = ', tokenResponse),
  // });
  // console.log('logiiiin:', login)

  const scope = [
    "https://www.googleapis.com/auth/calendar", 
    "https://www.googleapis.com/auth/calendar.app.created",
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

  // const handleLogin = async (credentialResponse) => {
    
  //   var obj = jwtDecode(credentialResponse.credential);
  //   console.log('obj: ',obj);
  //   var data = JSON.stringify(obj);
  //   console.log('data = ', data);

  //   // const data = {your data to send to server};

  // //   const config = {
  // //     method: 'POST',
  // //     url: 'http://127.0.0.1:8000/api/v1/calendar/token/',
  // //     headers: {},
  // //     data: data
  // //   }


  // // await axios(config)
  //   const response = fetch('http://localhost:8000/api/v1/calendar/token/', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Allow-Control-Allow-Origin': '*'
  //     },
  //     body: data,                
  //   });
  //   console.log('response body =', response.body)

  //   const hasAccess = hasGrantedAllScopesGoogle(
  //     response.body,
  //     "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created",
  //     "https://www.googleapis.com/auth/userinfo.email",
  //     "https://www.googleapis.com/auth/userinfo.profile",
  //     "openid"
  //   );  
  //   console.log('hasAccess = ', hasAccess);
  // }

  const handleLogin = async(credentialResponse) => {
    // console.log('credential Response', credentialResponse)
    const response = fetch('http://localhost:8000/api/v1/calendar/token/', {
      method: 'POST',
      // mode: 'no-cors',
      headers: {
        // 'X-BLA' : 'bla!',
        'Access-Control-Allow-Headers' : '*',
        'Content-Type': 'application/json',
        'Allow-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*'
      },
      body: credentialResponse,                
    });
    
    // console.log('response body =', response.body)
    console.log(credentialResponse)
  }
  // const teste = async() => {
  //   const resposta = fetch('http://localhost:8000/api/v1/calendar/token/', {
  //     method: 'GET',
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Access-Control-Allow-Headers': 'X-Requested-With',
  //       'Allow-Control-Allow-Origin': '*' 
  //     },
  //   });
  //   console.log('resposta = ',resposta);
  // }

  const login = useGoogleLogin({ 
    scope: "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile openid", 
    flow: 'auth-code',
    access_type: 'offline',
    prompt: 'consent',
    onSuccess: handleLogin,
  });

  // return (<button onClick={() => teste()}> oiasodiaosio</button>)
  return (<button onClick={() => login()}> Fazer login</button>)

  // return(<GoogleLogin onSuccess={credentialResponse => {
  //     console.log(credentialResponse);
  //   }}
  //   onError={() => {
  //     console.log('Login Failed');
  //   }}
  // />) 
}



     