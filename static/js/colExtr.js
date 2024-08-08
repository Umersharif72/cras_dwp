
document.getElementById('actionCol').addEventListener('change', function() {
    var action = this.value;
    document.getElementById('tablesCol-div').style.display = 'none';
    document.getElementById('api-div').style.display = 'none';
    document.getElementById('file-div').style.display = 'none';

    if (action === 'tables') {
        document.getElementById('tablesCol-div').style.display = 'block';
    } else if (action === 'api') {
        document.getElementById('api-div').style.display = 'block';
    } else if (action === 'file') {
        document.getElementById('file-div').style.display = 'block';
    }
});

document.getElementById('actionCol').dispatchEvent(new Event('change'));
$(document).ready(function() {
// Initialize Select2
$('#jurisdictionCol,  #columns').select2();
});

