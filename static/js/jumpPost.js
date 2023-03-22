
// const postPage = document.querySelector(".postpopup");
// var post_id;
// function jumpPost(postId){
//     post_id = postId.value1;
//     csrf_token = postId.value2;
//     // postPage.style.visibility="visible";
//     // postPage.style.opacity="1";
//     // postPage.style.transform="translate(-50%,45px) scale(1)";
//     $.ajax({
//         type:'POST',
//         url:"/postpage/" + post_id + '/',
//         data: {
//             csrfmiddlewaretoken:csrf_token,   
//         },
//         contentType:"application/json; charset=utf-8",
//         dataType:"json",
//     });

// }



  


// let xhr = new XMLHttpRequest();
// let url = "/postpage/" + post_id + '/';
// xhr.open("GET", url, true);
// xhr.responseType = "json";
// xhr.onload = () => {
//     if (xhr.status === 200){
//         let postData = xhr.response;
//         let postTitle = document.getElementById('context-title');

//         postTitle.textContent = postData.title;
//     }else{
//         console.log("request failed"+xhr.status);
//     }
// };
// xhr.send();