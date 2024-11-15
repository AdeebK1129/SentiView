// src/pages/LandingPage.tsx
import React, { useState } from 'react';
import SignupModal from '../SignupModal';

const LandingPage: React.FC = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false); // Temporary for testing
    const [showModal, setShowModal] = useState(false);

    const handleSignupClick = () => {
        setShowModal(true);
    };

    return (
        <div>
            <h1>Welcome to SentiView</h1>
            {!isLoggedIn && (
                <button onClick={handleSignupClick}>
                    Sign Up to Get Started
                </button>
            )}
            {showModal && <SignupModal onClose={() => setShowModal(false)} />}
        </div>
    );
};

export default LandingPage;
