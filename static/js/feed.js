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
        success: function(datas){
            // alert("hi");
            alert(datas[0]['nickname']);
            console.log(datas[0]);
            for(var i=0; i<length(datas); i++){
                alert(datas[i]['nickname'])
                var card = document.createElement("div");
                card.setAttribute("id", "card");
                card.setAttribute("class", "card feed-comment rounded-pill");
                $('#post').append(card);

                var card_header = document.createElement("div");
                card_header.setAttribute("id", "card-header");
                card_header.setAttribute("class", "card-header");
                card_header.innerHTML = datas[i]['nickname'];
                card.append(card_header);

                var card_body = document.createElement("div");
                card_body.setAttribute("id", "card-body");
                card_body.setAttribute("class", "card-body");
                card_header.append(card_body);


                var blockquote = document.createElement("blockquote");
                blockquote.setAttribute("class", "blockquote mb-0");
                card_body.append(blockquote);

                var p =  document.createElement("p");
                p.innerHTML = datas[i]['context'];
                blockquote.append(p);

                var feed_button =  document.createElement("div")
                feed_button.setAttribute("class", "feed-button");
                blockquote.append(feed_button);

                var button = document.createElement("button");
                button.setAttribute("type", "button");
                button.setAttribute("class", "btn btn-dark");
                button.innerHTML = '🙌';
                feed_button.append(button);

                var span = document.createElement("span");
                button.innerHTML = '&nbsp' + datas[i]['thumbs-up'];
                button.append(span);
            }
        },
        error: function(request, status, error){
            alert('ajax 통신 실패')
            alert(error);
        }
    })
})

