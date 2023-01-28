#include<iostream>
#include<fstream>
#include<string>
using std::cout;
using std::cin;     //Including from standard library
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;            //Including library for read & write operation in a file
using std::fstream;
using std::ios;


void login();
void registration();      //  Declaring 3 functions  
void forgot();

int main()
{
    int choice;     //Variable declaration

    cout<<"\t\t\t ________________________________________________\n";
    cout<<"\t\t\t               Welcome to the Login Page       \n\n\n";
    cout<<"\t\t\t________________      Menu    ___________________\n\n";
    cout<<"                                                        \n\n";
    cout<<"\t| Press 1 to LOGIN                 |"<<endl;                       /// Making the Interface
    cout<<"\t| Press 2 to REGISTER              |"<<endl;
    cout<<"\t| Press 3 to RESET PASSWORD        |"<<endl;
    cout<<"\t| Press 4 to EXIT                  |"<<endl;
    cout<<"\n\t\t\t Please enter your choice : ";
    cin>>choice;            // Taking input of choice from user 
    cout<<endl;

    switch (choice)
    {
    case 1:
            login();        // Calling the login function, if user inputs 1
        break;
    case 2:
            registration(); // calling the registration function, if user inputs 2
        break;
    case 3:
            forgot();  //calling the forgot function, if user inputs 3
        break;
    case 4:
            cout<<"\t\t\t Thank You! \n\n";
        break;
    
    default:
    system("cls"); // Clears the screen if any previous text is present

        cout<<"\t\t\t Please select from the options given above \n"<<endl;
        main();  // Giving control back to main function
    }
}


// -----------------------------------------Defining login()--------------------------------------


void login()
{
    int count;
    string userId, password, id, pass;

    system("cls");

    cout<<"\t\t\t Please enter the username and password : "<<endl;
    cout<<"\t\t\t USERNAME : ";
    cin>>userId;
    cout<<"\t\t\t PASSWORD : ";
    cin>>password;

    ifstream input("record.txt");  // Opening file for reading purpuse

    while(input>>id>>pass)  // while(var1>>var2>>var3) ==> This method is used to check the value of the variable (if it is already present in the file which is opened) 
    {
        if(id==userId && pass==password)  // Verification of the existing details of user
        {
            count =  1;
            system("cls");
        }
    }
    input.close();  /// Closing the file using close() method
    
    if(count == 1)
    {
        cout<<userId<<"\n Your LOGIN is successful \n Thanks for logging in";
        main();
    }
    else
    {
        cout<<"\n LOGIN ERROR \n Please check your username and password\n";
       
    }
}
// ================================================================================================

// -------------------------------------Defining registration()---------------------------------------

void registration()
{
    string  rUserId, rPassword, rId, rPass;
    system("cls");

    cout<<"\t\t\t Enter the USERNAME : ";
    cin>>rUserId;                               // Taking details for registration
    cout<<"\t\t\t Enter the PASSWORD : ";
    cin>>rPassword;

    ofstream takeInput("record.txt", ios::app); // Opening file for writing/editing purpose. ios::app ==> appends to the end of file; preventing deletion of data.
    takeInput<<rUserId<<" "<<rPassword<<endl;     // object << var1 << var2 ==> Used to store the value of variable in provided file

    system("cls");

    cout<<"\n\t\t\t Registration is Successful ! \n";
    main();

}

// ===================================================================================================

// -------------------------------------Defining forgot()--------------------------------------------------

void forgot()
{
    int option;
    system("cls");
    cout<<"\t\t\t You forgot the password ? No Worries \n";
    cout<<"\t Press 1 to search your id by USERNAME "<<endl;
    cout<<"\t Press 2 to go back to main menu "<<endl;
    cout<<"\t\t\t Enter Your Choice : ";
    cin>>option;
    
    switch (option)
    {
    case 1:
        {
            int count = 0;
            string sUserId,sId,sPass;

            cout<<"\n\t\t\t Enter the USERNAME which you remembered :";
            cin>>sUserId;
            ifstream read("record.txt");  // Opening file for reading purpose
            while (read>>sId>>sPass)        // Validation of value present with user inputs
            {
                if(sId == sUserId)      //Check for UserId (given by the user) exists in the file or not
                {
                    count = 1;
                }
            }
            read.close();

            if(count == 1)
            {
                cout<<"\n\n Your account is found ! \n";
                cout<<"\n\n Your password is : "<<sPass;
                main();
            }
            else 
            {
                cout<<"\n\t Sorry your account is not found!";
            }

        }
        break;
    case 2:
    {
        main();  ///Control will go back to main() menu
    }
        break;
    
    default:
    cout<<"\t\t\t Wrong Choice, Please try again ! "<<endl;
    forgot(); //Giving the control back to forgot() function
        break;
    }
}