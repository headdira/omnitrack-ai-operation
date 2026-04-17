// Sales Popup Notification Logic
const sales = [
    { name: "Carlos de Curitiba", type: "via PIX", time: "2 minutos" },
    { name: "Renata do Rio", type: "no Cartão", time: "5 minutos" },
    { name: "Bruno de BH", type: "via PIX", time: "1 minuto" },
    { name: "Mariana de SP", type: "via PIX", time: "8 minutos" },
    { name: "João de Porto Alegre", type: "no Cartão", time: "12 minutos" }
];

const popup = document.getElementById('sales-popup');
const popupText = document.getElementById('popup-text');

function showSalesNotification() {
    const sale = sales[Math.floor(Math.random() * sales.length)];
    popupText.innerHTML = `<strong>${sale.name}</strong> acabou de comprar<br><span style="color:var(--primary); font-size: 0.7rem;">${sale.type} há ${sale.time}</span>`;
    
    popup.classList.add('active');
    
    setTimeout(() => {
        popup.classList.remove('active');
    }, 5000);
}

// Initial Delay
setTimeout(() => {
    showSalesNotification();
    // Repeat every 15-25 seconds
    setInterval(showSalesNotification, Math.random() * (25000 - 15000) + 15000);
}, 3000);


// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Urgency Logic: Units countdown
let units = 14;
const urgencyText = document.querySelector('.fa-bolt').parentElement;

setInterval(() => {
    if (units > 3 && Math.random() > 0.7) {
        units--;
        urgencyText.innerHTML = `<i class="fas fa-bolt"></i> Apenas ${units} unidades restantes com desconto`;
        urgencyText.style.color = "#ff4444";
        setTimeout(() => urgencyText.style.color = "var(--text-muted)", 500);
    }
}, 10000);

// Interaction Hover Effects
const cards = document.querySelectorAll('.glass');
cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
    });
});

console.log("OmniTrack AI - Engine de Conversão Ativa");
