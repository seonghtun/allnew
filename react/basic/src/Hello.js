import React from 'react';

function Hello({ name, color, isSpecial }) {
    return  <div style={{color}}>
    {isSpecial && <b> * </b>}
    Hello~!! {name}</div>   
}

Hello.defaultProps = {
    name: "NoName"
} // 기본값 값이 없으면 뭐가 뜰지

export default Hello;
 