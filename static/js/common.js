function putParam(target, datafield ,data) {
    let returnTarget = new Object();
    //기존의 데이터 넣어주고
    returnTarget = target;
    if( data == '')
        return target;

    target[datafield] = data;
    return target;
}

function nonDataFilter(target) {
    for (let id in target) {
        if(target[id] == '')
            delete target[id];
    }
    return target
}


function pad(num) {
    num = num + '';
    return num.length < 2 ? '0' + num : num;
}

function f_date_form(date,type) {
    console.log(date);
    console.log(date);
    console.log(date);
    console.log(date);
    if(date == "")
        return null;
    let dateObj = new Date(date);
    if(type == 'YYYY-MM-DD') {
        return dateObj.getFullYear() + '-' + pad(dateObj.getMonth()+1) + '-' + pad(dateObj.getDate());
    }
    else if(type == 'YYYYMMDD') {
        return dateObj.getFullYear() + pad(dateObj.getMonth()+1) + pad(dateObj.getDate());
    }
    else if (type == 'YYYY-MM') {
        return dateObj.getFullYear() + '-' + pad(dateObj.getMonth()+1);
    }
    else if (type == 'YYYYMM') {
        return dateObj.getFullYear() + pad(dateObj.getMonth()+1);
    }
}

function f_date_add(date, add_num) {
    console.log(date);
    console.log(date);
    console.log(date);
    console.log(date);
    if(date == "NaNNaN")
        return null;
    let dateObj = new Date(date);
    return dateObj.setMonth(dateObj.getMonth()+add_num)
}



/**
 * 문자열이 빈 문자열인지 체크하여 결과값을 리턴한다.
 * @param str       : 체크할 문자열
 */
function isEmpty(str){

    if(typeof str == "undefined" || str == null || str == "")
        return true;
    else
        return false ;
}

/**
 * 문자열이 빈 문자열인지 체크하여 기본 문자열로 리턴한다.
 * @param str           : 체크할 문자열
 * @param defaultStr    : 문자열이 비어있을경우 리턴할 기본 문자열
 */
function nvl(str, defaultStr){

    if(typeof str == "undefined" || str == null || str == "")
        str = defaultStr ;

    return str ;
}

