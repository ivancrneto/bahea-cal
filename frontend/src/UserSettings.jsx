import { useState, useEffect } from 'react';
import axios from 'axios';

const UserSettings = () => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('URL_DO_SEU_MOCKBIN'); // Substitua pela URL do seu Mockbin que retorna um JSON com dados do usuário
        setUserData(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching user data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!userData) {
    return <div>Error loading user data.</div>;
  }

  return (
    <div className="container">
      <div className="user-info">
        <img src={userData.picture || 'https://via.placeholder.com/100'} alt="Foto do Usuário" className="profile-photo" />
        <h2>{userData.name || 'Nome do Usuário'}</h2>
        <p>Email: <strong>{userData.email || 'example@example.com'}</strong></p>
        <p>Time escolhido: <strong>{userData.team || 'Time Exemplo FC'}</strong></p>
      </div>
      <div className="notification-settings">
        <h3>Configurações de Notificação:</h3>
        <ul>
          <li>Receber notificações sobre os jogos: <strong>{userData.notificationTime || '30 minutos antes'}</strong></li>
        </ul>
      </div>
    </div>
  );
};

export default UserSettings;