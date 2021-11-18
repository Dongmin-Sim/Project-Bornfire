$('#button-addon2').click(function(){
    // 세션 값 가져오기
    //const user =  sessionStorage.getItem('nickname')
    const user = "성난 개구리 🐸";
    const context = $('#context').val();
    


    $.ajax({
        type: 'POST',
        url: '{{url_for("post_feed")}}',
        data: JSON.stringify(postdata),
        dataType : 'JSON',
        contentType: "application/json",
        success: function(data){
            alert('성공! 데이터 값:' + data.result2['id']+" " + data.result2['password']+ " " + data.result2['email'])
        },
        error: function(request, status, error){
            alert('ajax 통신 실패')
            alert(error);
        }
    })
})