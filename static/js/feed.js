$('#button-addon2').click(function(){
    // 세션 값 가져오기
    //const user =  sessionStorage.getItem('nickname')
    const nickname = "성난 개구리 🐸";
    const context = $('#context').val();

    var postdata = {
        "nickname" : nickname,
        "context" : context
    };

    $.ajax({
        type: 'POST',
        url: '/feed',
        data: JSON.stringify(postdata),
        dataType : 'json',
        contentType: "application/json",
        success: function(data){
            alert("통신 성공!!")
        },
        error: function(request, status, error){
            alert('ajax 통신 실패')
            alert(error);
        }
    })
})