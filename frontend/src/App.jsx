import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CarList from './components/CarList';
import CarDetail from './components/CarDetail';

function App() {
  return (
    <Router>
      <div className="container">
        <header>
          <h1>Collection de Luxe</h1>
        </header>
        
        <Routes>
          {/* Route pour la liste avec recherche et pagination */}
          <Route path="/" element={<CarList />} />
          
          {/* Route pour le détail d'une voiture (le rebond) */}
          <Route path="/car/:id" element={<CarDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;