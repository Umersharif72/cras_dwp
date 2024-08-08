document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        console.log('File selected:', file.name);
        const reader = new FileReader();
        reader.onload = function(e) {
            console.log('File loaded successfully');
            const data = new Uint8Array(e.target.result);
            try {
                const workbook = XLSX.read(data, { type: 'array' });
                const sheetName = workbook.SheetNames[0];
                const worksheet = workbook.Sheets[sheetName];
                const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
                console.log('Parsed JSON:', json);
                displayFileContent(json);
                setupColumnSelectors(json);
                setupVisualizationOptions(json);
            } catch (error) {
                console.error('Error reading file:', error);
            }
        };
        reader.readAsArrayBuffer(file);
    } else {
        console.log('No file selected');
    }
});

function displayFileContent(rows) {
    console.log('Displaying file content');
    const tableContainer = document.getElementById('tableContainer');
    tableContainer.innerHTML = '';

    if (rows.length === 0) {
        console.log('No data to display');
        tableContainer.textContent = 'No data to display';
        return;
    }

    const table = document.createElement('table');

    rows.forEach((row, index) => {
        const tr = document.createElement('tr');
        row.forEach(column => {
            const cell = document.createElement(index === 0 ? 'th' : 'td');
            cell.textContent = column !== undefined ? column : '';
            tr.appendChild(cell);
        });
        table.appendChild(tr);
    });

    tableContainer.appendChild(table);
    console.log('Table appended to container');
}

function setupColumnSelectors(data) {
    const columnSelector = document.getElementById('columnSelector');
    columnSelector.style.display = 'block';

    const xAxisSelect = document.getElementById('xAxis');
    const yAxisSelect = document.getElementById('yAxis');
    
    const headers = data[0]; // Assuming first row contains headers

    headers.forEach((header, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = header;
        xAxisSelect.appendChild(option);
        yAxisSelect.appendChild(option.cloneNode(true)); // Clone to avoid reference issues
    });
}

function setupVisualizationOptions(data) {
    document.getElementById('visualizationOptions').style.display = 'block';

    document.getElementById('barChartButton').addEventListener('click', () => createChart('bar', data));
    document.getElementById('lineChartButton').addEventListener('click', () => createChart('line', data));
    document.getElementById('pieChartButton').addEventListener('click', () => createChart('pie', data));
}

function createChart(type, data) {
    const xAxisIndex = parseInt(document.getElementById('xAxis').value);
    const yAxisIndex = parseInt(document.getElementById('yAxis').value);

    const labels = data.slice(1).map(row => row[xAxisIndex]);
    const values = data.slice(1).map(row => row[yAxisIndex]);

    const chartData = {
        labels: labels,
        datasets: [{
            label: 'Dataset',
            data: values,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    const chartConfig = {
        type: type,
        data: chartData,
        options: {}
    };

    const chartContainer = document.getElementById('chartContainer');
    chartContainer.style.display = 'block';

    const chartCanvas = document.getElementById('chartCanvas').getContext('2d');
    if (window.myChart) {
        window.myChart.destroy();
    }
    window.myChart = new Chart(chartCanvas, chartConfig);
}