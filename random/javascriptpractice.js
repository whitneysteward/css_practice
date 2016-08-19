
function setFocusToTextBox(){
// firstname
    document.getElementById("fullname").focus();
    var firstname = document.getElementById('fullname').value;
   var regex = /^[a-z ,.'-]+$/i;

   if (!regex.test("fullname")) {
     console.log("fullnameregextestfail")
       document.getElementById('fullnameError').textContent = "Please enter in first name!";
       document.getElementById('fullname')
   }


  //  lastname
//
// }
// function setFocusToTextBox(){
// document.getElementById("lastname").focus();
// var lastname = document.getElementById('lastname').value;
// var regex = /^(
// if (!regex.test(lastname)) {
//    document.getElementById('lastnameError').textContent = "Please enter a last name!";
//    document.getElementById('lastname').style.backgroundColor = 'red';
// }

// address

function setFocusToAddress(){
document.getElementById("address").focus();
var address = document.getElementById('address').value;
var regex = /[0-9]+\s*([a-zA-Z]+\s*[a-zA-Z]+\s)*[0-9]*/;
}

if (!regex.test('address')) {
   document.getElementById('addressError').textContent = "Please enter a valid address";
   document.getElementById('address').style.backgroundColor = 'red';
}

    //  city validation
function setFocusToCity(){
document.getElementById("city").focus();
var city = document.getElementById('city').value;
var regex =/^(.+?),([A-z]{2})$/gm;
}

if (!regex.test(city)) {
   document.getElementById('cityError').textContent = "Please enter a valid city ";
   document.getElementById('city').style.backgroundColor = 'red';
     }

// state validation
function setFocusToState(){
  document.getElementById("state").focus();

  var state = document.getElementById('state').value;
}
var regex = /^([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)@([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)[\\.]([a-zA-Z]{2,9})$/;

if (!regex.test(state)) {
   document.getElementById('stateError').textContent = "Please enter a valid state";
   document.getElementById('state').style.backgroundColor = 'red';
     }

function setFocusToZip(){
  document.getElementById("zip").focus();
var zip = document.getElementById('zip').focus();
var regex =/(^[0-9]{4}?[0-9]$|^[0-9]{4}?[0-9]-[0-9]{4}$)/gm;
}
if(!regex.test(zip)){
  document.getElementById('ZipError').textContent ="Please enter a valid zipcode";
  document.getElementById('zip').style.backgroundColor ='red';
}

//{
function setFocustoPhone(){
document.getElementById("phone").focus();
var phone = document.getElementById("phone").focus(
var regex = /(^(1?)(\s?)([\s]?)((\(\d{3}\))|(\d{3}))([\s]?)([\s-]?)(\d{3})([\s-]?)(\d{4})+$)/;

   if (!regex.test(phone)) {
       document.getElementById('phoneError').textContent = "Please enter a valid phone #";
       document.getElementById('phone').style.backgroundColor = 'red';
   }
);
/*{
  function setFocusToTextBox(){
    document.getElementById("comment box").focus();
  }
*/
