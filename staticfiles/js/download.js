$(document).ready(function () {
    $(".download-button").click(function () {
      let tableName = $(this).closest(".page").attr("id");
      console.log("Table ID:", tableName);
  
      // Gather data from the table
      let csvData = [];
      let headers = [];
      
      // Get table headers
      $(this).closest(".page").find("table thead th").each(function () {
        headers.push($(this).text().trim());
      });
      
      // Push headers to CSV data
      csvData.push(headers.join(","));
  
      // Get table rows (both th and td)
      $(this).closest(".page").find("table tbody tr").each(function () {
        let rowData = [];
        $(this).find("th, td").each(function () {
          rowData.push($(this).text().trim());
        });
        csvData.push(rowData.join(","));
      });
  
      // Create form and submit for downloading CSV
      let form = $("<form></form>");
      form.attr("method", "POST");
      form.attr("action", generateCsvUrl); // Replace with your URL
  
      // Add CSRF token
      let csrfToken = $('[name=csrfmiddlewaretoken]').val(); // Adjust as per your setup
      let csrfInput = $("<input type='hidden' name='csrfmiddlewaretoken'>").val(csrfToken);
      form.append(csrfInput);
  
      // Add CSV data
      let inputCsv = $("<input type='hidden' name='csv_data'>").val(csvData.join("\n"));
      form.append(inputCsv);
  
      // Add filename based on the table name
      let inputFileName = $("<input type='hidden' name='file_name'>").val(tableName + ".csv");
      form.append(inputFileName);
  
      // Append form to body and submit
      $("body").append(form);
      form.submit();
    });
  });
  