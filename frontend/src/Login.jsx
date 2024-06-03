
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

  return(
    <GoogleOAuthProvider clientId="470653035644-rkr19rof1eclp7f7gmd4044jt110hf9g.apps.googleusercontent.com">
        <GoogleLogin
            onSuccess={handleLogin}
        />
    </GoogleOAuthProvider>)
}


 