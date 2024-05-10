import ApiCalendar from "react-google-calendar-api";
import React from 'react';
import {} from 'react-router-dom'

const config = {
  clientId: process.env.REACT_APP_GOOGLE_CLIENT_ID,
  apiKey: process.env.REACT_APP_GOOGLE_API_KEY,
  scope: "https://www.googleapis.com/auth/calendar",
  discoveryDocs: [
    "https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest",
  ],
};



const apiCalendar = new ApiCalendar(config);
export default class Login extends React.Component {
  constructor(props) {
    super(props);
    this.handleItemClick = this.handleItemClick.bind(this);
  }

 
  handleItemClick = async (event, name) => {
    

   if (name === 'sign-in') {
         {
            const  myResponse = await apiCalendar.handleAuthClick()
            console.log(myResponse.access_token)

           /* var meuDicionario = {}
            for (var key in rs1) {
              meuDicionario[key] = rs1[key];
            }
            console.log(meuDicionario)
            console.log(meuDicionario.access_token)
*/
            const response =  fetch('/v1/calendar/flow/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                // Supondo que você precise passar o access token no corpo da requisição
                // Modifique isso de acordo com os requisitos da sua API
              },
             body: JSON.stringify({ accessToken: myResponse.access_token }),                
            });
            console.log(response.body)
         }
            
         }
         else if (name === 'sign-out') {
          apiCalendar.handleSignoutClick();
         }
    }
      

  render() {
    return (
      <div>
          <button
              onClick={(e) => this.handleItemClick(e, 'sign-in')}
              
          >
            sign-in
          </button>
          <button
              onClick={(e) => this.handleItemClick(e, 'sign-out')}
          >
            sign-out
          </button>
       </div>
      );
  }
}
  


 /* const response = await fetch('/v1/calendar/flow/', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                // Supondo que você precise passar o access token no corpo da requisição
                // Modifique isso de acordo com os requisitos da sua API
              },
             // body: JSON.stringify({ accessToken: access_token }),
            });
            
            // Verificar se a chamada à API foi bem-sucedida
            if (!response.ok) {
              throw new Error('Erro ao chamar a API do backend');
            }
           */
            // Ou qualquer outra ação após o login bem-sucedido