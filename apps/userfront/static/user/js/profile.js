async function submitProfile() {
    const profileData = {
        email_address: document.getElementById('email').value,
        alternative_address: document.getElementById('alternativeEmail').value,
        phone: document.getElementById('phone').value,
        dob: document.getElementById('dob').value,
        skype: document.getElementById('skype').value,
        gender: document.getElementById('gender').value,
    };

    try {
        // Retrieve the token using the same key as in login.js ("accessToken")
        let token = localStorage.getItem('accessToken');
        if (!token) {
            // If token is missing, inform the user. Optionally, you could implement token refresh logic here.
            alert("Access token not found. Please log in again.");
            return;
        }

        const response = await fetch('/user/userprofile/', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(profileData)
        });

        if (response.ok) {
            alert('Profile updated successfully!');
        } else {
            const errorData = await response.json();
            alert(`Error: ${JSON.stringify(errorData)}`);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while updating the profile.');
    }
}
