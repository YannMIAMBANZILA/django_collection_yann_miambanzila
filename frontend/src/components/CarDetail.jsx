import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const CarDetail = () => {
  const { id } = useParams(); // Récupère l'ID depuis l'URL /car/3
  const [car, setCar] = useState(null);

  useEffect(() => {
    // Appel vers ton API Django
    axios.get(`http://127.0.0.1:8000/api/cars/${id}/`)
      .then(res => setCar(res.data))
      .catch(err => console.error("Erreur lors du chargement", err));
  }, [id]);

  if (!car) return <p>Chargement des caractéristiques...</p>;

  return (
    <div className="car-detail-card">
      <Link color="primary" to="/">← Retour à la collection</Link>
      
      <h2>{car.brand_name} {car.model}</h2>
      <hr />
      
      <div className="specs">
        <p><strong>Année :</strong> {car.year}</p>
        <p><strong>Catégorie :</strong> {car.category_name}</p>
        <p><strong>Puissance :</strong> {car.power_hp} ch</p>
        <p><strong>Prix :</strong> {parseFloat(car.price).toLocaleString()} €</p>
      </div>

      <div className="description">
        <h3>Description</h3>
        <p>Ce modèle d'exception de la marque {car.brand_name} représente le sommet de l'ingénierie automobile.</p>
      </div>
    </div>
  );
};

export default CarDetail;