import React from 'react'; // 첫번째 줄은 항상들어간다.

function Wrapper({ children }) {
    const style = {
        border : '2px solid black',
        padding : '16px'
    };
    return (
        <div style={style}>
        { children }
        </div>
    )
}

export default Wrapper