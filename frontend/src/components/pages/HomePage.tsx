/**
 * HomePage Component
 * 
 * Fetches the "Hello, World!" message from the backend API and displays it.
 * 
 * @component
 * @example
 * // Example usage of HomePage component:
 * <HomePage />
 * 
 * @returns {JSX.Element} A component that renders the fetched data or shows loading/error states.
 */
import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { fetchHelloWorld } from '../../api/queries';

const HomePage: React.FC = () => {
    /**
     * useQuery hook for fetching data from the backend API.
     * 
     * @returns {Object} The state object with the following properties:
     * - data: The API response containing the "Hello, World!" message.
     * - error: Any errors encountered during the API call.
     * - isLoading: Boolean flag indicating if the API call is in progress.
     */
    const { data, error, isLoading } = useQuery({
        queryKey: ['helloWorld'],
        queryFn: fetchHelloWorld,
    });

    if (isLoading) return <p>Loading...</p>;
    if (error instanceof Error) return <p>Error: {error.message}</p>;

    return (
        <div>
            <h1>{data?.message}</h1>
        </div>
    );
};

export default HomePage;
