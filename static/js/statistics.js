let positive;
let negative;

$("#context").keydown(function(key){
    if(key.keyCode==13) {
        key.preventDefault();
        $('#sentiment-btn').click();
    }
});

$('#sentiment-btn').click(function(e){
    const context = $('#context').val();
    e.preventDefault();

    var postdata = {
        'context' : context
    };
    alert("사용자의 글을 감정분석중 입니다!")
    $.ajax({
        type: 'POST',
        url: '/statistics',
        data: JSON.stringify(postdata),
        dataType : 'json',
        contentType: "application/json",
        
        success: function(result){
            negative = result.result[0] * 100
            positive = result.result[1] * 100

            document.querySelector('#positive-rate').innerHTML = positive

            document.querySelector('#negative-rate').innerHTML = negative
            console.log(negative)
            testSentimentchart.data.datasets[0].data = result.result;
            testSentimentchart.update();
        },
        error: function(jqXHR, status, error){
            alert(error)
        }
    })
    
})
