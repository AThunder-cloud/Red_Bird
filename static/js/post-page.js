const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = 0;
  this.style.height = (this.scrollHeight) + "px";
}

var likeBtn = document.getElementById('post-like-button');

likeBtn.addEventListener('click', function(){
  var postId = likeBtn.getAttribute('data-post-id');
  var csrftoken = getCookie('csrftoken');
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/like-post/');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.setRequestHeader('X-CSRFToken', csrftoken);
  xhr.onload = () => {
    if(xhr.status === 200){
      var response = JSON.parse(xhr.responseText);
      if(response.liked){
        likeBtn.classList.add('liked');
      }else{
        likeBtn.classList.remove('liked');
      }
    }
  };
  xhr.send('post_id='+encodeURIComponent(postId));
});
function getCookie(name){
  var cookieValue =null;
  if(document.cookie && document.cookie !==''){
    var cookie = document.cookie.split(';');
    for(var i=0;i<cookie.length;i++){
      var cookie = cookie[i].trim();
      if(cookie.substring(0,name.length+1)===(name+'=')){
        cookieValue = decodeURIComponent(cookie.substring(name.length+1));
        break;
      }
    }
  }
  return cookieValue;

}