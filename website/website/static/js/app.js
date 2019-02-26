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
            <td>${result.game_name}</td>
            <td>${result.user_name}</td>
        </tr>`;
    });
    $('#myTable tbody').append(rows); 
    }
});