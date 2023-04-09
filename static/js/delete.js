var popup = document.querySelector('.popup');
var delBtn = document.querySelector('.Confirm-delete');
var item_name;
var post_title;
var csrf_token;
var post_id;

function deleteModal(postId){
    popup.style.visibility="visible";
    popup.style.top= "50%";
    popup.style.transform="translate(-50%,-50%) scale(1)";
    post_title = postId.value1;
    csrf_token = postId.value2;
    item_name = postId.value3;
    post_id = postId.value4;
    document.getElementById("valueName").innerHTML = post_title;
    document.getElementById("itemName").innerHTML = item_name;
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
