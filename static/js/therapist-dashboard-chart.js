const ctx = document.getElementById("myChart");

new Chart(ctx, {
    type: "bar", 
    data: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], 
        datasets: [
            {
                label: "Solutions", 
                data: [32, 32, 28, 48, 22, 32, 48], 
                backgroundColor: "#A6A8A6", 
                borderWidth: 1, 
                barThickness: 15, 
                borderRadius: 20, 
                fill: false,
            },
        ],
    },
    options: {
        scales: {
            x: {
                beginAtZero: true, 
                grid: {
                    display: false,
                },
            },
            y: {
                beginAtZero: true,
                barPercentage: 10, 
                categoryPercentage: 10, 
                grid: {
                    color: "#EDEEED", 
                    borderWidth: 5,
                    borderDash: [1, 1], 
                    drawBorder: false,
                    drawTicks: false,
                },
                tick: {
                    stepSize: 10,
                },

                labels: ["0", "10", "20", "30", "40", "50", "60"],
            },
        },
        layout: {
            padding: {
                left: 50,
            },
        },

        maintainAspectRatio: false,
        height: 300,
    },
});
