function validatePassword()
{
    var oldpass=document.getElementById("oldpass").value;
    var newpass=document.getElementById("newpass").value;
    var confirmpass=document.getElementById("confirmpass").value;

    var oldpass1= localStorage.getItem("confirmpass1")
    
        if (oldpass == "" || newpass == "" || confirmpass == "")
         {
            alert('Please fill all the details');
         }
         else if (oldpass != oldpass1 )
         alert("Enter Correct Old Password")
         else if(oldpass==newpass)
         {
             alert('Old and New passwords cannot be the same')
         }
         else if(newpass!=confirmpass)
         {
             alert('New Pass and Confirm Pass are not the same')
         }
         else
         {
           var resettpass=localStorage.setItem("confirmpass1",newpass)
             alert('Password Changed Sucessfully')
             window.open("login.html")
         }
    }