// app.js

// Simulated API endpoint (replace with real one)
const API_URL = 'https://api.yourdomain.com/v1/check_transaction';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('transaction-form');
    const result = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Collect transaction data from form
        const amount = parseFloat(document.getElementById('amount').value);
        const location = document.getElementById('location').value;
        const cardType = document.getElementById('card-type').value;

        // Create mock feature array (replace with real features from backend logic)
        const features = generateFeatureVector(amount, location, cardType);

        try {
            // Send data to fraud detection API
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ features })
            });

            const data = await response.json();

            // Display the result
            result.innerHTML = `
                <h3>Transaction Result</h3>
                <p><strong>Status:</strong> ${data.status}</p>
                <p><strong>Risk Score:</strong> ${data.risk_score}</p>
            `;
        } catch (error) {
            console.error('Error:', error);
            result.innerHTML = `<p style="color:red;">An error occurred. Please try again later.</p>`;
        }
    });
});

// Simulates feature vector generation
function generateFeatureVector(amount, location, cardType) {
    // In a real application, features would be derived from transaction context
    return [
        amount / 1000, // Normalize
        location.length % 10 / 10, // Fake location encoding
        cardType === 'credit' ? 1 : 0, // Encode card type
        Math.random(), Math.random(), Math.random(), // Additional synthetic features
        ...Array(27).fill(0).map(() => Math.random()) // Complete to 30 features
    ];
}
