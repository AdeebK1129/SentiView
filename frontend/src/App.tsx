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
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import HomePage from './components/pages/HomePage';

// Initialize React Query Client
const queryClient = new QueryClient();

const App: React.FC = () => {
    return (
        <QueryClientProvider client={queryClient}>
            <HomePage />
        </QueryClientProvider>
    );
};

export default App;
