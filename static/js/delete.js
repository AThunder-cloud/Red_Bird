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
var popup = document.querySelector('.popup')
// var closeButton = document.querySelector('.close')
let post_id;
let post_title;

function deleteModal(postId){
    popup.style.visibility="visible";
    popup.style.top= "50%";
    popup.style.transform="translate(-50%,-50%) scale(1)";
    post_id = postId.value1;
    post_title = postId.value2;
    document.getElementById("mytext").innerHTML = post_id;
    document.getElementById("mytext2").innerHTML = post_title;
}

function passValues(){
    alert("del")
    var data ={'post_id':post_id,'post_title':post_title};
    $.ajax({
        type:'POST',
        url:'Red_Bird/core/views.py/',
        data: data,
        success:function(response){
            alert(response);
        }
    });
}

function closeModal(){
    popup.style.top= "0";
    popup.style.transform="translate(-50%,-50%) scale(.1)";
    popup.style.visibility="hidden"; 
}