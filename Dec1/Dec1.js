const fs = require('fs');
let text = String(fs.readFileSync('Input.txt'));
text = text.split("\r\n");
let result = [];
let numFound = false;

for(let i = 0; i < text.length; i++){
    let curLine = text[i];
    numFound = false;

    for(let j = 0; j < curLine.length && !numFound; j++){
        for(let k = 1; k <= 10 && !numFound; k++){
            if(k == curLine[j]){
                result[i] = k*10;
                numFound = true;
            }
        }
        if(curLine[j] == 'o'){
            if(curLine[j+1] == 'n'){
                if(curLine[j+2] == 'e'){
                    result[i] = 10;
                    numFound = true;
                }
            }
        }
        else if(curLine[j] == 't'){
            if(curLine[j+1] == 'w' && curLine[j+2] == 'o'){
                result[i] = 20;
                numFound = true;
            }
            else if(curLine[j+1] == 'h' && curLine[j+2] == 'r' && curLine[j+3] == 'e' && curLine[j+4] == 'e'){
                result[i] = 30;
                numFound = true;
            }
        }
        else if(curLine[j] == 'f'){
            if(curLine[j+1] == 'o' && curLine[j+2] == 'u' && curLine[j+3] == 'r'){
                result[i] = 40;
                numFound = true;
            }
            else if(curLine[j+1] == 'i' && curLine[j+2] == 'v' && curLine[j+3] == 'e'){
                result[i] = 50;
                numFound = true;
            }
        }
        else if(curLine[j] == 's'){
            if(curLine[j+1] == 'i' && curLine[j+2] == 'x'){
                result[i] = 60;
                numFound = true;
            }
            if(curLine[j+1] == 'e' && curLine[j+2] == 'v' && curLine[j+3] == 'e' && curLine[j+4] == 'n'){
                result[i] = 70;
                numFound = true;
            }
        }
        else if(curLine[j] == 'e' && curLine[j+1] == 'i' && curLine[j+2] == 'g' && curLine[j+3] == 'h' && curLine[j+4] == 't'){
            result[i] = 80;
            numFound = true;
        }
        else if(curLine[j] == 'n' && curLine[j+1] == 'i' && curLine[j+2] == 'n' && curLine[j+3] == 'e'){
            result[i] = 90;
            numFound = true;
        } 
    }
    numFound = false;

    for(let j = curLine.length - 1; j >= 0 && !numFound; j--){
        for(let k = 1; k <= 10 && !numFound; k++){
            if(k == curLine[j]){
                result[i] += k;
                numFound = true;
            }
        }

        if(curLine[j] == 'e'){
            if(curLine[j-1] == 'n'){
                if(curLine[j-2] == 'o'){
                    result[i] += 1;
                    numFound = true;
                }
                else if(curLine[j-2] == 'i' && curLine[j-3] == 'n'){
                    result[i] += 9;
                    numFound = true;
                }
            }
            else if(curLine[j-1] == 'e' && curLine[j-2] == 'r' && curLine[j-3] == 'h' && curLine[j-4] == 't'){
                result[i] += 3;
                numFound = true;
            }
            else if(curLine[j-1] == 'v' && curLine[j-2] == 'i' && curLine[j-3] == 'f'){
                result[i] += 5;
                numFound = true;
            }
        }
        else if(curLine[j] == 'o' && curLine[j-1] == 'w' && curLine[j-2] == 't'){
            result[i] += 2;
            numFound = true;
        }
        else if(curLine[j] == 'r' && curLine[j-1] == 'u' && curLine[j-2] == 'o' && curLine[j-3] == 'f'){
            result[i] += 4;
            numFound = true;
        }
        else if(curLine[j] == 'x' && curLine[j-1] == 'i' && curLine[j-2] == 's'){
            result[i] += 6;
            numFound = true;
        }
        else if(curLine[j] == 'n' && curLine[j-1] == 'e' && curLine[j-2] == 'v' && curLine[j-3] == 'e' && curLine[j-4] == 's'){
            result[i] += 7;
            numFound = true;
        }
        else if(curLine[j] == 't' && curLine[j-1] == 'h' && curLine[j-2] == 'g' && curLine[j-3] == 'i' && curLine[j-4] == 'e'){
            result[i] += 8;
            numFound = true;
        }
    }
}

let add = 0;

for(let i = 0; i < result.length; i++){
    add += result[i];
}
console.log(add);