document.getElementById("loginForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    const response = await fetch('/user/auth/login/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Login successful!");
        localStorage.setItem("accessToken", data.access);
        window.location.href = "/user/profile/";  // Redirect to profile page
    } else {
        errorMessage.textContent = data.error || "Login failed. Please try again.";
    }
});
