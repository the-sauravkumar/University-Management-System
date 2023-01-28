#include<iostream>
using std::cout;
using std::cin;
using std::endl;

int main()
{
    int quantity;   //Number of specific items entered by the user 
    int choice;      //variable to store Choices from below 
    int menu;      //Used here to revert control to specific line of code (i.e. line 35) in case, user enters wrong input in choice variable

    int QuantityOfRooms = 0, QuantityPasta = 0, QuantityBurger = 0, QuantityNoodles = 0, QuantityShake = 0, QuantityChicken = 0;  //Declaring and initiallizing
                                                                                                                                        // Items present


    int SoldRooms = 0, SoldPasta = 0, SoldBurger = 0, SoldNoodles = 0, SoldShake = 0, SoldChicken = 0;      //Declaring and Initiallizing Sold Items

    float Total_roomPrice = 0, Total_pastaPrice = 0, Total_burgerPrice = 0, Total_noodlesPrice = 0, Total_shakePrice = 0, Total_chickenPrice = 0; //Declaring and 
                                                                                                                                    //Initiallizing Total amount present

cout<<"\n\t Quantity of items we have ";
cout<<"\n Rooms available : ";
cin>>QuantityOfRooms;
cout<<"\n\t Quantity of Pasta : ";
cin>>QuantityPasta;
cout<<"\n\t Quantity of Burger : ";             //Taking Input from user of Quantity of Items mentioned above
cin>>QuantityBurger;
cout<<"\n\t Quantity of Noodles : ";
cin>>QuantityNoodles;
cout<<"\n\t Quantity of Shakes : ";
cin>>QuantityShake;
cout<<"\n\t Quantity of Chicken Rolls : ";
cin>>QuantityChicken;

menu:
cout<<"\n\t\t\t Please, Select from the given menu options ";
cout<<"\n\n 1) Rooms    ";
cout<<"\n\n 2) Pasta    ";
cout<<"\n\n 3) Burger   ";
cout<<"\n\n 4) Noodles  ";
cout<<"\n\n 5) Shake    ";
cout<<"\n\n 6) Chicken  ";
cout<<"\n\n 7) Options Regarding Sales and Collections  ";
cout<<"\n\n 8) Exit  ";

cout<<" \n\n Please Enter Your Choice !";
cin>>choice;

switch (choice)
{
case 1:
            cout<<" \n\n Enter the number of rooms you want: ";
            cin>>quantity;                                      //Taking no. of rooms as input from user

            if(QuantityOfRooms - SoldRooms >= quantity)         //Condition for verification of rooms entered by the user are >= Remaining Rooms or not
            {
                SoldRooms += quantity;                          //Adding quantity entered to soldRooms if above condition matches
                Total_roomPrice += (quantity*1200); //Adding total price of room to quantity * 1200 (as per room costs 1200)
                cout<<"\n\n\t\t"<<quantity<<" room/rooms have been alloted to you!";
            }
            else
            {
                cout<<"\n\t Only "<<(QuantityOfRooms - SoldRooms)<<" rooms remaining hotel";
            }

    break;
case 2:
            cout<<" \n\n Enter Pasta Quantity : ";
            cin>>quantity;                                      //

            if(QuantityPasta - SoldPasta >= quantity)         //Condition for verification of Quantity entered by the user are >= Remaining Quantity or not
            {
                SoldPasta += quantity;                          //Adding quantity entered to soldPasta if above condition matches
                Total_pastaPrice += (quantity*150); //Adding total price of room to quantity * 150 (as per plate Pasta costs 150)
                cout<<"\n\n\t\t"<<" Here are your "<<quantity<<" Pasta";
            }
            else
            {
                cout<<"\n\t Only "<<(QuantityPasta - SoldPasta)<<" Pasta is remaining in hotel";
            }
    break;
case 3:
cout<<" \n\n Enter Burger Quantity : ";
            cin>>quantity;                                      //

            if(QuantityBurger - SoldBurger >= quantity)         //Condition for verification of Quantity entered by the user are >= Remaining Quantity or not
            {
                SoldBurger += quantity;                          //Adding quantity entered to soldBurger if above condition matches
                Total_burgerPrice += (quantity*250); //Adding total price of room to quantity * 250 (as per Burger costs 250)
                cout<<"\n\n\t\t"<<" Here are your "<<quantity<<" Burgers";
            }
            else
            {
                cout<<"\n\t Only "<<(QuantityBurger - SoldBurger)<<" Burger is remaining in hotel";
            }
    break;
case 4:
        cout<<" \n\n Enter Noodles Quantity : ";
            cin>>quantity;                                      //

            if(QuantityNoodles - SoldNoodles >= quantity)         //Condition for verification of Quantity entered by the user are >= Remaining Quantity or not
            {
                SoldNoodles += quantity;                          //Adding quantity entered to soldnNoodles if above condition matches
                Total_noodlesPrice += (quantity*350); //Adding total price of room to quantity * 350 (as per plate Noodles costs 350)
                cout<<"\n\n\t\t"<<" Here are your "<<quantity<<" plate/plates of Noodles";
            }
            else
            {
                cout<<"\n\t Only "<<(QuantityNoodles - SoldNoodles)<<" Noodles is remaining in hotel";
            }
    break;
case 5:
        cout<<" \n\n Enter Shake Quantity : ";
            cin>>quantity;                                      //

            if(QuantityShake - SoldShake >= quantity)         //Condition for verification of Quantity entered by the user are >= Remaining Quantity or not
            {
                SoldShake += quantity;                          //Adding quantity entered to soldShake if above condition matches
                Total_shakePrice += (quantity*450); //Adding total price of room to quantity * 450 (as per plate Shakes costs 450)
                cout<<"\n\n\t\t"<<" Here are your "<<quantity<<" glass/glasses of Shake";
            }
            else
            {
                cout<<"\n\t Only "<<(QuantityShake - SoldShake)<<" Shake is/are remaining in hotel";
            }
    break;
case 6:
        cout<<" \n\n Enter Chicken-Rolls Quantity : ";
            cin>>quantity;                                      //

            if(QuantityChicken - SoldChicken >= quantity)         //Condition for verification of Quantity entered by the user are >= Remaining Quantity or not
            {
                SoldChicken += quantity;                          //Adding quantity entered to soldChicken if above condition matches
                Total_chickenPrice += (quantity*500); //Adding total price of room to quantity * 500 (as per plate Chicken-Rolls costs 500)
                cout<<"\n\n\t\t"<<" Here are your "<<quantity<<" plate of Chicken-Rolls";
            }
            else
            {
                cout<<"\n\t Only "<<(QuantityChicken - SoldChicken)<<" Chicken-Rolls is remaining in hotel";
            }
    break;
case 7:
        cout<<"\n\t\t Details of Sales of Collection of Rooms ";
        cout<<"\n\n Number of Rooms we had : "<<QuantityOfRooms;
        cout<<"\n\n Number of Rooms we gave for rent : "<<SoldRooms;                //Printing Details of Rooms Sales and Collections
        cout<<"\n\n Remaining Rooms : "<<(QuantityOfRooms - SoldRooms);         
        cout<<"\n\n Total Rooms collection for the day : "<<Total_roomPrice;

        cout<<"\n\t\t Details of Sales of Collection of Pasta ";
        cout<<"\n\n Number of Pasta we had : "<<QuantityPasta;
        cout<<"\n\n Number of Pasta Sold : "<<SoldPasta;                             //Printing Details of Pasta Sales and Collections
        cout<<"\n\n Remaining Pasta : "<<(QuantityPasta - SoldPasta);
        cout<<"\n\n Total Pasta collection for the day : "<<Total_roomPrice;

        cout<<"\n\t\t Details of Sales of Collection of Burger ";
        cout<<"\n\n Number of Burger we had : "<<QuantityBurger;
        cout<<"\n\n Number of Burger Sold : "<<SoldBurger;                           //Printing Details of Burger Sales and Collections
        cout<<"\n\n Remaining Burger : "<<(QuantityBurger - SoldBurger);
        cout<<"\n\n Total Burger collection for the day : "<<Total_burgerPrice;

        cout<<"\n\t\t Details of Sales of Collection Shake ";
        cout<<"\n\n Number of Shake we had : "<<QuantityShake;
        cout<<"\n\n Number of Shake  : "<<SoldShake;                                 //Printing Details of Shake Sales and Collections
        cout<<"\n\n Remaining Shake : "<<(QuantityShake - SoldShake);
        cout<<"\n\n Total Shake collection for the day : "<<Total_shakePrice;

        cout<<"\n\t\t Details of Sales of Chicken-Rolls ";
        cout<<"\n\n Number of Chicken-Rolls we had : "<<QuantityChicken;
        cout<<"\n\n Number of Chicken-Rolls  : "<<SoldChicken;                       //Printing Details of Chicken-Rolls Sales and Collections
        cout<<"\n\n Remaining Chicken-Rolls : "<<(QuantityChicken - SoldChicken);
        cout<<"\n\n Total Chicken-Rolls collection for the day : "<<Total_chickenPrice;
    break;
case 8:
        exit(0);
default:
        cout<<"\n\t Please Select from the numbers mentioned above!";
}
goto menu;
}