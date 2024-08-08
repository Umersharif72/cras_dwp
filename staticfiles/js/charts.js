function renderChart() {
    const ctx = document.getElementById('myChart').getContext('2d');
    const chartType = document.getElementById('chartType').value;

    // Extract data from the table
    const labels = [];
    const values = [];
    document.querySelectorAll('#lazyBody tr').forEach(row => {
        const cells = row.querySelectorAll('td');
        labels.push(cells[0].textContent);  // Assuming 'Month' is the label
        values.push(cells[2].textContent);  // Assuming 'Value' is the data
    });

    // Destroy previous chart instance if exists
    if (window.myChart) {
        window.myChart.destroy();
    }

    // Create new chart
    window.myChart = new Chart(ctx, {
        type: chartType,
        data: {
            labels: labels,
            datasets: [{
                label: 'Values',
                data: values,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
