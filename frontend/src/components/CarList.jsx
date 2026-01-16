import { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
const CarList = () => {
  const [cars, setCars] = useState([]);
  const [search, setSearch] = useState("");
  const [url, setUrl] = useState("http://127.0.0.1:8000/api/cars/");

  useEffect(() => {
    // Appel de l'API 
    axios.get(`${url}?search=${search}`).then(res => {
      setCars(res.data);
    });
  }, [url, search]);

  return (
    <div>
      <input 
        type="text" 
        placeholder="Rechercher une Ferrari..." 
        onChange={(e) => setSearch(e.target.value)} 
      />
      <div className="grid">
        {cars.results?.map(car => (
            <div key={car.id} className="car-card">
                <h3>{car.brand_name} {car.model}</h3>
            <   p>{car.year}</p>
    
            {/* LE REBOND : Lien vers la page détail via l'ID */}
            <Link to={`/car/${car.id}`} className="btn-detail">
                Voir la fiche technique
            </Link>
            </div>
            ))}
      </div>
      {/* Pagination */}
      <button onClick={() => setUrl(cars.previous)} disabled={!cars.previous}>Précédent</button>
      <button onClick={() => setUrl(cars.next)} disabled={!cars.next}>Suivant</button>
    </div>
  );
};

export default CarList;