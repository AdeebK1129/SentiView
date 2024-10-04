import axios from 'axios';

/**
 * fetchHelloWorld function
 * 
 * Fetches a "Hello, World!" message from the backend Django API using axios.
 * 
 * @async
 * @function fetchHelloWorld
 * @returns {Promise<{message: string}>} A promise that resolves to an object with the "message" key.
 * @throws {Error} If the network request fails, an error will be thrown.
 */
export const fetchHelloWorld = async (): Promise<{ message: string }> => {
    try {
        const response = await axios.get<{ message: string }>('http://127.0.0.1:8000/api/hello/');
        return response.data;  // Axios automatically parses JSON response
    } catch (error) {
        throw new Error('Network request failed');
    }
};
