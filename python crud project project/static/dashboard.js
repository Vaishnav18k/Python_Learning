document.addEventListener("DOMContentLoaded", () => {
    loadEntries();
});

// Load all entries from FastAPI
async function loadEntries() {
    console.log("Loading entries...");
    try {
        const res = await fetch("http://localhost:8000/entries/");
        if (!res.ok) throw new Error("Failed to load entries");
        const entries = await res.json();

        const tbody = document.querySelector("#entries-table tbody");
        tbody.innerHTML = "";

        entries.forEach((entry, index) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${index + 1}</td>
                <td>${entry.user_id}</td>
                <td>${entry.name}</td>
                <td>${entry.occupation}</td>
                <td>${entry.phone}</td>
                <td>${entry.address}</td>
                <td>${entry.description}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (err) {
        console.error("Error loading entries:", err);
        alert("Error loading data.");
    }
}

// Open modal
function openCreateModal() {
    document.getElementById("createModal").style.display = "block";
}

// Close modal
function closeCreateModal() {
    document.getElementById("createModal").style.display = "none";
}

// Submit entry
async function submitEntry(e) {
    e.preventDefault();
    console.log("Form submitted");

    const entry = {
        user_id: parseInt(document.getElementById("user_id").value),
        name: document.getElementById("name").value.trim(),
        occupation: document.getElementById("occupation").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        address: document.getElementById("address").value.trim(),
        description: document.getElementById("description").value.trim()
    };

    // console.log("Sending entry:", entry);

    try {
        const res = await fetch("http://127.0.0.1:8000/entries/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(entry),
            credentials: 'same-origin'
        });

        console.log("Response status:", res.status);
        const data = await res.json();
        console.log("Response data:", data);

        if (!res.ok) {
            throw new Error(`Server responded with ${res.status}: ${JSON.stringify(data)}`);
        }

        alert("✅ Entry created successfully!");
        closeCreateModal();
        loadEntries(); // Refresh table
    } catch (err) {
        console.error("Submission error:", err);
        alert("❌ Error creating entry:\n" + err.message);
    }
}
// newly added code
// Open update modal
function openUpdateModal() {
    document.getElementById("updateModal").style.display = "block";
    document.getElementById("updateForm").style.display = "none";
    document.getElementById("update_user_id").value = "";
}

// Close update modal
function closeUpdateModal() {
    document.getElementById("updateModal").style.display = "none";
    document.getElementById("update_user_id").value = "";
    document.getElementById("update_user_id_hidden").value = "";
    document.getElementById("update_name").value = "";
    document.getElementById("update_occupation").value = "";
    document.getElementById("update_phone").value = "";
    document.getElementById("update_address").value = "";
    document.getElementById("update_description").value = "";
    document.getElementById("updateForm").style.display = "none";
}

// Load entry for update
async function loadEntryForUpdate(e) {
    e.preventDefault();
    const userId = document.getElementById("update_user_id").value;

    try {
        const res = await fetch(`http://localhost:8000/entries/${userId}`);
        if (!res.ok) throw new Error("Entry not found");

        const entry = await res.json();

        // Populate update form
        document.getElementById("update_user_id_hidden").value = entry.user_id;
        document.getElementById("update_name").value = entry.name;
        document.getElementById("update_occupation").value = entry.occupation;
        document.getElementById("update_phone").value = entry.phone;
        document.getElementById("update_address").value = entry.address;
        document.getElementById("update_description").value = entry.description;

        // Show update form, hide user ID input form
        document.getElementById("updateForm").style.display = "block";
        document.getElementById("update_user_id").parentElement.style.display = "none";
    } catch (err) {
        console.error("Error loading entry:", err);
        alert("❌ Error: " + err.message);
    }
}

// Submit update
async function submitUpdate(e) {
    e.preventDefault();
    const userId = document.getElementById("update_user_id_hidden").value;

    const updatedEntry = {
        user_id: parseInt(userId),
        name: document.getElementById("update_name").value.trim(),
        occupation: document.getElementById("update_occupation").value.trim(),
        phone: document.getElementById("update_phone").value.trim(),
        address: document.getElementById("update_address").value.trim(),
        description: document.getElementById("update_description").value.trim()
    };

    try {
        const res = await fetch(`http://localhost:8000/entries/${userId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(updatedEntry)
        });

        if (!res.ok) {
            const errData = await res.json();
            throw new Error(`Server responded with ${res.status}: ${JSON.stringify(errData)}`);
        }

        alert("✅ Entry updated successfully!");
        closeUpdateModal();
        loadEntries();
    } catch (err) {
        console.error("Update failed:", err);
        alert("❌ Update failed: " + err.message);
    }
}
// Prompt delete
async function promptDelete() {
    const entryId = prompt("Enter Entry ID to delete:");
    if (!entryId) return;

    if (!confirm("Are you sure? This action cannot be undone.")) return;

    try {
        const res = await fetch(`http://localhost:8000/entries/${entryId}`, {
            method: "DELETE"
        });

        if (!res.ok) throw new Error("Failed to delete entry");

        alert("✅ Entry deleted successfully!");
        loadEntries();
    } catch (err) {
        console.error(err);
        alert("❌ " + err.message);
    }
}