$(function () {
    console.log("Hello!");
});

$.ajax({
    url:  '/results/list',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        let rows =  '';
        data.results.forEach(result => {
        rows += `	
        <tr>
            <td>${result.value}</td>
            <td>${result.idGame}</td>
            <td>${result.date}</td>
        </tr>`;
    });
        console.log(rows);
    $('#myTable tbody').append(rows); 
    }
});