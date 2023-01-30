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
var openButton = document.querySelector('.open-delete')
var popup = document.querySelector('.popup')
var closeButton = document.querySelector('.close')


function deleteModal(postId){
    var post =postId.value1;
    var post2 = postId.value2;
    document.getElementById("mytext").innerHTML = post;
    document.getElementById("mytext2").innerHTML = post2;
    popup.style.visibility="visible";
    popup.style.top= "50%";
    popup.style.transform="translate(-50%,-50%) scale(1)";

}


function closeModal(){
    popup.style.top= "0";
    popup.style.transform="translate(-50%,-50%) scale(.1)";
    popup.style.visibility="hidden"; 
}