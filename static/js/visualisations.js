var urlPath = window.location.pathname;
var pId;

// Assuming `urlPaths` is an object mapping page IDs to paths
for (var pageId in urlPaths) {
    if (urlPaths[pageId] === urlPath) {
        pId = pageId;
        break;
    }
}

var container = document.querySelector("#" + pId);
console.log(container);

// Variable to store the selected chart type
var selectedChartType;
var canvas = container.querySelector('#chartCanvas');
var ctx = canvas.getContext('2d');
console.log(ctx);

function parseValue(value) {
    // Try parsing as float
    var floatValue = parseFloat(value);
    // If it's not a number, return the original string
    if (isNaN(floatValue)) {
        return value;
    }
    return floatValue;
}

// Function to generate graph based on selected columns and chart type
function generateGraph(chartType) {
    var xAxisIndex = container.querySelector('#xAxis').selectedIndex;
    var yAxisIndex = container.querySelector('#yAxis').selectedIndex;

    console.log(pId);

    // Select the table element using its unique ID
    var table = container.querySelector(".table-responsive table");
    console.log(table);

    var data = [];
    for (var i = 1; i < table.rows.length; i++) {
        // Extract data from each row based on the X-axis and Y-axis indices
        var rowData = {
            x: parseValue(table.rows[i].cells[xAxisIndex].textContent),
            y: parseValue(table.rows[i].cells[yAxisIndex].textContent)
        };

        // Push the extracted data into the data array
        data.push(rowData);
    }

    var chartData = {
        labels: data.map(function (row) { return row.x; }),
        datasets: [{
            label: 'Data',
            data: data.map(function (row) { return row.y; }),
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    var chartOptions = {
        type: chartType, // Set the chart type dynamically based on the parameter
        data: chartData,
        options: {}
    };

    // Destroy previous chart instance if it exists
    if (window.myChart !== undefined) {
        window.myChart.destroy();
    }

    // Render the chart
    window.myChart = new Chart(ctx, chartOptions);
    canvas.style.display = 'block';
}

container.querySelector('#showLineChartButton').addEventListener('click', function () {
    // Get the chart type from the clicked button's attributes or any other source
    selectedChartType = 'line';
    generateGraph(selectedChartType);
});

// Event listener for button click to render graph
container.querySelector('#showBarChartButton').addEventListener('click', function () {
    // Generate graph with the selected chart type
    selectedChartType = 'bar';
    generateGraph(selectedChartType);
});

// Event listener for button click to render graph
container.querySelector('#showPieButton').addEventListener('click', function () {
    // Generate graph with the selected chart type
    selectedChartType = 'pie';
    generateGraph(selectedChartType);
});

// Event listener for button click to render graph
container.querySelector('#showRadarButton').addEventListener('click', function () {
    // Generate graph with the selected chart type
    selectedChartType = 'radar';
    generateGraph(selectedChartType);
});
