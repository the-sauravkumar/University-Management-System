 function validate()
{
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;

   var username1 = localStorage.getItem("regn1")
    var password1 = localStorage.getItem("confirmpass1")   


    if(username==username1 && password == password1)
    {
       window.open("EXPERIMENTE_9.html");
    }
    else{
        alert('Login failed')
    }
}