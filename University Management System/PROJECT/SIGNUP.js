function SignUp(){
    var fName=document.getElementById("fName").value;
    var lName=document.getElementById("lName").value;
    var regn=document.getElementById("regn").value;
    var newpass=document.getElementById("newpass").value;
    var confirmpass=document.getElementById("confirmpass").value;

   if(fName== "" || lName== "" || regn == "" || newpass == "" || confirmpass == "")
   {
       alert("Please fill all the inputs")
   }
    else if (newpass==confirmpass)
    {
     localStorage.setItem("fName1",fName)
     localStorage.setItem("lName2",lName)
      localStorage.setItem("regn1",regn)
    localStorage.setItem("newpass1",newpass)
    localStorage.setItem("confirmpass1",confirmpass)
      
    window.open("login.html")
    }
    else
    {
        alert("New and Confirm Pass must be the same")
    }

}