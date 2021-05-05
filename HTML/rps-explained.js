//this code is used to be as maleable as possible you can add every fun feature you want you just don't have to do the boring/hard part of it
var users_choice = 3; // here is the users choice change this variable to what the user choose, from 1 to what ever lenght your list is
var Lenght_of_sign = 3; //the Lenght of the sign liste have to be odd or else it wont be balanced 

var range = (Lenght_of_sign - 1) + 1;
var randomNumber = Math.floor( Math.random() * range) + 1;
var computer_choice = randomNumber; 
console.log(randomNumber)  // simplest random number generator  based on how many sign there is 

var be = ((Lenght_of_sign-1)/2) + users_choice //the -1 is to turn the odd into even, in rps you need to beat as much as you  are beaten by sign so whe divide by 2 and add the users choice to see wich one you beat and wich one you don't

if (be>Lenght_of_sign && users_choice>computer_choice){//if we get pass the lenght of the liste, we call this 
    be = ((Lenght_of_sign-1)/2)
    be = (Lenght_of_sign-be) - users_choice
    be = computer_choice + be
    if(0<be){
        console.log('loose');
    } else{
        console.log('win');
    }
} else if (users_choice==computer_choice){ //juste tie, very simple way to set it 
        console.log('tie');
} else if (users_choice<computer_choice){ //if the user choosed a number that is before him in the list
    if (be>=computer_choice){//and we see if it beat the computer choice
        console.log('win');
    } else{
        console.log('loose');//or not
    }
} else {
    if (computer_choice>be){
        console.log('win');
    } else {//remaing possibility can only be a loose
        console.log('loose');
    }
}
console.log('be:', be);
console.log('cpu:',computer_choice);
console.log('user:',users_choice);