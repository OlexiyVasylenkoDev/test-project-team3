import React from "react";
import "./logo.scss";

export default function Logo() {
  return (
    <div className="logo">
      <div className="logo_box">
        <div>VILKA</div>
        <div className="vilka">
          <img src="../img/vilka.svg" alt="img" />
        </div>
      </div>
      <div className="lang">
        <div>УКР</div>|<div>ENG</div>
      </div>
    </div>
  );
}
