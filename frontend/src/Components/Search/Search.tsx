import React, { ChangeEvent, SyntheticEvent, useState } from "react";
import "./search.scss";

export default function Search() {
  const [searchItem, setSearchItem] = useState<string>("");

  const handleEnterText = (e: ChangeEvent<HTMLInputElement>) => {
    setSearchItem(e.target.value);
  };

  return (
    <>
      <div className="custom_input">
        <input
          type="text"
          placeholder="Пошук товару"
          className="input"
          onChange={handleEnterText}
        />
        <img src="../img/lupa.svg" className="lupa" />
        <img src="../img/microphone.svg" className="microphone" />
        <button className="btn">Знайти</button>
      </div>
    </>
  );
}
