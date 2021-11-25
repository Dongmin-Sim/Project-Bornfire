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
            alert('로그인이 필요합니다.')
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
var page = 1;
var scrollchk = true;
var mutex = false;
// 스크롤 감지
$(function(){
    $(window).scroll(function(){
        let $window = $(this);
        let scrollTop = $window.scrollTop();
        let windowHeight = $window.height();
        let documentHeight = $(document).height();

        if(scrollchk){
            if(scrollTop + windowHeight + 230 > documentHeight){
                if (mutex){
                    return;
                }
                mutex = true;
                console.log("hi");
                $('loading').show();
                fetchList(page);
                page++;
                mutex = false;
                scrollchk = true;
                
            }
        }
    })
})

let fetchList = function(page){
    console.log('page: '+page);

    let page_num ={
        "page" : page
    };

    console.log(page_num);
    $.ajax({
        type: "POST",
        url: '/inifinity',
        data: JSON.stringify(page_num),
        contentType: "application/json",
        dataType : 'json',
        beforeSend: function(){
           
        },
        success: function(result){
            //컨트롤러에서 가져온 리스트는 result.data에 담겨오도록 한다.
            //남은 데이터가 0개 이하일 경우 무한 스크롤 종료
            console.log(result, page)
            var res = 1;
            res = card_bottom(result)
        

            let length = res;
            while(length != 0){
                mutex = true;
                scrollhk = false;
                return;
            }
            mutex = false;
            scrollchk = true;
            page ++;
             //데이터 로딩이 끝나면 스크롤체크를 풀어준다.
             //데이터로딩이 끝나면 ajax접근권한을 준다(중복호출 방어)
        },
        complete: function(){
            $('#loading').hide(300);
        }
    });
}


function card_bottom(datas){
    parent = document.getElementById('card-row');
    for(var i=0; i<datas.length; i++){
        var card_col = document.createElement("div");
        card_col.setAttribute("class", "col-md-4");
        parent.appendChild(card_col, parent.firstChild);

        var card = document.createElement("div");
        card.setAttribute("id", "card");
        card.setAttribute("class", "card col-md-12 feed-comment");
        // document.getElementById('post').appendChild(card);
        card_col.appendChild(card);
        

        var card_header = document.createElement("div");
        card_header.setAttribute("id", "card-header");
        card_header.innerHTML = datas[i]['nickname'];
        card.appendChild(card_header);

        
        var card_content = document.createElement("div")
        card_content.setAttribute("class", "card-content")
        card.appendChild(card_content);

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
        card.appendChild(feed_button);
    
        var button = document.createElement("button");
        button.setAttribute("type", "button");
        button.setAttribute("class", "btn btn-dark");
        button.setAttribute("value", datas[i]['_id']);
        button.innerHTML = " 🙌"+ "<span> &nbsp;"+ datas[i]['thumbs-up']+ "</span>";
        feed_button.appendChild(button);        
    }
    return 0;
}

function card(datas){
    parent = document.getElementById('card-row');
    for(var i=0; i<datas.length; i++){
        var card_col = document.createElement("div");
        card_col.setAttribute("class", "col-md-4");
        parent.insertBefore(card_col, parent.firstChild);

        var card = document.createElement("div");
        card.setAttribute("id", "card");
        card.setAttribute("class", "card col-md-12 feed-comment");
        // document.getElementById('post').appendChild(card);
        card_col.appendChild(card);
        

        var card_header = document.createElement("div");
        card_header.setAttribute("id", "card-header");
        card_header.innerHTML = datas[i]['nickname'];
        card.appendChild(card_header);

        
        var card_content = document.createElement("div")
        card_content.setAttribute("class", "card-content")
        card.appendChild(card_content);

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
        card.appendChild(feed_button);
    
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
