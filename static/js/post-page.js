var likeBtn = document.getElementById('post-like-button');
var heartSvg = document.getElementById('heart-svg');

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
        heartSvg.setAttribute("fill", "rgb(255,40,40)");
      }else{
        heartSvg.setAttribute("fill", "grey");
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