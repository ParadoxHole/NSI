//this is the fastest the safware can go no extra variable no extra calculation 
var L = 9;
var range = (L - 1) + 1;
var randomNumber = Math.floor( Math.random() * range) + 1; 
var uc=6;
var cc=randomNumber;
var be = ((L-1)/2) + uc;

if (be>L && uc>cc) {
    be = cc + (L-((L-1)/2)) - uc
    if(0<be) {console.log('loose');}
    else {console.log('win');} 
}else if (uc==cc) {console.log('tie');}  
else if (uc<cc)
    if (be>=cc) {console.log('win');}
    else {console.log('loose');}  
else
    if (cc>be) {console.log('win');}
    else {console.log('loose');} 

    if (be>L && uc>cc) {
        be = cc + (L-((L-1)/2)) - uc
        if(0<be) {console.log('loose');}
        else {console.log('win');} 
    }else if (uc==cc) {console.log('tie');}  
    else if (uc<cc)
        if (be>=cc) {console.log('win');}
        else {console.log('loose');}  
    else
        if (cc>be) {console.log('win');}
        else {console.log('loose');}
        
