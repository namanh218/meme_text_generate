var url = document.getElementsByClassName("image")[0].src;
if (url != "http://127.0.0.1:58005/static/ai.jpg"){
    console.log("In If");
    var btn_predict = document.getElementsByClassName("btn-predict")[0];
    btn_predict.addEventListener("click", function(){
        console.log("OPEN SPINNER");
        document.getElementsByClassName("loader")[0].style.display = "block";
      });
}