$("#context").keydown(function(key){
    if(key.keyCode==13) {
        $('#button-addon2').click();
    }
});





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
            card(datas)
        },
        error: function(request, status, error){
            alert('ajax 통신 실패')
            alert(error);
        }
    })
})

$(document).on("click",".btn-dark",function(){
    
    console.log($(this).val())
    let $dom = $(this); 
    console.log($dom)
    let id = $(this).val();

    $.ajax({
        type: 'UPDATE',
        url: '/thumbs',
        data: JSON.stringify(id),
        dataType : 'json',
        contentType: "application/json",
        success: function(thumbs_up){
            console.log(thumbs_up)
            $dom.html("🙌 <span> &nbsp;" + thumbs_up + "</span>"); 
        },
        error: function(request, status, error){
            alert('ajax 통신 실패')
            alert(error);
        }
    })

});

function post(){
    
}


function card(datas){
    parent = document.getElementById('post');
    for(var i=0; i<datas.length; i++){
        var card = document.createElement("div");
        card.setAttribute("id", "card");
        card.setAttribute("class", "card feed-comment rounded-pill");
        // document.getElementById('post').appendChild(card);
        parent.insertBefore(card, parent.firstChild);

        var card_header = document.createElement("div");
        card_header.setAttribute("id", "card-header");
        card_header.setAttribute("class", "card-header");
        card_header.innerHTML = datas[i]['nickname'];
        card.appendChild(card_header);

        var card_body = document.createElement("div");
        card_body.setAttribute("id", "card-body");
        card_body.setAttribute("class", "card-body");
        card.appendChild(card_body);


        var blockquote = document.createElement("blockquote");
        blockquote.setAttribute("class", "blockquote mb-0");
        card_body.appendChild(blockquote);

        var p =  document.createElement("p");
        p.innerHTML = datas[i]['context'];
        blockquote.appendChild(p);
     
        var feed_button =  document.createElement("div")
        feed_button.setAttribute("class", "feed-button");
        blockquote.appendChild(feed_button);
    
        var button = document.createElement("button");
        button.setAttribute("type", "button");
        button.setAttribute("class", "btn btn-dark");
        button.setAttribute("value", datas[i]['_id']);
        button.innerHTML = " 🙌"+ "<span> &nbsp;"+ datas[i]['thumbs-up']+ "</span>";
        feed_button.appendChild(button);        
    }
}

// function button_click(ObjectId){
    
//     $.ajax({
//         type: 'UPDATE',
//         url: '/thumbs',
//         data: JSON.stringify(ObjectId),
//         dataType : 'json',
//         contentType: "application/json",
//         success: function(thumbs_up){
//             console.log($(this));
//             $(this).innerHTML = "🙌"+ "<span>" + "&nbsp;"+ thumbs_up + "</span>";
//         },
//         error: function(request, status, error){
//             alert('ajax 통신 실패')
//             alert(error);
//         }
//     })


// }
