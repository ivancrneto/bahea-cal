import axios from 'axios'

export default function Login1() {
  const Login1 = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/v1/calendar/token/', {'bla':'bla'}, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log('response-data: ', response.data);
    } catch (error) {
      console.error('error: ', error);
    }
  }

  return (<button onClick={Login1}> Fazer login</button>)
<<<<<<< HEAD
}





// import {} from 'react-router-dom'
// import axios from 'axios'


// export default function Login1() {
//   const Login1 = async () => {
    


 
// var options = {
//   method: 'POST',
//   url: 'http://localhost:8000/api/v1/calendar/token/',
//     headers: {
//             'Content-Type': 'application/json',
//             'Allow-Control-Allow-Origin': '*'
//           },
//           body:   {'bla':'bla'}     

//   };

 
// axios.request(options).then(function (response) {
//   console.log(response.data);
// }).catch(function (error) {
//   console.error(error);
// });


// }
//         return (<button onClick={() => Login1()}> Fazer login</button>)
//  }
=======
}
>>>>>>> 47d2db413d38ab8a9e87759ddf7ce20f5943283d
