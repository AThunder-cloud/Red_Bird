// var popup = document.getElementById("popup");
// var open = document.getElementsByClassName("open-delete");
// var close = document.getElementById('close')
// open.onclick =function(){
// popup.style.visibility="visible";
// popup.style.top= "50%";
// popup.style.transform="translate(-50%,-50%) scale(1)"; 

// }
// close.onclick =function(){
// popup.style.top= "0";
// popup.style.transform="translate(-50%,-50%) scale(.1)";
// popup.style.visibility="hidden"; 
// }
// var openButton = document.querySelector('.open-delete')
var popup = document.querySelector('.popup');
var delBtn = document.querySelector('.Confirm-delete');
var post_id;
var post_title;
var csrf_token;

function deleteModal(postId){
    popup.style.visibility="visible";
    popup.style.top= "50%";
    popup.style.transform="translate(-50%,-50%) scale(1)";
    post_id = postId.value1;
    post_title = postId.value2;
    document.getElementById("mytext").innerHTML = post_id;
    document.getElementById("mytext2").innerHTML = post_title;
}



function passValues(token){
    // var data ={'post_id':post_id,'post_title':post_title};
    csrf_token = token.value1;
    alert(csrf_token)
    $.ajax({
        type:'POST',
        url:delBtn.dataset.url,
        headers:{
            "X_CSRFToken":csrf_token,
        },
        data: {
            'post_id':post_id,        
        },
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success :function(response){
            alert(response);
        },
        error: function(xhr,status,error){
            alert("unsuccessfull...!!!")
        }
    });
}

function closeModal(){
    popup.style.top= "0";
    popup.style.transform="translate(-50%,-50%) scale(.1)";
    popup.style.visibility="hidden"; 
}