
function showGraph(type) {
    // Fetch data from the table
    var table = document.querySelector('#INFO1 .table');
    var labels = [];
    var data = {
        RevGL: [],
        COGSGL: [],
        InvGL: [],
        Vol: []
    };
    
    for (var i = 1, row; row = table.rows[i]; i++) {
        labels.push(row.cells[0].innerText);
        data.RevGL.push(parseFloat(row.cells[1].innerText));
        data.COGSGL.push(parseFloat(row.cells[2].innerText));
        data.InvGL.push(parseFloat(row.cells[3].innerText));
        data.Vol.push(parseFloat(row.cells[5].innerText));
    }
    
    // Define the chart data and configuration
    var chartData = {
        labels: labels,
        datasets: [{
            label: 'RevGL',
            data: data.RevGL,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: false
        }, {
            label: 'COGSGL',
            data: data.COGSGL,
            borderColor: 'rgba(153, 102, 255, 1)',
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            fill: false
        }, {
            label: 'InvGL',
            data: data.InvGL,
            borderColor: 'rgba(255, 159, 64, 1)',
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            fill: false
        }, {
            label: 'Vol',
            data: data.Vol,
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            fill: false
        }]
    };

    var ctx = document.getElementById('myChart').getContext('2d');
    
    // Destroy the previous chart instance if it exists
    if (window.myChartInstance) {
        window.myChartInstance.destroy();
    }

    // Create a new chart instance
    window.myChartInstance = new Chart(ctx, {
        type: type,
        data: chartData,
        options: {
            responsive: true,
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'SKU'
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Values'
                    }
                }
            }
        }
    });
}

