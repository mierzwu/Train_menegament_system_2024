function updateTime() {
    const now = new Date();
    const dateElement = document.getElementById("currentDate");
    const timeElement = document.getElementById("currentTime");

    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    dateElement.textContent = now.toLocaleDateString('pl-PL', options);

    timeElement.textContent = now.toLocaleTimeString('pl-PL');
}
function handleFormSubmit(event) {
    event.preventDefault(); // Zapobiega domyślnej akcji formularza

    // Pobieranie danych z formularza
    const from_station = document.getElementById("from_station").value;
    const to_station = document.getElementById("to_station").value;
    const date = document.getElementById("date").value;

    // Tworzenie obiektu z danymi
    const formData = { from_station, to_station, date };

    // Wysyłanie danych na serwer za pomocą fetch (AJAX)
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Dane zostały wysłane:", data);
        // Można przekierować lub wyświetlić odpowiedź
    })
    

    // Możesz również zapisać dane w localStorage, jeśli chcesz je użyć później
    localStorage.setItem("searchData", JSON.stringify(formData));
}

setInterval(updateTime, 1000);
updateTime(); // Aktualizacja natychmiastowa
