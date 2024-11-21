document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search-button').addEventListener('click', function() {
        const city = document.getElementById('city').value.trim();

        if (!city) {
            alert("Пожалуйста, введите название города.");
            return;
        }

        fetch(`/api/v1/weather/?city=${encodeURIComponent(city)}`)
            .then(response => response.json())
            .then(data => {
                if (data && data.city) {

                    document.getElementById('city-name').textContent = `Погода в городе ${data.city}`;
                    document.getElementById('temp').textContent = `Температура: ${data.temp}°C`;
                    document.getElementById('pressure').textContent = `Давление: ${data.def_pressure_mm} мм рт. ст.`;
                    document.getElementById('wind-speed').textContent = `Скорость ветра: ${data.wind_speed} м/с`;
                    document.getElementById('weather-url').href = data.url;
                    document.getElementById('weather-url').textContent = 'Узнать подробности';
                    document.getElementById('weather-info').style.display = 'block';
                } else {
                    alert('Не удалось получить информацию о погоде для указанного города.');
                }
            })
            .catch(error => {
                console.error('Ошибка при отправке запроса:', error);
                alert('Не удалось получить данные о погоде.');
            });
    });
});
