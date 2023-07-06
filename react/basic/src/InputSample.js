import React, { useState, useRef } from 'react';

function InputSample() {
    const [inputs, setInputs] = useState({
        name: '',
        nickname: ''
    })

    const nameInput = useRef();

    const { name, nickname } = inputs;

    const onChange = (e) => {
        const { value, name } = e.target;
        setInputs({
            ...inputs, // 기존 인풋 객체 복사
            [name]: value
        });
    }

    const onReset = () => {
        setInputs({
            name: '', // 기존 인풋 객체 복사
            nickname: ''
        });
        nameInput.current.focus();
    }

    return (
        <div>
            <input placeholder='이름' onChange={onChange} value={name} name="name" ref={nameInput} />
            <input placeholder='닉네임' onChange={onChange} value={nickname} name="nickname" />
            <button onClick={onReset}>초기화</button>
            <div>
                <b>값:</b>
                {name} ({nickname})
            </div>
        </div>
    );
}

export default InputSample;