document.addEventListener("DOMContentLoaded", () => {

    // Manual form submission
    const claimForm = document.getElementById("claimForm");
    if (claimForm) {
        claimForm.addEventListener("submit", async function(e) {
            e.preventDefault();

            const data = {
                policyNumber: document.getElementById("policyNumber").value,
                policyholderName: document.getElementById("policyholderName").value,
                incidentDate: document.getElementById("incidentDate").value,
                incidentTime: document.getElementById("incidentTime").value,
                location: document.getElementById("location").value,
                description: document.getElementById("description").value,
                estimatedDamage: Number(document.getElementById("estimatedDamage").value),
                claimType: document.getElementById("claimType").value
            };

            await submitClaimToBackend(data);
        });
    }

    // ACORD text submission
    const acordForm = document.getElementById("acordForm");
    if (acordForm) {
        acordForm.addEventListener("submit", async function(e) {
            e.preventDefault();

            const acordText = document.getElementById("acordText").value;
            if (!acordText.trim()) {
                alert("Please paste the ACORD form text!");
                return;
            }

            await submitClaimToBackend(acordText);
        });
    }

});

// Common function to send data to backend
async function submitClaimToBackend(data) {
    try {
        const response = await fetch("http://127.0.0.1:5000/submit-claim", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById("output").textContent = JSON.stringify(result, null, 4);
    } catch (error) {
        console.error("Error submitting claim:", error);
        alert("Failed to submit claim. Check console for details.");
    }
}
