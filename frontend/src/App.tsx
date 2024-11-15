/**
 * App Component
 * 
 * The root component of the React app that wraps child components with the QueryClientProvider.
 * 
 * @component
 * @example
 * // Render the entire app
 * <App />
 * 
 * @returns {JSX.Element} The main app component with React Query configuration.
 */
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './components/pages/LandingPage';

const App: React.FC = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                {/* Additional routes can go here */}
            </Routes>
        </Router>
    );
};

export default App;

