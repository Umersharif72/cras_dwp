document.getElementById('applyFilter').addEventListener('click', function() {
    const filters = {};
    document.querySelectorAll('.filter-container input').forEach(input => {
        if (input.value) {
            filters[input.name] = input.value;
        }
    });

    const rows = document.querySelectorAll('#dataTable tbody tr');
    rows.forEach(row => {
        let showRow = true;
        for (const [column, value] of Object.entries(filters)) {
            const cellIndex = [...row.parentNode.children[0].children].findIndex(th => th.textContent === column);
            const cell = row.querySelector(`td:nth-child(${cellIndex + 1})`);
            if (!cell.textContent.includes(value)) {
                showRow = false;
                break;
            }
        }
        row.style.display = showRow ? '' : 'none';
    });
});