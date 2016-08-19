// document.getElementById("firstname").addEventListener("focus",function(){
// document.getElementById("firstname").style.backgroundColor="yellow";
// })
// document.getElementById("firstname").addEventListener("blur",function(){
// document.getElementById("firstname").style.backgroundColor="white";
// })
// document.getElementById("lastname").addEventListener("focus",function(){
// document.getElementById("lastname").style.backgroundColor="yellow";
// })
// document.getElementById("lastname").addEventListener("blur",function(){
// document.getElementById("lastname").style.backgroundColor="white";
// })
// document.getElementById("address").addEventListener("focus",function(){
// document.getElementById("address").style.backgroundColor="yellow";
// })
// document.getElementById("address").addEventListener("blur",function(){
// document.getElementById("address").style.backgroundColor="white";
// })
// document.getElementById("city").addEventListener("focus",function(){
// document.getElementById("city").style.backgroundColor="yellow";
// })
// document.getElementById("city").addEventListener("blur",function(){
// document.getElementById("city").style.backgroundColor="white";
// })
// document.getElementById("state").addEventListener("focus",function(){
// document.getElementById("state").style.backgroundColor="yellow";
// })
// document.getElementById("state").addEventListener("blur",function(){
// document.getElementById("state").style.backgroundColor="white";
// })
//
// document.getElementById("zip").addEventListener("focus",function(){
// document.getElementById("zip").style.backgroundColor="yellow";
// })
// document.getElementById("zip").addEventListener("blur",function(){
// document.getElementById("zip").style.backgroundColor="white";
// })
// document.getElementById("phone").addEventListener("focus",function(){
// document.getElementById("phone").style.backgroundColor="yellow";
// })
// document.getElementById("phone").addEventListener("blur",function(){
// document.getElementById("phone").style.backgroundColor="white";
// })
// document.getElementById("email").addEventListener("focus",function(){
// document.getElementById("email").style.backgroundColor="yellow";
// })
// document.getElementById("email").addEventListener("blur",function(){
// document.getElementById("email").style.backgroundColor="white";
// })
//
// document.getElementById("commentbox").addEventListener("focus",function(){
// document.getElementById("commentbox").style.backgroundColor="yellow";
// })
// document.getElementById("commentbox").addEventListener("blur",function(){
// document.getElementById("commentbox").style.backgroundColor="white";
// })
//
// document.getElementById("submit").addEventListener("click",function(){
//   event.preventDefault()
//   var firstname = document.getElementById("firstname").value
//   var lastname = document.getElementById("lastname").value
//   var address = document.getElementById("address").value
//   var city = document.getElementById("city").value
//   var state = document.getElementById("state").value
//   var zip = document.getElementById("zip").value
//   var phone = document.getElementById("phone").value
//   var email = document.getElementById("email").value
//   var commentbox =document.getElementById("commentbox").value
//
//
//
//
//
//   if (!firstname){
//     document.getElementById("firstname").style.backgroundColor="red";
//     }
//   if (!lastname){
//     document.getElementById("lastname").style.backgroundColor="red";
//   }
//   if (!address){
//     document.getElementById("address").style.backgroundColor="red";
//   }
// if (!city){
//   document.getElementById("city").style.backgroundColor="red";
// }
// if (!state){
//   document.getElementById("state").style.backgroundColor="red";
// }
// if (!zip){
//   document.getElementById("zip").style.backgroundColor="red";
// }
// if(!phone){
//     document.getElementById("phone").style.backgroundColor="red";
// }
// if(!email){
//   document.getElementById("email").style.backgroundColor="red";
// }
// if(!commentbox){
//   document.getElementById("commentbox").style.backgroundColor="red";
// }
// })
$("input[type=text]").focus(function(){
    $(this).css("background-color","yellow");
});

$("input[type=text]").blur(function(){
    $(this).css("background-color","white");
});



 $("#submit").click(function(){
   event.preventDefault();
  var x = $("#firstname").val().length;

    if (x > 1){
      $("#firstname").css('background-color', '');}


  if (x < 1){
    $("#firstname").css('background-color', 'red');}

    var y =$("#lastname").val().length;
    if(y > 1){
      $("#lastname").css('background-color','');}

    if (y < 1){
      $("#lastname").css('background-color','red');}

    var w =$("#address").val().length;
    if (w > 1){
      $("#address").css('background-color','');}
    if (w < 1){
    $("#address").css('background-color','red');}

    var e=$('#city').val().length;
    if (e > 1){
      $("#city").css('background-color','');}
    if(e < 1){
      $("#city").css('background-color','red');}

    var r=$('#state').val().length;
    if(r > 1){
      $('#state').css('background-color','');}
    if(r < 1){
      $('#state').css('background-color','red');}

    var t =$("#zip").val().length;
    if (t > 1){
      $("#zip").css('background-color','');}
    if (t < 1){
      $("#zip").css('background-color','red');}
  var s =$("#phone").val().length;
  if (s > 1){
    $("#phone").css('background-color','');}
  if (s < 1){
    $("#phone").css('background-color','red');}
  var d =$("#email").val().length;
  if (d > 1){
    $("#email").css('background-color','');}
  if (d < 1){
    $("#email").css('background-color','red');}



});

  // var y =document.$("#firstname").val();
    // if ("#firstname".length < 1).style.backgroundColor= "red";}

  // var w = $()
