// import ApiCalendar from "react-google-calendar-api";
import {} from 'react-router-dom'
import  {  GoogleLogin, GoogleOAuthProvider  }  from  '@react-oauth/google' ;
import { hasGrantedAllScopesGoogle } from '@react-oauth/google';
import { jwtDecode } from 'jwt-decode';
import axios from 'axios';

export default function Login() {
  
  <GoogleOAuthProvider clientId="470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com"></GoogleOAuthProvider>;

  const scope = ["https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.app.created",
                  "https://www.googleapis.com/auth/userinfo.email",
                  "https://www.googleapis.com/auth/userinfo.profile",
                  "openid"]
  console.log('scope configurado = ', scope)
  const login = GoogleLogin({
    onSuccess: tokenResponse => console.log(tokenResponse),
  });

  const hasAccess = hasGrantedAllScopesGoogle(
    login.tokenResponse,
    scope
  );  
  console.log(hasAccess);

  // return (<div>
  //         <button onClick={ () => login()}>Login com Google</button>
  //         <button>(nao funciona) Log out</button>
  //   </div>);

  const handleLogin = async (credentialResponse) => {
    var obj = jwtDecode(credentialResponse.credential);
    var data = JSON.stringify(obj);
    console.log(data);

  //   // const data = {your data to send to server};

    const config = {
      method: 'POST',
      url: 'http://127.0.0.1:8000/api/v1/calendar/token/',
      headers: {},
      data: data
    }

  await axios(config)
}

<<<<<<< HEAD
  return(
    <GoogleOAuthProvider clientId="470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com">
        <GoogleLogin
            onSuccess={handleLogin}
        />
    </GoogleOAuthProvider>)
=======
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
>>>>>>> da576de (tests code)
}


 