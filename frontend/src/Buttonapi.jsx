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
}