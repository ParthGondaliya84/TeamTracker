// async function submitProfile() {
//     // Check for the access token in localStorage
//     let token = localStorage.getItem('accessToken');
//     if (!token) {
//         // If the token is missing, redirect to the login page
//         alert("You must be logged in to update your profile.");
//         window.location.href = "/user/login/";  // Adjust the login URL if needed
//         return;
//     }

//     const profileData = {
//         email_address: document.getElementById('email').value,
//         alternative_address: document.getElementById('alternativeEmail').value,
//         phone: document.getElementById('phone').value,
//         dob: document.getElementById('dob').value,
//         skype: document.getElementById('skype').value,
//         gender: document.getElementById('gender').value,
//     };

//     try {
//         const response = await fetch('/user/userprofile/', {
//             method: 'PUT',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'Authorization': `Bearer ${token}`
//             },
//             body: JSON.stringify(profileData)
//         });

//         if (response.ok) {
//             alert('Profile updated successfully!');
//         } else if (response.status === 401) {
//             // Token might have expired, redirect to login
//             alert("Session expired. Please log in again.");
//             localStorage.removeItem('accessToken');  // Clear the expired token
//             window.location.href = "/user/login/";  // Redirect to login page
//         } else {
//             const errorData = await response.json();
//             alert(`Error: ${JSON.stringify(errorData)}`);
//         }
//     } catch (error) {
//         console.error('Error:', error);
//         alert('An error occurred while updating the profile.');
//     }
// }


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
