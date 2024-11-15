// src/components/SignupModal.tsx
import React, { useState } from 'react';

interface SignupModalProps {
    onClose: () => void;
}

const SignupModal: React.FC<SignupModalProps> = ({ onClose }) => {
    const [step, setStep] = useState(1);

    const handleNextStep = () => {
        setStep(step + 1);
    };

    return (
        <div style={modalStyle}>
            <button onClick={onClose}>X</button>
            {step === 1 && (
                <div>
                    <h2>Step 1: Enter Your Email</h2>
                    <input type="email" placeholder="Enter your email" />
                    <button onClick={handleNextStep}>Continue</button>
                </div>
            )}
            {step === 2 && (
                <div>
                    <h2>Step 2: Enter Your Name</h2>
                    <input type="text" placeholder="Enter your name" />
                    <button onClick={handleNextStep}>Continue</button>
                </div>
            )}
            {step === 3 && (
                <div>
                    <h2>Step 3: Verify Code</h2>
                    <input type="text" placeholder="Enter code" />
                    <button onClick={handleNextStep}>Continue</button>
                </div>
            )}
            {step > 3 && (
                <div>
                    <h2>Sign Up Complete</h2>
                    <p>You’re almost ready to start using SentiView!</p>
                    <button onClick={onClose}>Close</button>
                </div>
            )}
        </div>
    );
};

const modalStyle: React.CSSProperties = {
    position: 'fixed',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    padding: '20px',
    backgroundColor: '#fff',
    borderRadius: '8px',
    boxShadow: '0px 4px 12px rgba(0, 0, 0, 0.1)',
    zIndex: 1000,
};

export default SignupModal;
