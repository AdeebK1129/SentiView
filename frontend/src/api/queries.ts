/**
 * fetchHelloWorld function
 * 
 * Fetches a "Hello, World!" message from the backend Django API.
 * 
 * @async
 * @function fetchHelloWorld
 * @returns {Promise<{message: string}>} A promise that resolves to an object with the "message" key.
 * @throws {Error} If the network request fails, an error will be thrown.
 */
export const fetchHelloWorld = async (): Promise<{ message: string }> => {
    const response = await fetch('http://127.0.0.1:8000/api/hello/');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
};
