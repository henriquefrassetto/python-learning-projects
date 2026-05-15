const baseURL = "http://127.0.0.1:8000";

// =======================
// HELPERS
// =======================
function getCity() {
    return document.getElementById("cityInput").value.trim();
}

function getUnit() {
    return document.getElementById("unit").value;
}

// =======================
// UI
// =======================
function setBackground(url) {
    document.body.style.backgroundImage = `url('${url}')`;
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundPosition = "center";
    document.body.style.backgroundAttachment = "fixed";
}

// =======================
// ICONS + BACKGROUND
// =======================
function getIcon(condition = "") {
    const c = condition.toLowerCase();

    if (c.includes("thunder")) return "⛈️";

    if (c.includes("rain")) return "🌧️";

    if (c.includes("snow")) return "❄️";

    if (
        c.includes("overcast") ||
        c.includes("partially cloudy") ||
        c.includes("cloud")
    ) {
        return "☁️";
    }

    if (c.includes("clear") || c.includes("sun")) return "☀️";

    return "🌡️";
}

const weatherBackgrounds = {
    clear: "https://ilp-media.wgbh.org/filer_public/30/59/30590aea-8c73-4e3b-be1d-c7d1d4298705/buac18-img-sunsky-poster.png",
    clouds: "https://patternpictures.com/wp-content/uploads/2019/12/Radiant-Cloudy-Sky-over-Sea-Water-patternpictures-0612.jpg",
    rain: "https://images.unsplash.com/photo-1719038850147-2778f06ccae0?auto=format&fit=crop&w=3000",
    snow: "https://previews.123rf.com/images/feelart/feelart1907/feelart190700050/127412242-snow-falling-on-sky-with-cloud-for-winter-season.jpg",
    thunder: "https://i0.wp.com/mandry.club/wp-content/uploads/2025/05/beautiful_lightning_in_the_night_sky_0.webp?ssl=1",
    default: "https://ilp-media.wgbh.org/filer_public/30/59/30590aea-8c73-4e3b-be1d-c7d1d4298705/buac18-img-sunsky-poster.png"
};

function getBackground(condition = "") {
    const c = condition.toLowerCase();

    if (c.includes("thunder")) return weatherBackgrounds.thunder;

    if (c.includes("rain")) return weatherBackgrounds.rain;

    if (c.includes("snow")) return weatherBackgrounds.snow;

    if (
        c.includes("overcast") ||
        c.includes("partially cloudy") ||
        c.includes("cloud")
    ) {
        return weatherBackgrounds.clouds;
    }

    if (c.includes("clear") || c.includes("sun")) return weatherBackgrounds.clear;

    return weatherBackgrounds.default;
}

// =======================
// CURRENT WEATHER
// =======================
async function getCurrent() {
    const city = getCity();
    const unit = getUnit();

    const res = await fetch(`${baseURL}/weather/current?city=${city}&unit=${unit}`);
    const data = await res.json();

    if (!res.ok) {
        alert(data.detail);
        return;
    }

    document.getElementById("cityDisplay").innerText = data.weather.city;
    document.getElementById("temp").innerText = `${data.weather.temperature}°`;
    document.getElementById("condition").innerText = data.weather.condition;
    document.getElementById("icon").innerText = getIcon(data.weather.condition);

    let windUnit = "km/h";

    if (unit === "us") {
        windUnit = "mph";
    }

    document.getElementById("wind").innerText = `${data.weather.wind} ${windUnit}`;

    document.getElementById("feelsLike").innerHTML =
        `Feels like <span style="font-size:16px; opacity:0.7">${data.weather.sensation}°</span>`;

    setBackground(getBackground(data.weather.condition));
}

// =======================
// FORECAST
// =======================
async function getForecast() {
    const city = getCity();
    const unit = getUnit();

    const res = await fetch(`${baseURL}/weather/forecast?city=${city}&unit=${unit}`);
    const data = await res.json();

    if (!res.ok) {
        alert(data.detail);
        return;
    }

    const container = document.getElementById("forecast");
    container.innerHTML = "";

    const forecast = data.weather?.forecast || [];

    container.innerHTML = forecast.map(day => `
        <div class="forecast-card">
            <div>${day.date}</div>
            <div style="font-size:28px">${getIcon(day.condition)}</div>
            <div>${day.temperature}°</div>
            <div style="opacity:0.7">${day.condition}</div>
        </div>
    `).join("");
}

function loadWeather() {
    getCurrent();
    getForecast();
}

// =======================
// FAVORITES
// =======================
async function addFavorite() {
    const city = getCity();

    const res = await fetch(`${baseURL}/favorites?city=${city}`, {
        method: "POST"
    });

    const data = await res.json();

    alert(data.detail || data.msg);
}

async function loadFavorites() {
    const res = await fetch(`${baseURL}/favorites`);
    const data = await res.json();

    const container = document.getElementById("favorites");

    if (!res.ok) {
        container.innerHTML = data.detail;
        return;
    }

    container.innerHTML = data.favorites
        .map(c => `⭐ ${c}`)
        .join("<br>");
}

async function clearFavorites() {
    const city = getCity();

    const res = await fetch(`${baseURL}/favorites?city=${city}`, {
        method: "DELETE"
    });

    const data = await res.json();

    const container = document.getElementById("favorites");

    if (!res.ok) {
        alert(data.detail);
        return;
    }

    container.innerHTML = data.favorites.length
        ? data.favorites.map(c => `⭐ ${c}`).join("<br>")
        : "<p style='opacity:0.6'>Empty</p>";
}

// =======================
// HISTORIC
// =======================
async function loadHistoric() {
    const res = await fetch(`${baseURL}/historic`);
    const data = await res.json();

    if (!res.ok) {
        document.getElementById("historic").innerHTML = data.detail;
        return;
    }

    document.getElementById("historic").innerHTML = data.historic
        .slice()
        .reverse()
        .map(item => `
            <div class="card" style="display:flex; justify-content:space-between;">
                <div>
                    <strong>📍 ${item.city}</strong><br>
                    <small>🌐 ${item.ip}</small>
                </div>
                <div>⏰ ${item.time}</div>
            </div>
        `).join("");
}

async function clearHistoric() {
    const res = await fetch(`${baseURL}/historic`, {
        method: "DELETE"
    });

    const data = await res.json();

    if (!res.ok) {
        alert(data.detail);
        return;
    }

    document.getElementById("historic").innerHTML =
        "<p style='opacity:0.6'>Empty</p>";
}

// =======================
// INIT
// =======================
window.addEventListener("load", () => {
    setBackground(weatherBackgrounds.default);
});