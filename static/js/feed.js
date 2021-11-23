$("#context").keydown(function(key){
    if(key.keyCode==13) {
        key.preventDefault();
        $('#button-addon2').click();
    }
});


$('#button-addon2').click(function(e){
    const context = $('#context').val();
    e.preventDefault();
    var postdata = {
        "context" : context
    };
  
    $.ajax({
        type: 'POST',
        url: '/feed',
        data: JSON.stringify(postdata),
        dataType : 'json',
        contentType: "application/json",

        success: function(datas){
            card(datas);
            $("#context").val('');
        },
        error: function(request, status, error){
            alert('ajax 통신 실패')
            alert(error);
        }
    })
})

$(document).on("click",".btn-dark",function(){
    let $dom = $(this); 
    let id = $(this).val();


    $.ajax({
        type: 'UPDATE',
        url: '/likes',
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



function card(datas){
    parent = document.getElementById('card-row');
    for(var i=0; i<datas.length; i++){
        var card_col = document.createElement("div");
        card_col.setAttribute("class", "col-md-6");
        parent.insertBefore(card_col, parent.firstChild);

        var card = document.createElement("div");
        card.setAttribute("id", "card");
        card.setAttribute("class", "card col-md-12 feed-comment");
        // document.getElementById('post').appendChild(card);
        card_col.appendChild(card);
        

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
