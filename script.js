// Når skjemaet blir sendt inn
document.getElementById("task-form").addEventListener("submit", async (e) => {
    e.preventDefault();  // Forhindre at siden lastes på nytt

    // Hent data fra skjemaet
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    // Send data til serveren
    const response = await fetch("/add_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description })
    });

    // Hvis oppgaven ble lagt til, last inn oppgavene på nytt
    if (response.ok) {
        alert("Task added successfully!");
        loadTasks();
    }
});

// Last opp oppgaver fra serveren
async function loadTasks() {
    const response = await fetch("/tasks");
    const tasks = await response.json();
    const taskContainer = document.getElementById("tasks");
    taskContainer.innerHTML = tasks.map(
        task => `<div>${task[1]} - Priority: ${task[3]}</div>`
    ).join("");
}

// Last opp oppgavene når siden lastes
loadTasks();
