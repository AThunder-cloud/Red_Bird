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
    csrf_token = postId.value3;
    document.getElementById("mytext").innerHTML = post_id;
    document.getElementById("mytext2").innerHTML = post_title;
}



function passValues(token){
    $.ajax({
        type:'POST',
        url:"/delete/" + post_id + '/',
        data: {
            csrfmiddlewaretoken:csrf_token,   
        },
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success :function(response){
            if(response.success){
                alert("Successfull.....!!")
                location.reload()
            }else{
                alert("Unsuccessfull....!!")
            }
        },
        error: function(xhr,status,error){
            alert("There is an error in deleteing the post...!!!")
        }
    });
    popup.style.top= "0";
    popup.style.transform="translate(-50%,-50%) scale(.1)";
    popup.style.visibility="hidden"; 
}

function closeModal(){
    popup.style.top= "0";
    popup.style.transform="translate(-50%,-50%) scale(.1)";
    popup.style.visibility="hidden"; 
}